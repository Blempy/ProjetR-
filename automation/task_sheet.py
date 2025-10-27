# -*- coding: utf-8 -*-
"""Logic to generate task sheet Markdown files."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import re
from textwrap import indent

from .utils import slugify
ROOT = Path(__file__).resolve().parent.parent
REFS_DIR = ROOT / "refs"
FICHE_DIR = REFS_DIR / "fiches_taches"
PLACEHOLDER = "Aucun point précisé pour l'instant."


def _bullet_block(items: list[str]) -> str:
    if not items:
        return "- Aucun point précisé pour l'instant."
    cleaned = [item.strip() for item in items if item.strip()]
    return "\n".join(f"- {item}" for item in cleaned) or "- Aucun point précisé pour l'instant."


def _numbered_block(items: list[str]) -> str:
    if not items:
        return "1. À détailler."
    cleaned = [item.strip() for item in items if item.strip()]
    return "\n".join(f"{idx}. {item}" for idx, item in enumerate(cleaned, start=1)) or "1. À détailler."


_SECTION_PATTERN = re.compile(r"## (.+?)\n\n(.*?)(?=\n## |\Z)", re.S)


def _extract_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    for match in _SECTION_PATTERN.finditer(text):
        sections[match.group(1).strip()] = match.group(2)
    return sections


def _extract_field(section_text: str, label: str) -> str:
    pattern = re.compile(rf"- \*\*{re.escape(label)}\*\*\s*:\s*(.*)")
    match = pattern.search(section_text)
    if match:
        return match.group(1).strip()
    return ""


def _extract_block(section_text: str, label: str) -> str:
    pattern = re.compile(
        rf"- \*\*{re.escape(label)}\*\*\s*:\s*(?:\n)?(.*?)(?=\n- \*\*|\Z)",
        re.S,
    )
    match = pattern.search(section_text)
    if match:
        return match.group(1).strip()
    return ""


def _parse_bullet_block_text(block_text: str) -> list[str]:
    if not block_text:
        return []
    items: list[str] = []
    for raw in block_text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("- "):
            line = line[2:].strip()
        if not line or PLACEHOLDER in line:
            continue
        items.append(line)
    return items


def _parse_numbered_text(block_text: str) -> list[str]:
    if not block_text:
        return []
    items: list[str] = []
    for raw in block_text.splitlines():
        match = re.match(r"\s*\d+\.\s*(.*)", raw)
        if not match:
            continue
        value = match.group(1).strip()
        if not value:
            continue
        if value.casefold().startswith("à détailler"):
            continue
        items.append(value)
    return items


@dataclass
class TaskSheetData:
    phase: str
    task_name: str
    responsable: str
    frequency: str
    duration: str
    objective: str
    trigger: str
    steps: list[str] = field(default_factory=list)
    data_needed: list[str] = field(default_factory=list)
    docs_needed: list[str] = field(default_factory=list)
    tools_needed: list[str] = field(default_factory=list)
    outputs: list[str] = field(default_factory=list)
    formats: list[str] = field(default_factory=list)
    recipients: list[str] = field(default_factory=list)
    pains: list[str] = field(default_factory=list)
    automation_ideas: list[str] = field(default_factory=list)
    automation_type: str = "À qualifier"
    automation_prereq: str = "À qualifier"
    automation_effort: str = "À qualifier"
    automation_benefits: list[str] = field(default_factory=list)
    priority: str = "À qualifier"
    status: str = "À lancer"
    next_action: str = "À définir"
    linked_docs: list[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)

    def to_markdown(self) -> str:
        ts = self.timestamp.strftime("%Y-%m-%d")
        numbered_steps = indent(_numbered_block(self.steps), "  ")
        data_block = indent(_bullet_block(self.data_needed), "  ")
        docs_block = indent(_bullet_block(self.docs_needed), "  ")
        tools_block = indent(_bullet_block(self.tools_needed), "  ")
        outputs_block = indent(_bullet_block(self.outputs), "  ")
        formats_block = indent(_bullet_block(self.formats), "  ")
        recipients_block = indent(_bullet_block(self.recipients), "  ")
        pains_block = _bullet_block(self.pains)
        ideas_block = indent(_bullet_block(self.automation_ideas), "  ")
        benefits_block = indent(_bullet_block(self.automation_benefits), "  ")
        linked_block = indent(_bullet_block(self.linked_docs), "  ")

        return f"""# Fiche tâche — {self.task_name}

> Phase : **{self.phase}** · Dernière mise à jour : {ts}

## Informations générales

- **Phase MOE** : {self.phase}
- **Intitulé de la tâche** : {self.task_name}
- **Responsable / intervenants** : {self.responsable}
- **Fréquence** : {self.frequency}
- **Durée estimée** : {self.duration}

## Description

- **Objectif** : {self.objective}
- **Déclencheur** : {self.trigger}
- **Étapes principales** :
{numbered_steps}

## Entrées / ressources nécessaires

- **Données** :
{data_block}
- **Documents de référence** :
{docs_block}
- **Logiciels / outils** :
{tools_block}

## Sorties attendues

- **Livrables** :
{outputs_block}
- **Formats** :
{formats_block}
- **Destinataires / diffusion** :
{recipients_block}

