"""
Single gateway for all LLM calls in the system.

Every agent and the brain imports from here:
    from providers.llm_client import call_llm

Nobody calls an LLM directly anywhere else in the codebase.
"""

import yaml
import time
import structlog
from dataclasses import dataclass
from pathlib import Path

log = structlog.get_logger()

# ── Response type ──────────────────────────────────────────────────────────────

@dataclass
class LLMResponse:
    text: str           # the model's reply
    model: str          # which model actually ran
    latency_ms: float   # how long it took
    phi_safe: bool      # was PHI-safe routing used?


# ── Config loader ──────────────────────────────────────────────────────────────

def _load_config() -> dict:
    config_path = Path(__file__).parent.parent / "config.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


# ── Provider implementations ───────────────────────────────────────────────────

def _call_mock(system: str, user: str) -> str:
    """
    Offline mock LLM — returns a deterministic extractive answer.
    Used in local PoC. No API key, no network, no cost.
    Finds the first sentence of the user prompt and echoes it back
    with a [MOCK] label so it's always obvious this isn't a real model.
    """
    first_sentence = user.split(".")[0].strip()
    return f"[MOCK LLM] Based on context: {first_sentence}. (Replace with real model in production.)"


def _call_ollama(system: str, user: str, model_name: str) -> str:
    """Calls a locally-running Ollama model. Requires `ollama serve` to be running."""
    try:
        import requests
        payload = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "stream": False,
        }
        resp = requests.post("http://localhost:11434/api/chat", json=payload, timeout=60)
        resp.raise_for_status()
        return resp.json()["message"]["content"]
    except Exception as e:
        raise RuntimeError(f"Ollama call failed: {e}") from e


def _call_openai(system: str, user: str, model_name: str) -> str:
    """Calls OpenAI API. Requires OPENAI_API_KEY env var."""
    try:
        from openai import OpenAI
        client = OpenAI()
        resp = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        return resp.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"OpenAI call failed: {e}") from e


def _call_anthropic(system: str, user: str, model_name: str) -> str:
    """Calls Anthropic API. Requires ANTHROPIC_API_KEY env var."""
    try:
        import anthropic
        client = anthropic.Anthropic()
        resp = client.messages.create(
            model=model_name,
            max_tokens=2048,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return resp.content[0].text
    except Exception as e:
        raise RuntimeError(f"Anthropic call failed: {e}") from e


# ── PHI routing logic ──────────────────────────────────────────────────────────

def _select_provider(config: dict, contains_phi: bool) -> tuple[str, str]:
    """
    Returns (provider_name, model_name) based on PHI flag.

    PHI-bearing prompts MUST use phi_safe provider — never a public LLM.
    Non-PHI prompts use the default provider.
    """
    if contains_phi:
        section = config["llm"]["phi_safe"]
    else:
        section = config["llm"]["default"]

    provider = section["provider"]
    model_name = section.get("model", "")
    return provider, model_name


# ── Main entry point ───────────────────────────────────────────────────────────

def call_llm(
    system: str,
    user: str,
    contains_phi: bool = False,
    retries: int = 3,
) -> LLMResponse:
    """
    The single entry point for every LLM call in the system.

    Args:
        system:       The system prompt (instructions to the model).
        user:         The user/human turn (the actual question or task).
        contains_phi: Set True if the prompt contains patient data.
                      This routes to the PHI-safe (private) model.
        retries:      How many times to retry on failure before giving up.

    Returns:
        LLMResponse with text, model name, latency, and phi_safe flag.

    Raises:
        RuntimeError if all retries are exhausted.
    """
    config = _load_config()
    provider, model_name = _select_provider(config, contains_phi)

    last_error = None
    for attempt in range(1, retries + 1):
        start = time.monotonic()
        try:
            log.info("llm_call_start", provider=provider, phi_safe=contains_phi, attempt=attempt)

            if provider == "mock":
                text = _call_mock(system, user)
            elif provider == "ollama":
                text = _call_ollama(system, user, model_name or "llama3")
            elif provider == "openai":
                text = _call_openai(system, user, model_name or "gpt-4o")
            elif provider == "anthropic":
                text = _call_anthropic(system, user, model_name or "claude-opus-4-8")
            else:
                raise ValueError(f"Unknown LLM provider: {provider!r}")

            latency_ms = (time.monotonic() - start) * 1000
            log.info("llm_call_done", provider=provider, latency_ms=round(latency_ms, 1))

            return LLMResponse(
                text=text,
                model=f"{provider}/{model_name}" if model_name else provider,
                latency_ms=latency_ms,
                phi_safe=contains_phi,
            )

        except Exception as e:
            last_error = e
            wait = 2 ** attempt  # exponential backoff: 2s, 4s, 8s
            log.warning("llm_call_failed", attempt=attempt, error=str(e), retry_in=wait)
            if attempt < retries:
                time.sleep(wait)

    raise RuntimeError(f"LLM call failed after {retries} attempts: {last_error}")
