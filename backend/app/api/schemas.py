from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class UserProfile(BaseModel):
    username: str
    roles: list[str]


class TaskSheetCreate(BaseModel):
    phase: str
    task_name: str
    responsable: str | None = ""
    frequency: str | None = ""
    duration: str | None = ""
    objective: str
    trigger: str | None = ""
    steps: list[str] = []
    data_needed: list[str] = []
    docs_needed: list[str] = []
    tools_needed: list[str] = []
    outputs: list[str] = []
    formats: list[str] = []
    recipients: list[str] = []
    pains: list[str] = []
    automation_ideas: list[str] = []
    automation_type: str | None = "À qualifier"
    automation_prereq: str | None = "À qualifier"
    automation_effort: str | None = "À qualifier"
    automation_benefits: list[str] = []
    priority: str | None = "À qualifier"
    status: str | None = "À lancer"
    next_action: str | None = "À définir"
    linked_docs: list[str] = []


class TaskSheetResponse(BaseModel):
    path: str
    task_name: str
    phase: str


class PainPointCreate(BaseModel):
    phase: str
    task: str
    description: str
    frequency: int
    duration: int
    impact: int
    stress: int
    automation_idea: str | None = ""
    comments: str | None = ""


class PainPointResponse(BaseModel):
    path: str
    phase: str
    task: str


class TaskSheetListItem(BaseModel):
    task_name: str
    phase: str
    path: str
    updated_at: Optional[str] = None
