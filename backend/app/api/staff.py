from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re

from fastapi import APIRouter, Depends, HTTPException, Query

from ..auth.deps import get_staff_user
from ..auth.models import StaffUser
from .schemas import (
    UserProfile,
    TaskSheetCreate,
    TaskSheetDetail,
    TaskSheetResponse,
    TaskSheetUpdate,
    PainPointCreate,
    PainPointResponse,
    TaskSheetListItem,
)
from automation.task_sheet import (
    TaskSheetData,
    create_task_sheet,
    FICHE_DIR,
    load_task_sheet,
    update_task_sheet,
)
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


def _clean_str(value: str | None) -> str:
    return value.strip() if isinstance(value, str) else ""


def _clean_list(values: list[str] | None) -> list[str]:
    if not values:
        return []
    return [item.strip() for item in values if isinstance(item, str) and item.strip()]


def _build_task_sheet_data(payload: TaskSheetCreate) -> TaskSheetData:
    return TaskSheetData(
        phase=_clean_str(payload.phase) or "",
        task_name=_clean_str(payload.task_name) or "Fiche tâche",
        responsable=_clean_str(payload.responsable),
        frequency=_clean_str(payload.frequency),
        duration=_clean_str(payload.duration),
        objective=_clean_str(payload.objective),
        trigger=_clean_str(payload.trigger),
        steps=_clean_list(payload.steps),
        data_needed=_clean_list(payload.data_needed),
        docs_needed=_clean_list(payload.docs_needed),
        tools_needed=_clean_list(payload.tools_needed),
        outputs=_clean_list(payload.outputs),
        formats=_clean_list(payload.formats),
        recipients=_clean_list(payload.recipients),
        pains=_clean_list(payload.pains),
        automation_ideas=_clean_list(payload.automation_ideas),
        automation_type=_clean_str(payload.automation_type) or "À qualifier",
        automation_prereq=_clean_str(payload.automation_prereq) or "À qualifier",
        automation_effort=_clean_str(payload.automation_effort) or "À qualifier",
        automation_benefits=_clean_list(payload.automation_benefits),
        priority=_clean_str(payload.priority) or "À qualifier",
        status=_clean_str(payload.status) or "À lancer",
        next_action=_clean_str(payload.next_action) or "À définir",
        linked_docs=_clean_list(payload.linked_docs),
    )


def _as_relative(path: Path) -> Path:
    try:
        return path.relative_to(Path.cwd())
    except ValueError:
        return path


def _resolve_task_sheet_path(raw_path: str) -> Path:
    fiche_root = FICHE_DIR.resolve()
    candidate = Path(raw_path)

    if not candidate.is_absolute():
        candidate = (Path.cwd() / candidate).resolve()
    else:
        candidate = candidate.resolve()

    if not str(candidate).startswith(str(fiche_root)):
        candidate = (fiche_root / Path(raw_path)).resolve()

    if not str(candidate).startswith(str(fiche_root)):
        raise HTTPException(status_code=400, detail="Chemin de fiche invalide.")
    if not candidate.exists():
        raise HTTPException(status_code=404, detail="Fiche tâche introuvable.")

    return candidate


@router.get("/profile", response_model=UserProfile, summary="Informations utilisateur connecté")
async def get_profile(user: StaffUser = Depends(get_staff_user)) -> UserProfile:
    return UserProfile(username=user.username, roles=user.roles)


@router.post("/task-sheets", response_model=TaskSheetResponse, summary="Créer une fiche tâche")
async def create_task_sheet_endpoint(
    payload: TaskSheetCreate,
    user: StaffUser = Depends(get_staff_user),
) -> TaskSheetResponse:
    data = _build_task_sheet_data(payload)

    filepath = create_task_sheet(data)

    relative_path = _as_relative(filepath)

    return TaskSheetResponse(path=str(relative_path), task_name=data.task_name, phase=data.phase)


@router.get(
    "/task-sheets/detail",
    response_model=TaskSheetDetail,
    summary="Consulter le détail d'une fiche tâche",
)
async def get_task_sheet_detail(
    path: str = Query(..., description="Chemin relatif vers la fiche tâche"),
    user: StaffUser = Depends(get_staff_user),
) -> TaskSheetDetail:
    file_path = _resolve_task_sheet_path(path)
    data = load_task_sheet(file_path)
    relative_path = _as_relative(file_path)

    return TaskSheetDetail(
        path=str(relative_path),
        last_updated=data.timestamp.strftime("%Y-%m-%d"),
        phase=data.phase,
        task_name=data.task_name,
        responsable=data.responsable,
        frequency=data.frequency,
        duration=data.duration,
        objective=data.objective,
        trigger=data.trigger,
        steps=data.steps,
        data_needed=data.data_needed,
        docs_needed=data.docs_needed,
        tools_needed=data.tools_needed,
        outputs=data.outputs,
        formats=data.formats,
        recipients=data.recipients,
        pains=data.pains,
        automation_ideas=data.automation_ideas,
        automation_type=data.automation_type,
        automation_prereq=data.automation_prereq,
        automation_effort=data.automation_effort,
        automation_benefits=data.automation_benefits,
        priority=data.priority,
        status=data.status,
        next_action=data.next_action,
        linked_docs=data.linked_docs,
    )


@router.put(
    "/task-sheets",
    response_model=TaskSheetResponse,
    summary="Mettre à jour une fiche tâche",
)
async def update_task_sheet_endpoint(
    payload: TaskSheetUpdate,
    user: StaffUser = Depends(get_staff_user),
) -> TaskSheetResponse:
    file_path = _resolve_task_sheet_path(payload.path)
    data = _build_task_sheet_data(payload)
    update_task_sheet(file_path, data)
    relative_path = _as_relative(file_path)

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
