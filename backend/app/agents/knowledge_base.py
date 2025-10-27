from __future__ import annotations

import array
import hashlib
import json
import math
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional

from .embeddings import get_embedding

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DB_PATH = ROOT / "data" / "agents_memory.db"


def _ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def _to_blob(values: list[float]) -> bytes:
    arr = array.array("f", values)
    return arr.tobytes()


def _from_blob(blob: bytes) -> list[float]:
    arr = array.array("f")
    arr.frombytes(blob)
    return list(arr)


def _cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


@dataclass
class KBEntry:
    id: int
    question: str
    answer: str
    metadata: dict[str, Any]
    similarity: float
    usage_count: int


class KnowledgeBase:
    def __init__(
        self,
        db_path: Path | None = None,
        similarity_threshold: float = 0.85,
        max_age_days: int = 365,
    ) -> None:
        self.db_path = db_path or DEFAULT_DB_PATH
        _ensure_parent(self.db_path)
        self.similarity_threshold = similarity_threshold
        self.max_age_days = max_age_days
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS responses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    key_hash TEXT NOT NULL,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    metadata TEXT NOT NULL,
                    embedding BLOB NOT NULL,
                    created_at TEXT NOT NULL,
                    usage_count INTEGER NOT NULL DEFAULT 0
                )
                """
            )
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_responses_key ON responses(key_hash)"
            )
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_responses_created ON responses(created_at)"
            )

    def _normalize_question(self, question: str) -> str:
        return " ".join(question.strip().lower().split())

    def _make_key(self, question: str, metadata: dict[str, Any]) -> str:
        phase = (metadata.get("phase") or "").lower()
        project = (metadata.get("project") or "").lower()
        normalized = self._normalize_question(question)
        raw = f"{phase}|{project}|{normalized}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def lookup(
        self,
        question: str,
        metadata: dict[str, Any] | None = None,
    ) -> Optional[KBEntry]:
        metadata = metadata or {}
        question = question or ""
        if not question.strip():
            return None

        try:
            query_embedding = get_embedding(question)
        except Exception:
            return None

        cutoff_date = (
            datetime.utcnow() - timedelta(days=self.max_age_days)
        ).isoformat()

        best_entry: Optional[KBEntry] = None

        with self._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM responses WHERE created_at >= ?",
                (cutoff_date,),
            ).fetchall()

        for row in rows:
            embedding = _from_blob(row["embedding"])
            similarity = _cosine_similarity(query_embedding, embedding)
            if similarity >= self.similarity_threshold:
                entry = KBEntry(
                    id=row["id"],
                    question=row["question"],
                    answer=row["answer"],
                    metadata=json.loads(row["metadata"]),
                    similarity=similarity,
                    usage_count=row["usage_count"],
                )
                if not best_entry or similarity > best_entry.similarity:
                    best_entry = entry

        if best_entry:
            self._increment_usage(best_entry.id, 2 if best_entry.similarity >= 0.95 else 1)
        return best_entry

    def _increment_usage(self, entry_id: int, increment: int) -> None:
        with self._connect() as conn:
            conn.execute(
                "UPDATE responses SET usage_count = usage_count + ? WHERE id = ?",
                (increment, entry_id),
            )

    def store(
        self,
        question: str,
        answer: str,
        metadata: dict[str, Any] | None = None,
    ) -> Optional[int]:
        metadata = metadata or {}
        question = question or ""
        answer = answer or ""
        if not question.strip() or not answer.strip():
            return None

        key_hash = self._make_key(question, metadata)

        try:
            embedding = get_embedding(question)
        except Exception:
            return None

        payload = json.dumps(metadata, ensure_ascii=False)

        with self._connect() as conn:
            existing = conn.execute(
                "SELECT id FROM responses WHERE key_hash = ? LIMIT 1",
                (key_hash,),
            ).fetchone()
            if existing:
                return existing["id"]

            conn.execute(
                """
                INSERT INTO responses (key_hash, question, answer, metadata, embedding, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    key_hash,
                    question,
                    answer,
                    payload,
                    _to_blob(embedding),
                    datetime.utcnow().isoformat(),
                ),
            )
            entry_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
            return entry_id
