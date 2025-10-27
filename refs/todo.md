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

- [x] Concevoir une interface « utilisateur final » distincte, centrée sur les automatisations (notes, points de douleur, etc.).
- [x] Isoler l’interface de création de fiches tâches dans un espace privé / administrateur.
- [x] Mettre en place un mécanisme d’accès (auth ou protection simple) pour l’interface privée.

### Mise au norme des données d’entrées (AVP)

- [ ] Compléter la fiche (`refs/fiches_taches/2025-10-27-mise-au-norme-des-donnes-dentres.md`) : préciser étapes, données d’entrée et livrables.
- [ ] Inventorier les plans/datasets à harmoniser et définir les formats cibles.
- [ ] Identifier les outils/scripts nécessaires (AutoCAD, Covadis, routines de conversion).
- [ ] Définir une première automatisation cible (checklist + script de contrôle).

### Automatisations thèmes transverses (modules 01 → 12)

- [ ] `2025-10-27-architecture-fonctionnelle-du-projet.md` : générer automatiquement la cartographie des blocs (diagrammes + documentation) à partir d’un référentiel YAML/JSON.
- [ ] `2025-10-27-definition-du-besoin-cahier-des-charges.md` : créer un assistant de collecte (formulaire) et générateur de cahier des charges en Markdown/Word.
- [ ] `2025-10-27-mise-a-la-charte-graphique.md` : définir des scripts de validation (lint) sur plans/rapports pour garantir la charte graphique.
- [ ] `2025-10-27-gestion-de-projet-et-versionning.md` : automatiser la création d’espaces projet (Git/Notion) et la synchronisation des statuts.
- [ ] `2025-10-27-calculs-vrd.md` : connecter les moteurs de calcul aux fiches (imports quantitatifs + génération de tableaux).
- [ ] `2025-10-27-gestion-des-donnees-de-terrain.md` : mettre en place une pipeline d’ingestion terrain (imports DXF → base normalisée + géoréférencement).
- [ ] `2025-10-27-generation-de-rapports-et-livrables.md` : industrialiser la production des rapports (templates Word/PDF + scripts d’assemblage).
- [ ] `2025-10-27-verification-normative.md` : développer une check-list automatisée (règles métiers + génération de rapport de conformité).
- [ ] `2025-10-27-coordination-et-communication.md` : automatiser la diffusion des comptes-rendus / plans d’actions (emails + tableau de bord).
- [ ] `2025-10-27-integration-sig.md` : scripts d’import/export SIG (shp/geojson) et synchronisation avec la base projet.
- [ ] `2025-10-27-integration-de-donnees-publiques.md` : connecter les APIs publiques (cadastre, PLU) pour enrichir les dossiers.
- [ ] `2025-10-27-cout-et-budgetisation-automatique.md` : relier les fiches de quantités à une base de prix pour produire des estimations automatiques.
- [ ] `2025-10-27-compte-rendu-de-reunion.md` : générer des comptes rendus types avec reprise automatique des décisions/actions.
- [ ] `2025-10-27-pilotage-a-distance-slack-webhook.md` : mettre en place un bot Slack/Webhook pour notifier les jalons et suivre les tâches.

### Migration FastAPI + React

- [x] Valider l’architecture cible (`docs/migration_fastapi_react.md`) et la structure des dossiers `backend/` + `frontend/`.
- [x] Préparer l’environnement backend : dépendances FastAPI, structure initiale, endpoints de base.
- [x] Préparer l’environnement frontend : initialisation React (Vite/CRA), routage public/staff.
- [x] Implémenter l’authentification multi-comptes staff (hash + stockage sécurisé, portail React).
- [x] Migrer la création de fiches tâches vers FastAPI + React (staff).
- [x] Migrer les points de douleur vers l’API + React.
- [x] Planifier le retrait progressif de Flask après validation (`docs/retire_flask.md`).

### Backlog général

- [ ] Lister les pains points actuels sur chaque phase en suivant `refs/process_points_douleur.md`.
- [ ] Recenser les scripts/macros déjà existants dans AutoCAD, Covadis, Mensura, suite Office.
- [ ] Documenter systématiquement chaque session dans `AGENTS.md` (rappel de routine).

## En cours

- Saisie et enrichissement des fiches tâches prioritaires (`refs/fiches_taches/2025-10-25-gnration-automatise-des-notes-de-calcul-dassainissement-bassins-de-rtention-et-rseaux-ep.md`).
- Consolidation des formules et hypothèses `refs/assainissement_notes_calcul.md`.
- Suivi de la fiche « Mise au norme des données d’entrées » (`refs/fiches_taches/2025-10-27-mise-au-norme-des-donnes-dentres.md`).


## Finalisé

- [x] Interface web locale pour la saisie (app.py + templates).
- [x] Assistant de création de fiches (`scripts/create_task_sheet.py`).
- [x] Modèle de fiche tâche en Markdown (`refs/modele_fiche_tache.md`).
- [x] Extraction du PDF et synthèse Markdown (`refs/phases_taches.md`).
