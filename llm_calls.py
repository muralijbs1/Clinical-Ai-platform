"""
All LLM calls in the system live here — nothing else.

Every agent imports from this file. Nobody calls call_llm() directly anywhere else.

Each function:
  1. Pulls the prompt from prompts/prompts.py
  2. Calls call_llm() from providers/llm_client.py
  3. Returns the LLMResponse

PHI flag: set contains_phi=True when patient data is in the prompt.
          This routes to the phi_safe provider defined in config.yaml.
"""

from prompts.prompts import (
    classify_intent_prompt,
    research_synthesize_prompt,
    research_query_expansion_prompt,
    documentation_soap_prompt,
    documentation_coding_prompt,
    diagnostic_differentials_prompt,
    coordination_extraction_prompt,
    coordination_prior_auth_prompt,
    surgical_annotation_prompt,
    grounding_check_prompt,
)
from providers.llm_client import call_llm, LLMResponse


# ── Brain ──────────────────────────────────────────────────────────────────────

def call_classify_intent(query: str) -> LLMResponse:
    system, user = classify_intent_prompt(query)
    return call_llm(system, user, contains_phi=False)


# ── Research Agent ─────────────────────────────────────────────────────────────

def call_research_synthesize(query: str, retrieved: list[dict]) -> LLMResponse:
    system, user = research_synthesize_prompt(query, retrieved)
    return call_llm(system, user, contains_phi=False)


def call_research_query_expansion(query: str) -> LLMResponse:
    system, user = research_query_expansion_prompt(query)
    return call_llm(system, user, contains_phi=False)


# ── Documentation Agent ────────────────────────────────────────────────────────

def call_documentation_soap(transcript: str, context: dict) -> LLMResponse:
    system, user = documentation_soap_prompt(transcript, context)
    return call_llm(system, user, contains_phi=True)


def call_documentation_coding(soap_note: str) -> LLMResponse:
    system, user = documentation_coding_prompt(soap_note)
    return call_llm(system, user, contains_phi=True)


# ── Diagnostic Agent ───────────────────────────────────────────────────────────

def call_diagnostic_differentials(features: dict, similar_cases: list[dict]) -> LLMResponse:
    system, user = diagnostic_differentials_prompt(features, similar_cases)
    return call_llm(system, user, contains_phi=True)


# ── Care Coordination Agent ────────────────────────────────────────────────────

def call_coordination_extraction(referral_text: str) -> LLMResponse:
    system, user = coordination_extraction_prompt(referral_text)
    return call_llm(system, user, contains_phi=True)


def call_coordination_prior_auth(referral_fields: dict, policy_snippet: str) -> LLMResponse:
    system, user = coordination_prior_auth_prompt(referral_fields, policy_snippet)
    return call_llm(system, user, contains_phi=True)


# ── Surgical Agent ─────────────────────────────────────────────────────────────

def call_surgical_annotation(detections: list[dict], procedure: str) -> LLMResponse:
    system, user = surgical_annotation_prompt(detections, procedure)
    return call_llm(system, user, contains_phi=False)


# ── Evaluation ─────────────────────────────────────────────────────────────────

def call_grounding_check(answer: str, sources: list[dict]) -> LLMResponse:
    system, user = grounding_check_prompt(answer, sources)
    return call_llm(system, user, contains_phi=False)
