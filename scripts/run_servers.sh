#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}" )/.." && pwd)"

if [[ ! -d "${ROOT_DIR}/.venv" ]]; then
  echo "[ERREUR] L'environnement virtuel .venv est introuvable dans ${ROOT_DIR}" >&2
  exit 1
fi

cleanup() {
  if [[ -n "${BACKEND_PID:-}" ]]; then
    echo "\n[INFO] Arrêt du backend (PID ${BACKEND_PID})…"
    kill "${BACKEND_PID}" >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

source "${ROOT_DIR}/.venv/bin/activate"

echo "[INFO] Démarrage du backend FastAPI…"
uvicorn app.main:app --app-dir backend --reload &
BACKEND_PID=$!

echo "[INFO] Backend lancé (PID ${BACKEND_PID}). Lancement du frontend Vite…"
cd "${ROOT_DIR}/frontend"
npm run dev
