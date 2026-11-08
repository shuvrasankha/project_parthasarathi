"""Ingestion CLI: `python -m rag.ingest gita|mb|situations`."""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

from rag.config import settings
from rag.db import Row, connect, upsert_chunks
from rag.embed import get_embedder

log = logging.getLogger("ingest")


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    log.info("wrote %d records -> %s", len(records), path)


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def ingest_gita() -> int:
    from rag.sources import gita

    raw, clean = settings.data_dir / "raw", settings.data_dir / "clean" / "gita_verses.jsonl"
    gita.download(raw)
    report = gita.build(raw)
    print(report.render())
    if not report.ok:
        log.error("Gita validation failed; nothing written.")
        return 1

    # Keep hand-written fields if the clean file already has them (you edit meaning_simple/themes there).
    previous = {r["id"]: r for r in read_jsonl(clean)}
    records = []
    for v in report.records:
        d = v.to_dict()
        old = previous.get(d["id"], {})
        d["meaning_simple"] = old.get("meaning_simple") or d["meaning_simple"]
        d["themes"] = old.get("themes") or d["themes"]
        records.append(d)
    write_jsonl(clean, records)

    rows = [Row(id=d["id"], content=gita.embed_text(d), meta=d) for d in records]
    with connect() as conn:
        upsert_chunks(conn, "gita_verses", rows, get_embedder())
    return 0


def ingest_mb(batch_size: int = 256) -> int:
    from rag.chunking import bge_token_counter
    from rag.sources import ganguli

    raw, clean = settings.data_dir / "raw", settings.data_dir / "clean" / "mb_passages.jsonl"
    ganguli.download(raw)
    report = ganguli.build(raw, bge_token_counter())
    print(report.render())
    if not report.ok:
        log.error("Mahabharata validation failed; nothing written.")
        return 1
    write_jsonl(clean, report.chunks)

    rows = [Row(id=c["id"], content=c["text"], meta={k: v for k, v in c.items() if k != "text"}) for c in report.chunks]
    embedder = get_embedder()
    written = skipped = 0
    with connect() as conn:
        for i in range(0, len(rows), batch_size):  # commit per batch so an interrupted run keeps its progress
            stats = upsert_chunks(conn, "mb_passages", rows[i : i + batch_size], embedder)
            written, skipped = written + stats.written, skipped + stats.skipped
            log.info("mb_passages progress: %d/%d", min(i + batch_size, len(rows)), len(rows))
    log.info("mb_passages total: read=%d written=%d skipped=%d", len(rows), written, skipped)
    return 0


def ingest_situations() -> int:
    from rag import situations as sit

    entries, verses, sections = sit.load_yaml(), sit.load_verses(), sit.load_sections()
    print(sit.report(entries, set(verses), set(sections)))
    if not entries or sit.validate(entries, set(verses), set(sections)):
        log.error("situations validation failed (or %s is empty); nothing written.", sit.YAML_PATH)
        return 1
    rows = [Row(id=e["id"], content=sit.embed_text(e), meta=e) for e in entries]
    with connect() as conn:
        ids = [r.id for r in rows]  # drop rows for entries removed from the YAML
        gone = conn.execute("delete from chunks where collection = 'situations' and id <> all(%s)", (ids,)).rowcount
        if gone:
            log.info("situations: deleted %d rows no longer in the YAML", gone)
        upsert_chunks(conn, "situations", rows, get_embedder())
    return 0


COMMANDS = {"gita": ingest_gita, "mb": ingest_mb, "situations": ingest_situations}


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    for noisy in ("httpx", "httpx2", "httpcore", "urllib3", "huggingface_hub", "sentence_transformers"):
        logging.getLogger(noisy).setLevel(logging.WARNING)
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("collection", choices=sorted(COMMANDS))
    sys.exit(COMMANDS[p.parse_args().collection]())


if __name__ == "__main__":
    main()
