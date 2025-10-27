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
- [ ] Confirmer les sources officielles des pluies de projet utilisables (Montana, données locales, etc.).
- [ ] Standardiser le format Covadis/Mensura attendu pour les exports (colonnes, identifiants, unités).

### Interfaces web

- [x] Concevoir une interface « utilisateur final » distincte, centrée sur les automatisations (notes, points de douleur, etc.).
- [x] Isoler l’interface de création de fiches tâches dans un espace privé / administrateur.
- [x] Mettre en place un mécanisme d’accès (auth ou protection simple) pour l’interface privée.

### Mise au norme des données d’entrées (AVP)

- [ ] Compléter la fiche (`refs/fiches_taches/2025-10-27-mise-au-norme-des-donnes-dentres.md`) : préciser étapes, données d’entrée et livrables.
- [ ] Inventorier les plans/datasets à harmoniser et définir les formats cibles.
- [ ] Identifier les outils/scripts nécessaires (AutoCAD, Covadis, routines de conversion).
- [ ] Définir une première automatisation cible (checklist + script de contrôle).
- [ ] Formaliser les règles de nommage/calques validées avec le BE.

### Automatisations thèmes transverses (modules 01 → 12)

- `2025-10-27-architecture-fonctionnelle-du-projet.md` (`docs/agents/architecture-fonctionnelle-du-projet.md`)
  - [ ] Définir les niveaux de détail attendus (macro vs micro) pour les schémas fonctionnels.
  - [ ] Choisir l’outil de restitution (Mermaid, Draw.io, diagrams Python) et formaliser le template YAML/JSON.
- `2025-10-27-definition-du-besoin-cahier-des-charges.md` (`docs/agents/definition-du-besoin-cahier-des-charges.md`)
  - [ ] Lister les informations minimales à collecter auprès du MOA.
  - [ ] Décider des formats finaux (Word, Markdown, Excel) et du mode de génération.
- `2025-10-27-mise-a-la-charte-graphique.md` (`docs/agents/mise-a-la-charte-graphique.md`)
  - [ ] Rassembler les règles actuelles de charte graphique (calques, couleurs, nomenclature).
  - [ ] Prioriser les contrôles automatiques vs vérifications manuelles.
- `2025-10-27-gestion-de-projet-et-versionning.md` (`docs/agents/gestion-de-projet-et-versionning.md`)
  - [ ] Choisir les outils cibles pour la gestion de projet (Git, Notion, GanttProject, etc.).
  - [ ] Clarifier la fréquence de synchronisation et les informations à suivre automatiquement.
- `2025-10-27-calculs-vrd.md` (`docs/agents/calculs-vrd.md`)
  - [ ] Cataloguer les méthodes de calcul à supporter (rationnelle, Caquot, tables internes).
  - [ ] Identifier les gabarits AutoCAD/Covadis utilisables pour les premiers tests.
- `2025-10-27-gestion-des-donnees-de-terrain.md` (`docs/agents/gestion-des-donnees-de-terrain.md`)
  - [ ] Lister les formats livrés par les géomètres (CSV, DXF, LandXML, etc.).
  - [ ] Qualifier les conversions nécessaires avant intégration SIG ou calculs.
- `2025-10-27-generation-de-rapports-et-livrables.md` (`docs/agents/generation-de-rapports-et-livrables.md`)
  - [ ] Recenser les gabarits Word/PDF existants et ceux à créer.
  - [ ] Définir les règles de nommage et de diffusion des livrables générés.
- `2025-10-27-verification-normative.md` (`docs/agents/verification-normative.md`)
  - [ ] Établir la liste des normes et référentiels à intégrer dans les contrôles.
  - [ ] Définir le format du rapport d’écart et sa diffusion.
- `2025-10-27-coordination-et-communication.md` (`docs/agents/coordination-et-communication.md`)
  - [ ] Identifier les canaux de communication à supporter (mail, Teams, Slack, …).
  - [ ] Choisir les indicateurs de suivi ou KPI à afficher automatiquement.
- `2025-10-27-integration-sig.md` (`docs/agents/integration-sig.md`)
  - [ ] Préciser les systèmes de coordonnées utilisés par projet.
  - [ ] Planifier les fréquences de mise à jour des fonds externes.
- `2025-10-27-integration-de-donnees-publiques.md` (`docs/agents/integration-de-donnees-publiques.md`)
  - [ ] Lister les APIs open data prioritaires (cadastre, PLU, réseaux).
  - [ ] Vérifier les licences d’utilisation et contraintes juridiques.
- `2025-10-27-cout-et-budgetisation-automatique.md` (`docs/agents/cout-et-budgetisation-automatique.md`)
  - [ ] Structurer la base de prix (sources, unités, versioning).
  - [ ] Définir le process de validation humaine avant diffusion d’un budget.
- `2025-10-27-compte-rendu-de-reunion.md` (`docs/agents/compte-rendu-de-reunion.md`)
  - [ ] Confirmer les sources d’entrée (notes manuscrites, audio, chat).
  - [ ] Définir le format standard du compte rendu (rubriques, styles).
- `2025-10-27-pilotage-a-distance-slack-webhook.md` (`docs/agents/pilotage-a-distance-slack-webhook.md`)
  - [ ] Valider les espaces Slack/webhook déjà disponibles.
  - [ ] Lister les actions à déclencher automatiquement depuis Slack/bot.
- `2025-10-27-test-api-fiche.md` (`docs/agents/test-api-fiche.md`)
  - [ ] Lister les endpoints à tester en priorité (création fiche, points de douleur, auth).
  - [ ] Définir les jeux de données de test et les assertions attendues.

### Agents conversationnels (orchestrateur & prompts)

- [ ] Formaliser le schéma d’échange entre orchestrateur, agent de dispatch et spécialistes (format JSON, événements, erreurs).
- [ ] Rédiger un premier jet de prompts pour l’agent d’accueil, l’agent de clarification et l’agent de synthèse.
- [ ] Générer une version JSON/YAML des briefs `docs/agents/*.md` pour chargement automatique par le backend.
- [ ] Prototyper un endpoint FastAPI `/api/agents/route` qui appelle l’orchestrateur avec une requête utilisateur.
- [ ] Définir un plan de tests (unitaires + scénarios de bout en bout) pour valider les enchaînements d’agents.

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
