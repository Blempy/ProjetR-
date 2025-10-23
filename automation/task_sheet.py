# -*- coding: utf-8 -*-
"""Logic to generate task sheet Markdown files."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from textwrap import indent

from .utils import slugify
ROOT = Path(__file__).resolve().parent.parent
REFS_DIR = ROOT / "refs"
FICHE_DIR = REFS_DIR / "fiches_taches"


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
