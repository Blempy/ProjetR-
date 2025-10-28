from __future__ import annotations

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from ..ep import EPCalculator, EPInput
from ..ep.exporter import generate_excel


router = APIRouter(prefix="/ep", tags=["ep"])


@router.post("/calc", summary="Calculer une note EP", response_class=JSONResponse)
async def calculate_ep(payload: EPInput):
    try:
        result = EPCalculator(payload).run()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    try:
        excel_path = generate_excel(result)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    payload_response = result.dict()
    payload_response["excel_path"] = str(excel_path)

    return JSONResponse(content=payload_response)
