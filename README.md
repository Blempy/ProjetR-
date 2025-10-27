# Automatisation MOE VRD — Outils locaux

Ce dépôt rassemble la documentation et les outils destinés à automatiser les tâches de maîtrise d'œuvre (VRD, urbanisme, infrastructures). Les notes détaillées et les plans d'action sont stockés dans `refs/`.

## Pré-requis

- Python 3.12+
- Environnement virtuel recommandé (`python3 -m venv .venv`)
- Dépendances : voir `backend/requirements.txt` et `frontend/package.json`

```bash
python3 -m venv .venv
. .venv/bin/activate  # ou source .venv/bin/activate
pip install -r backend/requirements.txt
cd frontend && npm install
```

> Si l'accès réseau est restreint, contacter l'administrateur pour autoriser l'installation des paquets nécessaires ou utiliser un miroir interne.

## Ligne de commande

Générer une fiche tâche depuis le terminal :

```bash
./scripts/create_task_sheet.py
```

Le script pose une série de questions et crée automatiquement un fichier Markdown daté dans `refs/fiches_taches/`.

## Plateforme FastAPI + React

- **Backend** : voir `backend/README.md` (FastAPI, Uvicorn, auth staff, endpoints `/api`, création fiches + points de douleur).
- **Frontend** : voir `frontend/README.md` (React + Vite, portails public et staff).
- Gestion des comptes staff : `scripts/manage_staff_users.py --password ...` (hashage bcrypt dans `config/staff_users.json`).

### Lancer l’environnement de développement

```bash
# Terminal 1 — backend
source .venv/bin/activate
uvicorn app.main:app --app-dir backend --reload

# Terminal 2 — frontend
cd frontend
npm run dev
```

Naviguer ensuite sur <http://127.0.0.1:5173>.

Routes utiles :

- `/user` : portail utilisateur (soumettre une fiche ou un point de douleur).
- `/staff/login` → `/staff/dashboard` : portail staff protégé (gestion interne).
- `/staff/task-sheets` : consultation des fiches existantes (tableau).
- Une barre de navigation fixe est accessible en haut de page pour basculer rapidement entre les espaces.

> Roadmap détaillée : `docs/migration_fastapi_react.md`. Retrait de l’ancienne app Flask : `docs/retire_flask.md`.

## Structure principale

- `refs/` : référentiel documentaire (phases, plan, todo, fiches générées, points de douleur).
- `automation/` : logique Python partagée entre la CLI et l'application web.
- `backend/` : projet FastAPI.
- `frontend/` : application React (Vite + TypeScript).
- `scripts/` : scripts utilitaires (CLI, gestion users).

## Versionnage

Chaque nouvelle fonctionnalité est commitée dans le dépôt GitHub. Utilisez :

```bash
git status
git add <fichiers>
git commit -m "Message"
git push
```

Pensez à vérifier `refs/todo.md` pour suivre les prochaines actions d'automatisation.
