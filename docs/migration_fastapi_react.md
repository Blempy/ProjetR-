# Migration vers FastAPI + React

> Objectif : faire évoluer l'application actuelle (Flask + templates) vers une architecture front/back moderne, scalable et adaptée à la séparation « utilisateur final » / « staff ».

## 1. Périmètre actuel à migrer

- Génération de fiches tâches (Markdown) — aujourd'hui via CLI et formulaire Flask.
- Saisie des points de douleur (tableaux Markdown).
- Documentation stockée dans `refs/`.
- Roadmap : futur assistant de notes de calcul EP (forms + génération Excel/PDF).

## 2. Architecture cible

### Backend (FastAPI)

- Projet Python structuré (`app/` ou `src/`) avec :
  - `routers/public.py` : endpoints accessibles sans authentification (soumission de formulaires, simulation, export public).
  - `routers/staff.py` : endpoints protégés (CRUD fiches tâches, configuration).
  - `models/` : objets Pydantic pour valider entrées/sorties.
  - `services/` : logique métier (génération Markdown, interactions fichiers `refs/`, génération Excel).
  - `auth/` : gestion des utilisateurs (hash + JWT ou cookies signés).
- Serveur ASGI (Uvicorn) pour le développement, Gunicorn/Uvicorn pour la prod.
- Tests automatisés (pytest) pour les routes et la logique métier.

### Frontend (React)

- Application React (Vite ou Create React App) avec deux zones :
  - **User Portal** : formulaires d'automatisation (notes de calcul, points de douleur) → consomme les endpoints publics.
  - **Staff Portal** : interface privée (gestion des fiches, suivi backlog) → nécessite login/mot de passe.
- Routage (React Router) + gestion d'état légère (React Query ou Redux Toolkit si besoin).
- Appels API avec `fetch`/`axios`, gestion du token staff (stockage sécurisé).
- Components réutilisables (tableaux, formulaires dynamiques, notifications).

## 3. Authentification et sécurité

- Stockage des utilisateurs staff dans un fichier sécurisé (`config/staff_users.yaml`) ou base légère.
- Hashage des mots de passe côté serveur (bcrypt via `passlib` ou `werkzeug.security`).
- API d'auth `POST /auth/login` → renvoie un JWT signé (durée configurée).
- Middleware FastAPI pour protéger les routes staff (`Depends(get_current_staff)`).
- Sur le front staff : stocker le token en mémoire ou cookie HTTPOnly.
- CSRF & CORS à configurer (FastAPI + React).

## 4. Plan de migration

### Étape 1 — Préparation

1. Lister les fonctionnalités existantes et leurs dépendances (fait dans ce document).
2. Décider de la structure des répertoires (`backend/`, `frontend/`).
3. Choisir les outils :
   - FastAPI, Uvicorn, Pydantic, SQLModel (optionnel), passlib.
   - React + TypeScript (recommandé), Vite, Tailwind/Chakra (optionnel), axios, React Query.

### Étape 2 — Mise en place du squelette

1. Créer le projet FastAPI (`backend/`) :
   - Initialisation Pyproject/requirements.
   - Endpoints de test (`/health`, `/version`).
2. Créer le projet React (`frontend/`) :
   - Page d'accueil + route `/login`.
   - Configuration du proxy (développement) pour pointer vers l'API.

### Étape 3 — Authentification staff

1. Implémenter `/auth/login` côté FastAPI (vérification utilisateurs).
2. Protéger les routes staff avec un `Depends`.
3. Implémenter le formulaire de login React + gestion du token.
4. Ajouter un décorateur côté front pour restreindre l'accès au portail staff.

### Étape 4 — Portage fonctionnel

1. **Fiches tâches** :
   - Endpoint POST pour créer une fiche (génère Markdown).
   - Endpoint GET pour lister/consulter.
2. **Points de douleur** :
   - Même logique, création + lecture.
3. **Notes de calcul EP** (quand prêtes) :
   - Endpoint pour lancer le calcul/génération.
   - Front staff : interface de pilotage + suivi.
4. Vérifier la compatibilité avec l'existant (`refs/` reste la source de vérité).

### Étape 5 — Interfaces finales

- **User Portal** : formulaires simplifiés (notes, pain points) + page de confirmation.
- **Staff Portal** : dashboard (todo, fiches, scripts), accès aux exports.
- Composants partagés (tableaux, formulaires dynamiques).

### Étape 6 — Décommission de Flask

- Après validation, retirer progressivement les templates Flask.
- Garder la CLI (`scripts/create_task_sheet.py`) mais la faire appeler l'API (optionnel).

## 5. Prochaines actions

- [x] Valider la structure des dossiers (`backend/`, `frontend/`).
- [x] Créer une checklist d'installation (FastAPI env, Node.js).
- [x] Mettre à jour `refs/todo.md` avec les tâches détaillées.
- [x] Préparer un script d'ajout d'utilisateurs staff (hashage).
- [ ] Définir un plan de tests (unitaires + end-to-end).
- [x] Migrer la création de fiches tâches vers l'API + React (staff).
- [x] Migrer la saisie des points de douleur vers l'API + React.

---

*Document à compléter au fur et à mesure de la migration.* (Dernière mise à jour : 2025-10-25)
