"""One chat-completion call behind a config switch (LLM_PROVIDER = anthropic | groq | openrouter | nvidia,
or a comma-separated chain such as "groq,openrouter" tried in order)."""
from __future__ import annotations

import json
import logging
import re
import time

import httpx

from rag.config import settings

log = logging.getLogger(__name__)


def _anthropic(system: str, user: str, max_tokens: int, temperature: float) -> str:
    if not settings.anthropic_api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is empty in .env (or set LLM_PROVIDER=nvidia)")
    r = httpx.post(
        "https://api.anthropic.com/v1/messages",
        headers={"x-api-key": settings.anthropic_api_key, "anthropic-version": "2023-06-01"},
        json={"model": settings.rewrite_model, "max_tokens": max_tokens, "temperature": temperature,
              "system": system, "messages": [{"role": "user", "content": user}]},
        timeout=180,
    )
    r.raise_for_status()
    return "".join(b.get("text", "") for b in r.json()["content"])


def _openai_compat(url: str, key: str, body: dict, system: str, user: str, max_tokens: int, temperature: float) -> str:
    r = httpx.post(
        f"{url}/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={**body, "max_tokens": max_tokens, "temperature": temperature,
              "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]},
        timeout=300,
    )
    r.raise_for_status()
    content = r.json()["choices"][0]["message"].get("content")
    if not content:
        raise RuntimeError("model returned no content (raise max_tokens?)")
    return content


def _nvidia(system: str, user: str, max_tokens: int, temperature: float) -> str:
    if not settings.nvidia_api_key:
        raise RuntimeError("NVIDIA_API_KEY is empty in .env")
    return _openai_compat(settings.nvidia_base_url, settings.nvidia_api_key, {"model": settings.nvidia_model},
                          system, user, max_tokens, temperature)


def _groq(system: str, user: str, max_tokens: int, temperature: float) -> str:
    if not settings.groq_api_key:
        raise RuntimeError("GROQ_API_KEY is empty in .env")
    err: Exception | None = None
    for model in [m.strip() for m in settings.groq_models.split(",") if m.strip()]:
        try:  # Groq has no server-side fallback list, so try models here (rate limits are per model)
            return _openai_compat("https://api.groq.com/openai/v1", settings.groq_api_key, {"model": model},
                                  system, user, max_tokens, temperature)
        except (httpx.HTTPError, RuntimeError) as e:
            log.warning("groq %s failed (%s)", model, e)
            err = e
    raise RuntimeError(f"all Groq models failed: {err}")


def free_models(spec: str) -> list[str]:
    """Parse OPENROUTER_MODELS; refuse anything that is not a free model so nothing is ever billed."""
    models = [m.strip() for m in spec.split(",") if m.strip()]
    if not models or any(not m.endswith(":free") for m in models):
        raise ValueError(f"OPENROUTER_MODELS must list only ':free' models, got {models}")
    return models


def _openrouter(system: str, user: str, max_tokens: int, temperature: float) -> str:
    if not settings.openrouter_api_key:
        raise RuntimeError("OPENROUTER_API_KEY is empty in .env")
    return _openai_compat("https://openrouter.ai/api/v1", settings.openrouter_api_key,
                          {"models": free_models(settings.openrouter_models)},  # OpenRouter falls back in order
                          system, user, max_tokens, temperature)


PROVIDERS = {"anthropic": _anthropic, "groq": _groq, "openrouter": _openrouter, "nvidia": _nvidia}


def chat(system: str, user: str, max_tokens: int = 2000, temperature: float = 0.0, retries: int = 3) -> str:
    """Try each provider in LLM_PROVIDER in order; retry the whole chain with backoff."""
    chain = [PROVIDERS[p.strip()] for p in settings.llm_provider.split(",") if p.strip()]
    for attempt in range(1, retries + 1):
        for call in chain:
            try:
                return call(system, user, max_tokens, temperature)
            except (httpx.HTTPError, RuntimeError) as e:
                log.warning("LLM %s failed (%s)", call.__name__.lstrip("_"), e)
        if attempt < retries:
            log.warning("all LLM providers failed, retry %d/%d", attempt, retries - 1)
            time.sleep(10 * attempt)
    raise RuntimeError(f"all LLM providers failed: {settings.llm_provider}")


def parse_json(text: str):
    """First JSON object/array in a reply; tolerates <think> blocks and ``` fences."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S)
    start = min((i for i in (text.find("{"), text.find("[")) if i >= 0), default=-1)
    if start < 0:
        raise ValueError(f"no JSON in reply: {text[:200]!r}")
    return json.JSONDecoder().raw_decode(text[start:])[0]


def chat_json(system: str, user: str, max_tokens: int = 2000, temperature: float = 0.0, retries: int = 3):
    """chat() + parse_json(); re-asks on malformed or truncated JSON (seen on NVIDIA endpoints)."""
    for attempt in range(1, retries + 1):
        reply = chat(system, user, max_tokens, temperature)
        try:
            return parse_json(reply)
        except ValueError as e:  # JSONDecodeError is a ValueError
            if attempt == retries:
                raise
            log.warning("unparseable JSON reply (%s, %d chars), retry %d/%d", e, len(reply), attempt, retries - 1)
    raise AssertionError("unreachable")
