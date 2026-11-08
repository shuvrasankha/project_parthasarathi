"""Settings read from .env / environment. Nothing here is hard-coded per machine."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")


def _bool(name: str, default: str = "false") -> bool:
    return os.getenv(name, default).strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    database_url: str = os.getenv("DATABASE_URL", "postgresql://krishna:krishna@localhost:5432/krishna")
    embed_provider: str = os.getenv("EMBED_PROVIDER", "bge-m3")
    embed_model: str = os.getenv("EMBED_MODEL", "BAAI/bge-m3")
    embed_device: str = os.getenv("EMBED_DEVICE", "mps")
    embed_batch_size: int = int(os.getenv("EMBED_BATCH_SIZE", "8"))
    embed_dim: int = 1024  # fixed by the vector(1024) column
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    rewrite_model: str = os.getenv("REWRITE_MODEL", "claude-haiku-5-5")
    llm_provider: str = os.getenv("LLM_PROVIDER", "anthropic")  # one provider, or a comma-separated fallback chain: anthropic | groq | openrouter | nvidia
    nvidia_api_key: str = os.getenv("NVIDIA_API_KEY", "")
    nvidia_model: str = os.getenv("NVIDIA_MODEL", "nvidia/nemotron-3-ultra-550b-a55b")
    nvidia_base_url: str = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
    groq_api_key: str = os.getenv("GROQ_API_KEY", "")
    groq_models: str = os.getenv("GROQ_MODELS", "openai/gpt-oss-120b,qwen/qwen3.8-27b")  # tried in order
    openrouter_api_key: str = os.getenv("OPENROUTER_API_KEY", "")
    # comma-separated, tried in order by OpenRouter; every one must end in ":free"
    openrouter_models: str = os.getenv(
        "OPENROUTER_MODELS", "google/gemma-4-31b-it:free,nvidia/nemotron-3-ultra-550b-a55b:free,google/gemma-4-26b-a4b-it:free")
    rerank_enabled: bool = _bool("RERANK_ENABLED")
    linked_first: bool = _bool("LINKED_FIRST")  # verses/passages linked from situations rank above direct hits
    fts_text: str = os.getenv("FTS_TEXT", "all")  # full-text query words: all (rewrite + themes) | themes
    rerank_model: str = os.getenv("RERANK_MODEL", "BAAI/bge-reranker-v2-m3")
    data_dir: Path = ROOT / os.getenv("DATA_DIR", "data")


settings = Settings()
