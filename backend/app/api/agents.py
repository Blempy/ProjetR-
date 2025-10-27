from __future__ import annotations

from fastapi import APIRouter, Depends

from ..auth.deps import get_staff_user
from ..auth.models import StaffUser
from ..agents import Orchestrator
from .schemas import AgentRouteRequest, AgentRouteResponse

router = APIRouter(prefix="/agents", tags=["agents"])
orchestrator = Orchestrator()


@router.post("/route", response_model=AgentRouteResponse, summary="Router une requête vers le bon agent")
async def route_agent(
    payload: AgentRouteRequest,
    user: StaffUser = Depends(get_staff_user),
) -> AgentRouteResponse:
    result = orchestrator.route(
        session_id=payload.session_id,
        caller=payload.caller,
        message=payload.message.dict(),
        context=payload.context,
    )
    return AgentRouteResponse(**result)
