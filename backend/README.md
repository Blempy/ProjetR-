# Backend FastAPI — MOE VRD Automatisation

## Installation

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

## Lancement (développement)

```
uvicorn app.main:app --reload --app-dir backend
```

L’API expose notamment :
- `GET /api/health`
- `POST /api/auth/login` (auth staff)
- `GET /api/staff/profile` (protégé)

## Gestion des comptes staff

```
./scripts/manage_staff_users.py add --username toine --password monmotdepasse
./scripts/manage_staff_users.py list
```

Les mots de passe sont stockés hashés dans `config/staff_users.json`.
