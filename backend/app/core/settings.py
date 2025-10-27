from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration."""

    project_name: str = "MOE VRD Automatisation API"
    api_prefix: str = "/api"
    secret_key: str = "change-me"
    staff_users_file: Path = Path("config/staff_users.json")
    allow_origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
