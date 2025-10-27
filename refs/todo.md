# Todo — Automatisation MOE VRD

## À lancer

### Automatisation notes de calcul EP

- [ ] Concevoir un assistant interactif (formulaire web) pour renseigner les paramètres de la note et générer la sortie Excel/PDF.
- [ ] Ajouter une section de saisie manuelle des surfaces (tableau + liste déroulante du type de surface) dans l’assistant web.
- [ ] Concevoir un modèle Excel (saisie + export PDF) et gabarit Word associé pour la note de calcul.
- [ ] Tester l’export automatique Covadis/Mensura → Excel (surfaces, pentes, identifiants de tronçons).
- [ ] Constituer une bibliothèque de coefficients (ruissellement, pluies de projet) réutilisable par les scripts.
- [ ] Prototyper le script Python d’extraction des données AutoCAD/Covadis et de génération de la note.
- [ ] Préparer une future feature : extraction automatique des surfaces (AutoCAD/Covadis/Mensura) pour alimenter la saisie.

### Interfaces web

- [ ] Concevoir une interface « utilisateur final » distincte, centrée sur les automatisations (notes, pain points, etc.).
- [ ] Isoler l’interface de création de fiches tâches dans un espace privé / administrateur.
- [ ] Mettre en place un mécanisme d’accès (auth ou protection simple) pour l’interface privée.

### Migration FastAPI + React

- [x] Valider l’architecture cible (`docs/migration_fastapi_react.md`) et la structure des dossiers `backend/` + `frontend/`.
- [x] Préparer l’environnement backend : dépendances FastAPI, structure initiale, endpoints de base.
- [x] Préparer l’environnement frontend : initialisation React (Vite/CRA), routage public/staff.
- [x] Implémenter l’authentification multi-comptes staff (hash + stockage sécurisé, portail React).
- [x] Migrer la création de fiches tâches vers FastAPI + React (staff).
- [ ] Migrer les points de douleur vers l’API + React.
- [ ] Planifier le retrait progressif de Flask après validation.

### Backlog général

- [ ] Lister les pains points actuels sur chaque phase en suivant `refs/process_points_douleur.md`.
- [ ] Recenser les scripts/macros déjà existants dans AutoCAD, Covadis, Mensura, suite Office.
- [ ] Documenter systématiquement chaque session dans `AGENTS.md` (rappel de routine).

## En cours

- Saisie et enrichissement des fiches tâches prioritaires (`refs/fiches_taches/2025-10-25-gnration-automatise-des-notes-de-calcul-dassainissement-bassins-de-rtention-et-rseaux-ep.md`).
- Consolidation des formules et hypothèses `refs/assainissement_notes_calcul.md`.


## Finalisé

- [x] Interface web locale pour la saisie (app.py + templates).
- [x] Assistant de création de fiches (`scripts/create_task_sheet.py`).
- [x] Modèle de fiche tâche en Markdown (`refs/modele_fiche_tache.md`).
- [x] Extraction du PDF et synthèse Markdown (`refs/phases_taches.md`).
