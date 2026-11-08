"""Postgres access and the idempotent upsert used by every ingestion step."""
from __future__ import annotations

import hashlib
import logging
from dataclasses import dataclass, field

import psycopg
from pgvector.psycopg import register_vector
from psycopg.types.json import Jsonb

from rag.config import settings
from rag.embed import Embedder

log = logging.getLogger(__name__)


def connect() -> psycopg.Connection:
    conn = psycopg.connect(settings.database_url)
    register_vector(conn)
    return conn


def content_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


@dataclass
class Row:
    id: str
    content: str
    meta: dict = field(default_factory=dict)


@dataclass
class UpsertStats:
    read: int = 0
    written: int = 0
    skipped: int = 0


def upsert_chunks(conn: psycopg.Connection, collection: str, rows: list[Row], embedder: Embedder) -> UpsertStats:
    """Insert or update rows; re-embed only rows whose content hash changed."""
    stats = UpsertStats(read=len(rows))
    existing = dict(
        conn.execute(
            "select id, meta->>'content_hash' from chunks where id = any(%s)", ([r.id for r in rows],)
        ).fetchall()
    )
    todo = [r for r in rows if existing.get(r.id) != content_hash(r.content)]
    stats.skipped = len(rows) - len(todo)
    if todo:
        vecs = embedder.embed([r.content for r in todo])
        with conn.cursor() as cur:
            cur.executemany(
                """insert into chunks (id, collection, content, meta, embedding)
                   values (%s, %s, %s, %s, %s::vector)
                   on conflict (id) do update set collection = excluded.collection,
                     content = excluded.content, meta = excluded.meta, embedding = excluded.embedding""",
                [
                    (r.id, collection, r.content, Jsonb({**r.meta, "content_hash": content_hash(r.content)}), v)
                    for r, v in zip(todo, vecs)
                ],
            )
        conn.commit()
    # unchanged text keeps its embedding, but meta (sections, verses, reviewed) can still change
    same = [r for r in rows if existing.get(r.id) == content_hash(r.content)]
    if same:
        with conn.cursor() as cur:
            cur.executemany(
                "update chunks set meta = %s where id = %s and meta is distinct from %s",
                [(m, r.id, m) for r in same for m in [Jsonb({**r.meta, "content_hash": content_hash(r.content)})]],
            )
        conn.commit()
    stats.written = len(todo)
    log.info("%s: read=%d written=%d skipped=%d", collection, stats.read, stats.written, stats.skipped)
    return stats
