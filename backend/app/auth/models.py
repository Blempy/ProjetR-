from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
import json

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@dataclass
class StaffUser:
    username: str
    password_hash: str
    roles: list[str]

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash)


def load_staff_users(path: Path) -> dict[str, StaffUser]:
    if not path.exists():
        return {}
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    users: dict[str, StaffUser] = {}
    for item in data.get("users", []):
        user = StaffUser(
            username=item["username"],
            password_hash=item["password_hash"],
            roles=item.get("roles", []),
        )
        users[user.username] = user
    return users
