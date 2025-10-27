# Automatisation MOE VRD — Outils locaux

Ce dépôt rassemble la documentation et les outils destinés à automatiser les tâches de maîtrise d'œuvre (VRD, urbanisme, infrastructures). Les notes détaillées et les plans d'action sont stockés dans `refs/`.

## Pré-requis

- Python 3.12+
- Environnement virtuel recommandé (`python3 -m venv .venv`)
- Dépendances : voir `requirements.txt`

```bash
python3 -m venv .venv
. .venv/bin/activate  # ou source .venv/bin/activate
pip install -r requirements.txt
```

> Si l'accès réseau est restreint, contacter l'administrateur pour autoriser l'installation des paquets nécessaires ou utiliser un miroir interne.

## Ligne de commande

Générer une fiche tâche depuis le terminal :

```bash
./scripts/create_task_sheet.py
```

Le script pose une série de questions et crée automatiquement un fichier Markdown daté dans `refs/fiches_taches/`.

## Application web locale

Une interface web est disponible pour saisir les fiches tâches et les points de douleur sans passer par la ligne de commande (version Flask historique en attendant la migration FastAPI + React).

```bash
python3 app.py
```

Ouvrez ensuite <http://127.0.0.1:5000> dans votre navigateur. Deux formulaires sont proposés :

- **Nouvelle fiche tâche** : génère un fichier Markdown dans `refs/fiches_taches/`.
- **Point de douleur** : ajoute une entrée dans `refs/points_douleur/<phase>.md`.

> Note : l’interface est actuellement unique. Une séparation « utilisateur final » / « espace privé (fiches tâches) » est planifiée dans `refs/todo.md`.

### Migration FastAPI + React

- **Backend** : voir `backend/README.md` (FastAPI, Uvicorn, auth staff, endpoints `/api`, création fiches + points de douleur).
- **Frontend** : voir `frontend/README.md` (React + Vite, context d'authentification, formulaires staff pour fiches et points de douleur).
- Gestion des comptes staff : `scripts/manage_staff_users.py --password ...` (hashage bcrypt dans `config/staff_users.json`).

> La roadmap détaillée est disponible dans `docs/migration_fastapi_react.md`.

## Structure principale

- `refs/` : référentiel documentaire (phases, plan, todo, fiches générées, points de douleur).
- `automation/` : logique Python partagée entre la CLI et l'application web (Flask).
- `backend/` : projet FastAPI (en cours de construction).
- `frontend/` : application React (squelette Vite).
- `scripts/` : scripts utilitaires (CLI, gestion users).
- `templates/`, `static/` : ressources de l'application Flask.

## Versionnage

Chaque nouvelle fonctionnalité est commitée dans le dépôt GitHub. Utilisez :

```bash
git status
git add <fichiers>
git commit -m "Message"
git push
```

Pensez à vérifier `refs/todo.md` pour suivre les prochaines actions d'automatisation.
