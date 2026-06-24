"""
Unified data loader — single entry point for all Phase 2 data sources.

Usage:
    from data.loader import load_all, load_for_agent

    # All documents from every source
    all_docs = load_all()

    # Documents relevant to a specific agent
    research_docs = load_for_agent("research")    # abstracts + real pubmed
    diagnosis_docs = load_for_agent("diagnostic") # encounters + diagnostic cases + vitals
    docs_docs      = load_for_agent("documentation") # transcripts + encounters
    coord_docs     = load_for_agent("coordination")   # referrals + encounters
    surgical_docs  = load_for_agent("surgical")       # surgical frames

    # Real public data only (for RAG corpus seeding with real evidence)
    real_docs = load_real_public(query="heart failure SGLT2", max_results=10)
"""

from schemas import Document, DataTag

from data.synthetic.research_corpus import get_research_corpus
from data.synthetic.transcripts import get_transcripts
from data.synthetic.encounters import get_encounters
from data.synthetic.referrals import get_referrals
from data.synthetic.diagnostic_cases import get_diagnostic_cases
from data.randomised.vitals import get_vitals
from data.randomised.surgical_frames import get_surgical_frames
from data.real_public.pubmed import fetch_pubmed_abstracts


_AGENT_SOURCES = {
    "research": ["research_corpus", "pubmed_real"],
    "documentation": ["transcripts", "encounters"],
    "diagnostic": ["encounters", "diagnostic_cases", "vitals"],
    "coordination": ["referrals", "encounters"],
    "surgical": ["surgical_frames"],
}


def load_all(
    include_real_public: bool = False,
    pubmed_query: str = "sepsis management clinical guidelines",
    pubmed_max: int = 5,
) -> list[Document]:
    """
    Returns all documents from all data sources.

    Args:
        include_real_public: If True, fetches live PubMed abstracts.
                             Disabled by default (requires network).
        pubmed_query: Query string for PubMed fetch (used only if include_real_public=True).
        pubmed_max: Max real PubMed results to fetch.
    """
    docs: list[Document] = []
    docs.extend(get_research_corpus())
    docs.extend(get_transcripts())
    docs.extend(get_encounters())
    docs.extend(get_referrals())
    docs.extend(get_diagnostic_cases())
    docs.extend(get_vitals())
    docs.extend(get_surgical_frames())

    if include_real_public:
        docs.extend(fetch_pubmed_abstracts(pubmed_query, pubmed_max))

    return docs


def load_for_agent(
    agent_name: str,
    include_real_public: bool = False,
    pubmed_query: str = "clinical evidence",
    pubmed_max: int = 5,
) -> list[Document]:
    """
    Returns documents relevant to a specific agent.

    Args:
        agent_name: One of: research, documentation, diagnostic, coordination, surgical.
        include_real_public: If True, also fetches live PubMed for research agent.
        pubmed_query: PubMed query (research agent only).
        pubmed_max: Max PubMed results (research agent only).
    """
    sources = _AGENT_SOURCES.get(agent_name.lower(), [])
    docs: list[Document] = []

    if "research_corpus" in sources:
        docs.extend(get_research_corpus())
    if "transcripts" in sources:
        docs.extend(get_transcripts())
    if "encounters" in sources:
        docs.extend(get_encounters())
    if "referrals" in sources:
        docs.extend(get_referrals())
    if "diagnostic_cases" in sources:
        docs.extend(get_diagnostic_cases())
    if "vitals" in sources:
        docs.extend(get_vitals())
    if "surgical_frames" in sources:
        docs.extend(get_surgical_frames())
    if "pubmed_real" in sources and include_real_public:
        docs.extend(fetch_pubmed_abstracts(pubmed_query, pubmed_max))

    return docs


def load_real_public(
    query: str = "sepsis clinical guidelines",
    max_results: int = 10,
) -> list[Document]:
    """
    Fetches real PubMed abstracts only (REAL_PUBLIC tag).
    Useful for seeding the RAG corpus with genuine evidence.
    """
    return fetch_pubmed_abstracts(query, max_results)


def summarise(docs: list[Document]) -> dict:
    """Returns tag counts and source type counts for a document list."""
    tag_counts: dict[str, int] = {}
    source_counts: dict[str, int] = {}
    for doc in docs:
        tag_counts[doc.tag.value] = tag_counts.get(doc.tag.value, 0) + 1
        src = doc.metadata.get("source_type", "unknown")
        source_counts[src] = source_counts.get(src, 0) + 1
    return {
        "total": len(docs),
        "by_tag": tag_counts,
        "by_source": source_counts,
    }
