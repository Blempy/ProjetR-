# -*- coding: utf-8 -*-
"""Helpers to log pain points per phase."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from .utils import slugify

ROOT = Path(__file__).resolve().parent.parent
REFS_DIR = ROOT / "refs"
PAIN_DIR = REFS_DIR / "points_douleur"

TABLE_HEADER = (
    "| Date | Tâche | Description | Fréquence | Durée | Impact | Stress | Idée d'automatisation | Commentaires |\n"
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
)


def _escape_cell(value: str) -> str:
    """Ensure Markdown table safety by replacing pipes."""
    return value.replace("|", r"\|").strip() or "—"


@dataclass
class PainPointEntry:
    phase: str
    task: str
    description: str
    frequency: int
    duration: int
    impact: int
    stress: int
    automation_idea: str = ""
    comments: str = ""
    timestamp: datetime = field(default_factory=datetime.now)

    def as_markdown_row(self) -> str:
        date_str = self.timestamp.strftime("%Y-%m-%d")
        cols = [
            date_str,
            self.task,
            self.description,
            str(self.frequency),
            str(self.duration),
            str(self.impact),
            str(self.stress),
            self.automation_idea,
            self.comments,
        ]
        return "| " + " | ".join(_escape_cell(col) for col in cols) + " |"


def record_pain_point(entry: PainPointEntry) -> Path:
    """Append a pain point to the phase-specific Markdown log."""
    PAIN_DIR.mkdir(parents=True, exist_ok=True)
    phase_slug = slugify(entry.phase, fallback="phase")
    filepath = PAIN_DIR / f"{phase_slug}.md"

    if not filepath.exists():
        header = f"# Points de douleur — {entry.phase}\n\n{TABLE_HEADER}"
        filepath.write_text(header, encoding="utf-8")

    with filepath.open("a", encoding="utf-8") as fh:
        fh.write(entry.as_markdown_row() + "\n")

    return filepath
