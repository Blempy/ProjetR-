from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, Depends

from ..auth.deps import get_staff_user
from ..auth.models import StaffUser
from .schemas import UserProfile, TaskSheetCreate, TaskSheetResponse
from automation.task_sheet import TaskSheetData, create_task_sheet

router = APIRouter(prefix="/staff", tags=["staff"])


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
