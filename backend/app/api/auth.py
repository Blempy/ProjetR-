from __future__ import annotations

from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ..auth.models import load_staff_users
from ..auth.tokens import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from ..core.settings import get_settings
from .schemas import TokenResponse

router = APIRouter(tags=["auth"])


@router.post("/auth/login", response_model=TokenResponse, summary="Authentification staff")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> TokenResponse:
    settings = get_settings()
    users = load_staff_users(settings.staff_users_file)
    user = users.get(form_data.username)
    if not user or not user.verify_password(form_data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Identifiants invalides")
    access_token = create_access_token({"sub": user.username}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return TokenResponse(access_token=access_token, token_type="bearer")
