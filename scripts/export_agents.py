#!/usr/bin/env python3
"""Exporter les briefs agents Markdown vers un JSON exploitable par l'orchestrateur."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = ROOT / "docs" / "agents"
OUTPUT_PATH = ROOT / "docs" / "agents_registry.json"


PHASE_RE = re.compile(r"- \*\*Phase\*\* :\s*(.+)")
PRIORITY_RE = re.compile(r"- \*\*Priorité\*\* :\s*(.+)")
STATUS_RE = re.compile(r"- \*\*Statut\*\* :\s*(.+)")
RESP_RE = re.compile(r"- \*\*Responsable initial\*\* :\s*(.+)")
FREQ_RE = re.compile(r"- \*\*Fréquence\*\* :\s*(.+)")
DURATION_RE = re.compile(r"- \*\*Durée estimée\*\* :\s*(.+)")


@dataclass
class AgentBrief:
    slug: str
    title: str
    phase: str
    priority: str
    status: str
    responsable: str
    frequency: str
    duration: str
    source: str
    body: str


def _extract(pattern: re.Pattern[str], text: str, default: str = "") -> str:
    match = pattern.search(text)
    return match.group(1).strip() if match else default


def parse_agent_markdown(path: Path) -> AgentBrief:
    text = path.read_text(encoding="utf-8")
    title_match = re.search(r"#\s*Agent\s*(.+)", text)
    title = title_match.group(1).strip() if title_match else path.stem.replace("-", " ").title()
    slug = path.stem

    phase = _extract(PHASE_RE, text)
    priority = _extract(PRIORITY_RE, text)
    status = _extract(STATUS_RE, text)
    responsable = _extract(RESP_RE, text)
    frequency = _extract(FREQ_RE, text)
    duration = _extract(DURATION_RE, text)

    source_match = re.search(r"- \*\*Fiche source\*\* :\s*`([^`]+)`", text)
    source = source_match.group(1).strip() if source_match else ""

    return AgentBrief(
        slug=slug,
        title=title,
        phase=phase,
        priority=priority,
        status=status,
        responsable=responsable,
        frequency=frequency,
        duration=duration,
        source=source,
        body=text,
    )


def export_agents() -> list[dict[str, Any]]:
    briefs: list[dict[str, Any]] = []
    for path in sorted(AGENTS_DIR.glob("*.md")):
        briefs.append(asdict(parse_agent_markdown(path)))
    return briefs


def main() -> None:
    if not AGENTS_DIR.exists():
        raise SystemExit(f"Répertoire introuvable : {AGENTS_DIR}")
    data = export_agents()
    OUTPUT_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(data)} agents exportés → {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
