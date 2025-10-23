#!/usr/bin/env python3
"""Assistant de création de fiche tâche pour le référentiel MOE VRD.

Ce script pose des questions à l'utilisateur et génère automatiquement
un fichier Markdown conforme au modèle `refs/modele_fiche_tache.md`.
"""

from __future__ import annotations

from pathlib import Path

from automation.task_sheet import TaskSheetData, create_task_sheet


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


def ensure_directories() -> None:
    """Crée les répertoires nécessaires."""
    (Path(__file__).resolve().parent.parent / "refs" / "fiches_taches").mkdir(parents=True, exist_ok=True)


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

    data = TaskSheetData(
        phase=phase,
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
        automation_ideas=automation_raw,
        automation_type=automation_type,
        automation_prereq=automation_prereq,
        automation_effort=automation_effort,
        automation_benefits=automation_benefits,
        priority=priority,
        status=status,
        next_action=next_action,
        linked_docs=linked_docs,
    )

    filepath = create_task_sheet(data)
    print(f"\n✅ Fiche créée : {filepath.relative_to(Path(__file__).resolve().parent.parent)}")


if __name__ == "__main__":
    main()
