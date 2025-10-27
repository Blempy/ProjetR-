# AGENTS.md — Sessions de travail avec l’assistant

Ce fichier sert à tracer les interventions de l’agent (assistant IA) sur le projet : contexte, objectifs, actions menées et suites à donner. Chaque session doit être ajoutée avec date, auteur (humain + IA) et lien vers les fichiers concernés.

## Structure recommandée

```markdown
## 2025-10-24 — Session #1
- **Participants** : Blempy (client), IA
- **Objectifs** :
  - ...
- **Actions réalisées** :
  - ...
- **Fichiers modifiés** :
  - `refs/...`
- **Todo / suivi** :
  - [ ] ...
```

## Sessions

### 2025-10-24 — Session #1
- **Participants** : Blempy, IA
- **Objectifs** :
  - Mettre en place le référentiel `refs/` et transférer le PDF de référence.
  - Extraire le contenu du PDF et préparer un plan d’automatisation.
  - Structurer une todo et un gabarit de fiche tâche.
- **Actions réalisées** :
  - Déplacement du PDF dans `refs/`.
  - Création de `refs/README.md`, `plan_developpement.md`, `todo.md`.
  - Extraction du PDF en Markdown (`refs/phases_taches.md`, `Phases_MOE_VRD.md`).
  - Création du modèle de fiche (`refs/modele_fiche_tache.md`).
  - Installation de PyPDF2 via environnement virtuel.
  - Ajout du processus de collecte des points de douleur (`refs/process_points_douleur.md`).
- **Fichiers modifiés** :
  - `refs/Phases_MOE_VRD_reformate.pdf`
  - `refs/Phases_MOE_VRD_reformate.txt`
  - `refs/README.md`
  - `refs/plan_developpement.md`
  - `refs/todo.md`
  - `refs/phases_taches.md`
  - `refs/modele_fiche_tache.md`
  - `refs/process_points_douleur.md`
- **Todo / suivi** :
  - [x] Mettre en place un assistant CLI pour les fiches.
  - [x] Documenter le référentiel.
  - [ ] Collecter les points de douleur par phase.
  - [ ] Recenser les scripts métiers existants.

### 2025-10-24 — Session #2
- **Participants** : Blempy, IA
- **Objectifs** :
  - Automatiser la création de fiches via un formulaire web.
  - Ajouter un formulaire pour les points de douleur.
  - Documenter l’usage et la configuration.
- **Actions réalisées** :
  - Création du package `automation/` (logique mutualisée).
  - Mise à jour du script CLI pour réutiliser la logique partagée.
  - Développement de l’application Flask (`app.py`, `templates/`, `static/`).
  - Ajout de `requirements.txt`, `README.md`.
  - Mise à jour des documents `refs/`.
  - Commit local `Add local web UI for task and pain logs`.
- **Fichiers modifiés / créés** :
  - `app.py`
  - `automation/*`
  - `scripts/create_task_sheet.py`
  - `templates/*`
  - `static/style.css`
  - `requirements.txt`
  - `README.md`
  - `refs/*.md`
- **Todo / suivi** :
  - [ ] Tester l’application web avec des entrées réelles.
  - [ ] Éventuellement exposer l’application à un collègue (via tunnel ou réseau local).
  - [ ] Continuer le recensement des pains points et scripts métiers.

### 2025-10-27 — Session #3
- **Participants** : Blempy, IA
- **Objectifs** :
  - Préparer la migration vers FastAPI + React avec authentification multi-comptes.
  - Développer un squelette backend (API) et frontend (portails public/staff).
  - Permettre la création de fiches tâches via l’API et l’interface staff.
- **Actions réalisées** :
  - Création des projets `backend/` (FastAPI) et `frontend/` (React + Vite + TypeScript).
  - Mise en place de l’authentification staff (JWT, gestion des mots de passe hashés, script `scripts/manage_staff_users.py`).
  - Ajout des endpoints `/api/auth/login`, `/api/staff/profile`, `/api/staff/task-sheets`, `/api/staff/pain-points`.
  - Implémentation du contexte d’authentification React, pages `StaffDashboard`, `StaffTaskSheetForm`, `StaffPainPointForm`, formulaire de connexion.
  - Génération réussie d’une fiche via l’API (`refs/fiches_taches/2025-10-27-test-api-fiche.md`).
  - Saisie possible des points de douleur via l’interface staff (enregistrement Markdown dans `refs/points_douleur/`).
  - Documentation mise à jour (`docs/migration_fastapi_react.md`, `README.md`, `backend/README.md`, `frontend/README.md`).
- **Fichiers modifiés / créés** :
  - `backend/app/*`, `backend/requirements.txt`
  - `frontend/*` (React app, styles, configs)
  - `config/staff_users.json`, `scripts/manage_staff_users.py`
  - `refs/todo.md`, `docs/migration_fastapi_react.md`, `README.md`
  - `refs/fiches_taches/2025-10-27-test-api-fiche.md`
- **Todo / suivi** :
  - [ ] Planifier le retrait progressif de l’appli Flask.
  - [ ] Définir la stratégie de tests (unitaires + end-to-end) pour la nouvelle stack.
