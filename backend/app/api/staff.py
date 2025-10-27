from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re

from fastapi import APIRouter, Depends

from ..auth.deps import get_staff_user
from ..auth.models import StaffUser
from .schemas import (
    UserProfile,
    TaskSheetCreate,
    TaskSheetResponse,
    PainPointCreate,
    PainPointResponse,
    TaskSheetListItem,
)
from automation.task_sheet import TaskSheetData, create_task_sheet, FICHE_DIR
from automation.pain_points import PainPointEntry, record_pain_point

router = APIRouter(prefix="/staff", tags=["staff"])


def _extract_summary(path: Path) -> TaskSheetListItem:
    title = ""
    phase = ""
    updated_at: str | None = None

    title_pattern = re.compile(r"#\s*Fiche tâche\s*—\s*(.+)")
    phase_pattern = re.compile(r">\s*Phase\s*:\s*\*\*(.+?)\*\*")
    updated_pattern = re.compile(r"Dernière mise à jour\s*:\s*(\d{4}-\d{2}-\d{2})")

    try:
        with path.open("r", encoding="utf-8") as fh:
            for line in fh:
                if not title:
                    match = title_pattern.match(line)
                    if match:
                        title = match.group(1).strip()
                        continue
                if not phase:
                    match = phase_pattern.search(line)
                    if match:
                        phase = match.group(1).strip()
                if updated_at is None:
                    match = updated_pattern.search(line)
                    if match:
                        updated_at = match.group(1)
                if title and phase and updated_at:
                    break
    except OSError:
        pass

    if not title:
        title = path.stem
    if not updated_at:
        updated_at = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d")

    try:
        rel_path = path.relative_to(Path.cwd())
    except ValueError:
        rel_path = path

    return TaskSheetListItem(
        task_name=title,
        phase=phase,
        path=str(rel_path),
        updated_at=updated_at,
    )


@router.get("/profile", response_model=UserProfile, summary="Informations utilisateur connecté")
async def get_profile(user: StaffUser = Depends(get_staff_user)) -> UserProfile:
    return UserProfile(username=user.username, roles=user.roles)


@router.post("/task-sheets", response_model=TaskSheetResponse, summary="Créer une fiche tâche")
async def create_task_sheet_endpoint(
    payload: TaskSheetCreate,
    user: StaffUser = Depends(get_staff_user),
) -> TaskSheetResponse:
    data = TaskSheetData(
        phase=payload.phase,
        task_name=payload.task_name,
        responsable=payload.responsable or "",
        frequency=payload.frequency or "",
        duration=payload.duration or "",
        objective=payload.objective,
        trigger=payload.trigger or "",
        steps=payload.steps,
        data_needed=payload.data_needed,
        docs_needed=payload.docs_needed,
        tools_needed=payload.tools_needed,
        outputs=payload.outputs,
        formats=payload.formats,
        recipients=payload.recipients,
        pains=payload.pains,
        automation_ideas=payload.automation_ideas,
        automation_type=payload.automation_type or "À qualifier",
        automation_prereq=payload.automation_prereq or "À qualifier",
        automation_effort=payload.automation_effort or "À qualifier",
        automation_benefits=payload.automation_benefits,
        priority=payload.priority or "À qualifier",
        status=payload.status or "À lancer",
        next_action=payload.next_action or "À définir",
        linked_docs=payload.linked_docs,
    )

    filepath = create_task_sheet(data)

    try:
        relative_path = filepath.relative_to(Path.cwd())
    except ValueError:
        relative_path = filepath

    return TaskSheetResponse(path=str(relative_path), task_name=data.task_name, phase=data.phase)


@router.post("/pain-points", response_model=PainPointResponse, summary="Consigner un point de douleur")
async def create_pain_point_endpoint(
    payload: PainPointCreate,
    user: StaffUser = Depends(get_staff_user),
) -> PainPointResponse:
    entry = PainPointEntry(
        phase=payload.phase,
        task=payload.task,
        description=payload.description,
        frequency=payload.frequency,
        duration=payload.duration,
        impact=payload.impact,
        stress=payload.stress,
        automation_idea=payload.automation_idea or "",
        comments=payload.comments or "",
    )

    filepath = record_pain_point(entry)

    try:
        relative_path = filepath.relative_to(Path.cwd())
    except ValueError:
        relative_path = filepath

    return PainPointResponse(path=str(relative_path), phase=entry.phase, task=entry.task)


@router.get("/task-sheets", response_model=list[TaskSheetListItem], summary="Lister les fiches tâches")
async def list_task_sheets(user: StaffUser = Depends(get_staff_user)) -> list[TaskSheetListItem]:
    if not FICHE_DIR.exists():
        return []
    summaries: list[TaskSheetListItem] = []
    for file_path in sorted(FICHE_DIR.glob("*.md")):
        summaries.append(_extract_summary(file_path))
    return summaries
