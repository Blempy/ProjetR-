# -*- coding: utf-8 -*-
"""Application web locale pour gérer les fiches tâches et points de douleur."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from flask import Flask, flash, redirect, render_template, request, url_for

from automation.pain_points import PainPointEntry, record_pain_point
from automation.task_sheet import TaskSheetData, create_task_sheet

APP = Flask(__name__)
APP.config["SECRET_KEY"] = "dev-secret-change-me"

PROJECT_ROOT = Path(__file__).resolve().parent
PHASE_CHOICES = [
    "Études préliminaires",
    "Avant-projet (AVP)",
    "Projet (PRO)",
    "Assistance à la passation des contrats (ACT)",
    "Direction de l'exécution / VISA (DET/VISA)",
    "Assistance aux opérations de réception (AOR)",
]


def _split_lines(value: str | None) -> list[str]:
    if not value:
        return []
    return [line.strip() for line in value.replace("\r\n", "\n").split("\n") if line.strip()]


def _clamp_score(value: str | None, default: int = 1) -> int:
    try:
        number = int(value) if value is not None else default
    except ValueError:
        return default
    return max(1, min(5, number))


def _relative_path(path: Path) -> str:
    try:
        return str(path.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def _render_errors(errors: Iterable[str], template: str, **context):
    for error in errors:
        flash(error, "error")
    return render_template(template, **context)


@APP.get("/")
def home():
    return render_template("home.html", phase_options=PHASE_CHOICES)


@APP.route("/task/new", methods=["GET", "POST"])
def task_form():
    if request.method == "POST":
        form = request.form
        phase = form.get("phase", "").strip()
        task_name = form.get("task_name", "").strip()
        responsable = form.get("responsable", "").strip()
        frequency = form.get("frequency", "").strip()
        duration = form.get("duration", "").strip() or "À préciser"
        objective = form.get("objective", "").strip()
        trigger = form.get("trigger", "").strip() or "À préciser"

        errors = []
        if not phase:
            errors.append("Merci de préciser la phase du projet.")
        if not task_name:
            errors.append("Merci de renseigner l'intitulé de la tâche.")
        if not objective:
            errors.append("Merci de préciser l'objectif principal de la tâche.")

        if errors:
            return _render_errors(errors, "task_form.html", form=form, phase_options=PHASE_CHOICES)

        data = TaskSheetData(
            phase=phase,
            task_name=task_name,
            responsable=responsable,
            frequency=frequency,
            duration=duration,
            objective=objective,
            trigger=trigger,
            steps=_split_lines(form.get("steps")),
            data_needed=_split_lines(form.get("data_needed")),
            docs_needed=_split_lines(form.get("docs_needed")),
            tools_needed=_split_lines(form.get("tools_needed")),
            outputs=_split_lines(form.get("outputs")),
            formats=_split_lines(form.get("formats")),
            recipients=_split_lines(form.get("recipients")),
            pains=_split_lines(form.get("pains")),
            automation_ideas=_split_lines(form.get("automation_ideas")),
            automation_type=form.get("automation_type", "À qualifier").strip() or "À qualifier",
            automation_prereq=form.get("automation_prereq", "À qualifier").strip() or "À qualifier",
            automation_effort=form.get("automation_effort", "À qualifier").strip() or "À qualifier",
            automation_benefits=_split_lines(form.get("automation_benefits")),
            priority=form.get("priority", "À qualifier").strip() or "À qualifier",
            status=form.get("status", "À lancer").strip() or "À lancer",
            next_action=form.get("next_action", "À définir").strip() or "À définir",
            linked_docs=_split_lines(form.get("linked_docs")),
        )

        filepath = create_task_sheet(data)
        return render_template(
            "success.html",
            kind="Fiche tâche",
            path=_relative_path(filepath),
            back_url=url_for("task_form"),
            home_url=url_for("home"),
        )

    return render_template("task_form.html", form=None, phase_options=PHASE_CHOICES)


@APP.route("/pain-point/new", methods=["GET", "POST"])
def pain_form():
    if request.method == "POST":
        form = request.form
        phase = form.get("phase", "").strip()
        task = form.get("task", "").strip()
        description = form.get("description", "").strip()
        automation_idea = form.get("automation_idea", "").strip()
        comments = form.get("comments", "").strip()

        errors = []
        if not phase:
            errors.append("Merci de préciser la phase concernée.")
        if not task:
            errors.append("Merci d'indiquer la tâche ciblée.")
        if not description:
            errors.append("Merci de décrire le point de douleur.")

        if errors:
            return _render_errors(errors, "pain_form.html", form=form, phase_options=PHASE_CHOICES)

        entry = PainPointEntry(
            phase=phase,
            task=task,
            description=description,
            frequency=_clamp_score(form.get("frequency"), default=1),
            duration=_clamp_score(form.get("duration"), default=1),
            impact=_clamp_score(form.get("impact"), default=1),
            stress=_clamp_score(form.get("stress"), default=1),
            automation_idea=automation_idea,
            comments=comments,
        )

        filepath = record_pain_point(entry)
        return render_template(
            "success.html",
            kind="Point de douleur",
            path=_relative_path(filepath),
            back_url=url_for("pain_form"),
            home_url=url_for("home"),
        )

    return render_template("pain_form.html", form=None, phase_options=PHASE_CHOICES)


def main():
    APP.run(debug=True, host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()
