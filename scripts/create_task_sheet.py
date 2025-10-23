#!/usr/bin/env python3
"""Assistant de création de fiche tâche pour le référentiel MOE VRD.

Ce script pose des questions à l'utilisateur et génère automatiquement
un fichier Markdown conforme au modèle `refs/modele_fiche_tache.md`.
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from textwrap import indent

ROOT = Path(__file__).resolve().parent.parent
REFS_DIR = ROOT / "refs"
FICHE_DIR = REFS_DIR / "fiches_taches"
TEMPLATE_NAME = "modele_fiche_tache.md"


def prompt_line(question: str, required: bool = True, default: str | None = None) -> str:
    """Demande une réponse courte (une ligne)."""
    while True:
        suffix = f" (défaut : {default})" if default else ""
        answer = input(f"{question}{suffix}\n> ").strip()
        if not answer and default is not None:
            return default
        if answer or not required:
            return answer
        print("⚠️  Réponse obligatoire, merci de renseigner une valeur.")


def prompt_multiline(question: str) -> list[str]:
    """Collecte un bloc multi-ligne ; ligne vide pour terminer."""
    print(f"{question} (ligne vide pour terminer)")
    lines: list[str] = []
    while True:
        line = input("> ").rstrip()
        if not line:
            break
        lines.append(line)
    return lines


def bullet_block(items: list[str]) -> str:
    """Formate une liste en bloc Markdown à puces."""
    if not items:
        return "- Aucun point précisé pour l'instant."
    return "\n".join(f"- {item.strip()}" for item in items if item.strip()) or "- Aucun point précisé pour l'instant."


def numbered_block(items: list[str]) -> str:
    """Formate une liste en bloc Markdown numéroté."""
    if not items:
        return "1. À détailler."
    return "\n".join(f"{idx}. {item.strip()}" for idx, item in enumerate(items, start=1) if item.strip()) or "1. À détailler."


def slugify(value: str) -> str:
    """Transforme un libellé en slug utilisable dans un nom de fichier."""
    value = value.lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.ASCII)
    value = re.sub(r"[-\s]+", "-", value, flags=re.ASCII).strip("-")
    return value or "fiche-tache"


def ensure_directories() -> None:
    """Crée les répertoires nécessaires."""
    FICHE_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    ensure_directories()

    print("=== Création d'une nouvelle fiche tâche ===\n")

    phase = prompt_line("Phase MOE (ex : AVP, PRO, DET/VISA)")
    task_name = prompt_line("Intitulé de la tâche")
    responsable = prompt_line("Responsable principal / intervenants clés")
    frequency = prompt_line("Fréquence (ex : chaque projet, hebdomadaire, ponctuel)")
    duration = prompt_line("Durée estimée (sans automatisation)", required=False, default="À préciser")

    objective = prompt_line("Objectif principal de la tâche")
    trigger = prompt_line("Déclencheur (événement qui lance la tâche)", required=False, default="À préciser")
    steps = prompt_multiline("Étapes principales (une ligne = une étape)")

    data_needed = prompt_multiline("Entrées — données nécessaires")
    docs_needed = prompt_multiline("Entrées — documents de référence")
    tools_needed = prompt_multiline("Logiciels / outils mobilisés")

    outputs = prompt_multiline("Sorties — livrables produits")
    formats = prompt_multiline("Formats associés")
    recipients = prompt_multiline("Destinataires / diffusion")

    pains = prompt_multiline("Points de douleur actuels (temps, erreurs, coordination...)")

    print("\nPistes d'automatisation :")
    automation_raw = prompt_multiline("Idées (une ligne par idée)")
    automation_type = prompt_line(
        "Type principal envisagé (ex : macro Excel, script AutoCAD, modèle Word, checklist)", required=False, default="À qualifier"
    )
    automation_prereq = prompt_line("Pré-requis identifiés", required=False, default="À qualifier")
    automation_effort = prompt_line("Niveau d'effort estimé (faible / moyen / élevé)", required=False, default="À qualifier")
    automation_benefits = prompt_multiline("Bénéfices attendus")

    priority = prompt_line("Priorité (haute / moyenne / basse)", required=False, default="À qualifier")
    status = prompt_line("Statut actuel (à lancer / en cours / en test / déployé)", required=False, default="À lancer")
    next_action = prompt_line("Prochaine action à engager", required=False, default="À définir")
    linked_docs = prompt_multiline("Documents liés (chemins dans `refs/` ou externes)")

    timestamp = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(task_name)
    filename = FICHE_DIR / f"{timestamp}-{slug}.md"

    content = f"""# Fiche tâche — {task_name}

> Phase : **{phase}** · Dernière mise à jour : {timestamp}

## Informations générales

- **Phase MOE** : {phase}
- **Intitulé de la tâche** : {task_name}
- **Responsable / intervenants** : {responsable}
- **Fréquence** : {frequency}
- **Durée estimée** : {duration}

## Description

- **Objectif** : {objective}
- **Déclencheur** : {trigger}
- **Étapes principales** :
{indent(numbered_block(steps), '  ')}

## Entrées / ressources nécessaires

- **Données** :
{indent(bullet_block(data_needed), '  ')}
- **Documents de référence** :
{indent(bullet_block(docs_needed), '  ')}
- **Logiciels / outils** :
{indent(bullet_block(tools_needed), '  ')}

## Sorties attendues

- **Livrables** :
{indent(bullet_block(outputs), '  ')}
- **Formats** :
{indent(bullet_block(formats), '  ')}
- **Destinataires / diffusion** :
{indent(bullet_block(recipients), '  ')}

## Points de douleur actuels

{bullet_block(pains)}

## Pistes d'automatisation

- **Idées / solutions** :
{indent(bullet_block(automation_raw), '  ')}
- **Type** : {automation_type}
- **Pré-requis** : {automation_prereq}
- **Niveau d'effort** : {automation_effort}
- **Bénéfices attendus** :
{indent(bullet_block(automation_benefits), '  ')}

## État et priorisation

- **Priorité** : {priority}
- **Statut** : {status}
- **Prochaine action** : {next_action}
- **Documents liés** :
{indent(bullet_block(linked_docs), '  ')}
"""

    filename.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"\n✅ Fiche créée : {filename.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
