from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(tags=["public"])


@router.get("/health", summary="Health check")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/version", summary="API version")
async def get_version() -> dict[str, str]:
    return {"version": "0.1.0"}
