"""
Core data schemas for the Clinical AI Platform.

Every module imports from here — nothing defines its own data shapes.

Design notes:
  - Pydantic BaseModel for all transfer objects (validation + JSON serialization)
  - TypedDict for GraphState (required by LangGraph)
  - Every field is tagged with its data tag in a comment: REAL / REAL-PUBLIC / SYNTHETIC / RANDOMISED
"""

from __future__ import annotations

from typing import Any, Optional
from typing_extensions import TypedDict, Annotated
from pydantic import BaseModel, Field
from enum import Enum
import operator


# ── Enums ──────────────────────────────────────────────────────────────────────

class Intent(str, Enum):
    """Possible intents the classify_intent node can assign to a request."""
    RESEARCH       = "research"       # clinical evidence question
    DOCUMENTATION  = "documentation"  # SOAP note generation
    DIAGNOSTIC     = "diagnostic"     # differential diagnosis / risk score
    COORDINATION   = "coordination"   # referral triage / prior-auth
    SURGICAL       = "surgical"       # surgical analytics / video review
    UNKNOWN        = "unknown"        # fallback if classifier is unsure


class DataTag(str, Enum):
    """Data provenance tags — every piece of data carries exactly one."""
    REAL        = "REAL"         # genuine PHI source (only simulated in PoC)
    REAL_PUBLIC = "REAL_PUBLIC"  # real public non-PHI data (e.g. PubMed)
    SYNTHETIC   = "SYNTHETIC"   # realistic fake data, no PHI
    RANDOMISED  = "RANDOMISED"  # random placeholder, proves wiring only


class Urgency(str, Enum):
    """Urgency levels for referrals."""
    ROUTINE   = "routine"
    URGENT    = "urgent"
    EMERGENT  = "emergent"


# ── 1. Citation ────────────────────────────────────────────────────────────────

class Citation(BaseModel):
    """A reference to a source document used in an agent's answer."""

    source: int                          # REAL*  — index number in the source list
    title: str                           # SYNTHETIC — document title
    score: float = Field(ge=0.0, le=1.0) # REAL*  — retrieval relevance score
    doi: Optional[str] = None            # SYNTHETIC — DOI if available


# ── 2. Document ────────────────────────────────────────────────────────────────

class Document(BaseModel):
    """
    The atomic unit stored in the vector DB.
    One document = one chunk of text with its embedding and metadata.
    """

    id: str                              # REAL*  — chunk id (structure real, content synthetic)
    text: str                            # SYNTHETIC — chunk text (marked synthetic in PoC)
    metadata: dict[str, Any] = Field(   # SYNTHETIC — title, source_type, year, doi, evidence_grade
        default_factory=dict
    )
    embedding: Optional[list[float]] = None  # REAL* — vector; None until embedded
    tag: DataTag = DataTag.SYNTHETIC         # data provenance tag


# ── 3. SearchHit ───────────────────────────────────────────────────────────────

class SearchHit(BaseModel):
    """What retrieval returns — a Document plus its relevance score."""

    document: Document
    score: float = Field(ge=0.0, le=1.0)  # REAL* — similarity/relevance score
    rank: int                              # REAL* — position in the result list


# ── 4. AgentRequest ────────────────────────────────────────────────────────────

class AgentRequest(BaseModel):
    """What the brain sends to an agent to kick off its pipeline."""

    query: str                             # REAL — the question or task text
    session_id: str                        # REAL — session key
    context: dict[str, Any] = Field(      # mixed — shared state from the brain
        default_factory=dict
    )
    payload: dict[str, Any] = Field(      # SYNTHETIC — agent-specific extra input
        default_factory=dict
    )


# ── 5. AgentResponse ───────────────────────────────────────────────────────────

class AgentResponse(BaseModel):
    """What an agent returns to the brain after completing its pipeline."""

    agent: str                             # REAL  — which agent produced this
    answer: str                            # REAL* — the agent's output text
    sources: list[Citation] = Field(       # SYNTHETIC — citations used
        default_factory=list
    )
    metrics: dict[str, Any] = Field(       # REAL* — faithfulness, citation_coverage,
        default_factory=dict               #         flagged, model, latency_ms
    )


# ── 6. EvalResult ──────────────────────────────────────────────────────────────

class EvalResult(BaseModel):
    """
    Grounding and quality scores produced by the evaluate node.
    Determines whether human review is required.
    """

    faithfulness: float = Field(ge=0.0, le=1.0)      # REAL — how grounded is the answer?
    citation_coverage: float = Field(ge=0.0, le=1.0)  # REAL — fraction of claims cited
    flagged: bool                                      # REAL — True → send to human_review
    verdict: str = "unknown"                           # REAL — grounded | partial | ungrounded


# ── 7. SessionState ────────────────────────────────────────────────────────────

class SessionState(BaseModel):
    """
    Per-session cache stored in the StateStore (Redis or in-memory).
    Holds conversation history and context so agents have continuity.
    """

    session_id: str                        # REAL  — unique session key
    history: list[dict[str, Any]] = Field( # REAL* — prior turns in this session
        default_factory=list
    )
    context_cache: dict[str, Any] = Field( # SYNTHETIC — cached patient/encounter context
        default_factory=dict
    )
    updated_at: Optional[str] = None       # REAL  — ISO timestamp; used for TTL expiry


# ── 8. GraphState ──────────────────────────────────────────────────────────────
#
# TypedDict is required by LangGraph — it uses it to build the state graph.
# The Annotated[list, operator.add] pattern tells LangGraph how to merge
# parallel updates: lists are appended (not overwritten) when two nodes
# both write to the same list field at the same time.

class GraphState(TypedDict, total=False):
    """
    The single shared state object that flows through every LangGraph node.

    Every node reads from this and writes back to it.
    It is checkpointed after each node so the graph can pause (interrupt)
    and resume reliably — even minutes later.
    """

    # ── Identity & request ────────────────────────────────────────────────────
    session_id: str                  # REAL — conversation/session key
    user: dict[str, Any]             # REAL — {id, role} for RBAC and audit
    request: dict[str, Any]          # REAL — {query, payload}

    # ── Routing ───────────────────────────────────────────────────────────────
    intent: str                      # REAL* — set by classify_intent node
    route: list[str]                 # REAL* — agent names selected by route node

    # ── Context & retrieval ───────────────────────────────────────────────────
    patient_context: dict[str, Any]  # SYNTHETIC — context fetched for the session
    retrieved: list[SearchHit]       # SYNTHETIC — RAG context for agents

    # ── Agent outputs ─────────────────────────────────────────────────────────
    agent_outputs: dict[str, AgentResponse]  # REAL* — output per agent that ran

    # ── Evaluation & human review ─────────────────────────────────────────────
    eval: EvalResult                 # REAL  — grounding/quality scores
    requires_human_review: bool      # REAL  — True → interrupt at human_review node
    human_decision: dict[str, Any]   # REAL  — {approved, edits} set on resume

    # ── Output ────────────────────────────────────────────────────────────────
    final_output: dict[str, Any]     # REAL* — the delivered result

    # ── Reliability ───────────────────────────────────────────────────────────
    # Annotated with operator.add so parallel nodes append, not overwrite
    errors: Annotated[list[dict[str, Any]], operator.add]  # REAL — node failures
    audit: Annotated[list[dict[str, Any]], operator.add]   # REAL — append-only trace
