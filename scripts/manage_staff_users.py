#!/usr/bin/env python3
"""Gestion des comptes staff pour l'API FastAPI."""

from __future__ import annotations

import argparse
import json
from getpass import getpass
from pathlib import Path
from typing import Any

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

DEFAULT_CONFIG = Path("config/staff_users.json")


def load_config(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"users": []}
    return json.loads(path.read_text(encoding="utf-8"))


def save_config(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def add_user(path: Path, username: str, roles: list[str], password: str | None = None) -> None:
    data = load_config(path)
    for user in data["users"]:
        if user["username"] == username:
            raise SystemExit(f"Utilisateur {username} déjà existant")
    if password is None:
        password = getpass("Mot de passe : ")
        confirm = getpass("Confirmer : ")
        if password != confirm:
            raise SystemExit("Les mots de passe ne correspondent pas")
    elif password == "":
        raise SystemExit("Mot de passe vide interdit")
    password_hash = pwd_context.hash(password)
    data["users"].append({"username": username, "password_hash": password_hash, "roles": roles})
    save_config(path, data)
    print(f"Utilisateur {username} ajouté.")


def remove_user(path: Path, username: str) -> None:
    data = load_config(path)
    users = [user for user in data["users"] if user["username"] != username]
    if len(users) == len(data["users"]):
        raise SystemExit(f"Utilisateur {username} introuvable")
    data["users"] = users
    save_config(path, data)
    print(f"Utilisateur {username} supprimé.")


def list_users(path: Path) -> None:
    data = load_config(path)
    if not data["users"]:
        print("Aucun utilisateur enregistré.")
        return
    for user in data["users"]:
        roles = ", ".join(user.get("roles", [])) or "aucun"
        print(f"- {user['username']} (roles: {roles})")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gestion des comptes staff")
    parser.add_argument("action", choices=["add", "remove", "list"], help="Action à réaliser")
    parser.add_argument("--username", help="Identifiant utilisateur")
    parser.add_argument("--roles", nargs="*", default=["staff"], help="Liste des rôles")
    parser.add_argument("--password", help="Mot de passe (évite la saisie interactive)")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="Chemin du fichier JSON")
    args = parser.parse_args()

    path = Path(args.config)

    if args.action in {"add", "remove"} and not args.username:
        parser.error("--username est obligatoire pour cette action")

    if args.action == "add":
        add_user(path, args.username, args.roles, args.password)
    elif args.action == "remove":
        remove_user(path, args.username)
    elif args.action == "list":
        list_users(path)


if __name__ == "__main__":
    main()
