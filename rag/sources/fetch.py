"""Polite, cached downloads into data/raw. Re-runs reuse files already on disk."""
from __future__ import annotations

import logging
import time
from collections.abc import Callable
from pathlib import Path

import httpx

log = logging.getLogger(__name__)
USER_AGENT = "krishna-guide-rag/0.1 (personal research script; low volume)"


def fetch(
    url: str,
    dest: Path,
    params: dict | None = None,
    valid: Callable[[bytes], bool] = lambda b: len(b) > 0,
    delay: float = 5.0,
    retries: int = 4,
) -> Path:
    """Download url to dest unless it already exists. Retries with backoff on 429/5xx or invalid bodies."""
    if dest.exists() and dest.stat().st_size > 0:
        log.debug("cached %s", dest)
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(1, retries + 1):
        r = httpx.get(url, params=params, headers={"User-Agent": USER_AGENT}, timeout=60, follow_redirects=True)
        # Wikimedia returns its rate-limit notice as a 200 text body, so validate content too.
        if r.status_code == 200 and valid(r.content):
            dest.write_bytes(r.content)
            log.info("downloaded %s -> %s (%d bytes)", r.url, dest, len(r.content))
            time.sleep(delay)
            return dest
        wait = 30 * attempt
        log.warning("fetch %s failed (status %s, attempt %d); retrying in %ds", url, r.status_code, attempt, wait)
        time.sleep(wait)
    raise RuntimeError(f"could not download {url} after {retries} attempts")