## Points de douleur actuels

{pains_block}

## Pistes d'automatisation

- **Idées / solutions** :
{ideas_block}
- **Type** : {self.automation_type}
- **Pré-requis** : {self.automation_prereq}
- **Niveau d'effort** : {self.automation_effort}
- **Bénéfices attendus** :
{benefits_block}

## État et priorisation

- **Priorité** : {self.priority}
- **Statut** : {self.status}
- **Prochaine action** : {self.next_action}
- **Documents liés** :
{linked_block}
""".strip()


def create_task_sheet(data: TaskSheetData) -> Path:
    """Generate the Markdown content and save it under refs/fiches_taches."""
    FICHE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = data.timestamp.strftime("%Y-%m-%d")
    slug = slugify(data.task_name, fallback="fiche-tache")
    filepath = FICHE_DIR / f"{timestamp}-{slug}.md"
    filepath.write_text(data.to_markdown() + "\n", encoding="utf-8")
    return filepath


def load_task_sheet(path: Path) -> TaskSheetData:
    """Read a Markdown fiche tâche and convert it back into TaskSheetData."""
    text = path.read_text(encoding="utf-8")
    sections = _extract_sections(text)

    title_match = re.search(r"#\s*Fiche tâche\s*—\s*(.+)", text)
    task_name = title_match.group(1).strip() if title_match else path.stem

    meta_match = re.search(
        r">?\s*Phase\s*:\s*\*\*(.+?)\*\*\s*·\s*Dernière mise à jour\s*:\s*(\d{4}-\d{2}-\d{2})",
        text,
    )
    header_phase = ""
    timestamp = datetime.fromtimestamp(path.stat().st_mtime)
    if meta_match:
        header_phase = meta_match.group(1).strip()
        try:
            timestamp = datetime.strptime(meta_match.group(2), "%Y-%m-%d")
        except ValueError:
            pass

    general = sections.get("Informations générales", "")
    phase = _extract_field(general, "Phase MOE") or header_phase
    responsable = _extract_field(general, "Responsable / intervenants") or ""
    frequency = _extract_field(general, "Fréquence") or ""
    duration = _extract_field(general, "Durée estimée") or ""

    description = sections.get("Description", "")
    objective = _extract_field(description, "Objectif") or ""
    trigger = _extract_field(description, "Déclencheur") or ""
    steps_block = _extract_block(description, "Étapes principales")
    steps = _parse_numbered_text(steps_block)

    inputs = sections.get("Entrées / ressources nécessaires", "")
    data_needed = _parse_bullet_block_text(_extract_block(inputs, "Données"))
    docs_needed = _parse_bullet_block_text(_extract_block(inputs, "Documents de référence"))
    tools_needed = _parse_bullet_block_text(_extract_block(inputs, "Logiciels / outils"))

    outputs_section = sections.get("Sorties attendues", "")
    outputs = _parse_bullet_block_text(_extract_block(outputs_section, "Livrables"))
    formats = _parse_bullet_block_text(_extract_block(outputs_section, "Formats"))
    recipients = _parse_bullet_block_text(_extract_block(outputs_section, "Destinataires / diffusion"))

    pains_section = sections.get("Points de douleur actuels", "")
    pains = _parse_bullet_block_text(pains_section)

    automation_section = sections.get("Pistes d'automatisation", "")
    automation_ideas = _parse_bullet_block_text(_extract_block(automation_section, "Idées / solutions"))
    automation_type = _extract_field(automation_section, "Type") or "À qualifier"
    automation_prereq = _extract_field(automation_section, "Pré-requis") or "À qualifier"
    automation_effort = _extract_field(automation_section, "Niveau d'effort") or "À qualifier"
    automation_benefits = _parse_bullet_block_text(_extract_block(automation_section, "Bénéfices attendus"))

    status_section = sections.get("État et priorisation", "")
    priority = _extract_field(status_section, "Priorité") or "À qualifier"
    status = _extract_field(status_section, "Statut") or "À lancer"
    next_action = _extract_field(status_section, "Prochaine action") or "À définir"
    linked_docs = _parse_bullet_block_text(_extract_block(status_section, "Documents liés"))

    return TaskSheetData(
        phase=phase or header_phase or "",
        task_name=task_name,
        responsable=responsable,
        frequency=frequency,
        duration=duration,
        objective=objective,
        trigger=trigger,
        steps=steps,
        data_needed=data_needed,
        docs_needed=docs_needed,
        tools_needed=tools_needed,
        outputs=outputs,
        formats=formats,
        recipients=recipients,
        pains=pains,
        automation_ideas=automation_ideas,
        automation_type=automation_type,
        automation_prereq=automation_prereq,
        automation_effort=automation_effort,
        automation_benefits=automation_benefits,
        priority=priority,
        status=status,
        next_action=next_action,
        linked_docs=linked_docs,
        timestamp=timestamp,
    )


def update_task_sheet(path: Path, data: TaskSheetData) -> Path:
    """Overwrite an existing fiche tâche with new content."""
    data.timestamp = datetime.now()
    path.write_text(data.to_markdown() + "\n", encoding="utf-8")
    return path
