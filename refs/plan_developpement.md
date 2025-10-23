# Plan de développement pour l'automatisation MOE VRD

> Dernière mise à jour : 2025-10-24 — à ajuster lors de la prochaine édition.

## Objectifs

- Disposer d'un référentiel clair des phases, tâches et livrables de la maîtrise d'œuvre VRD.
- Identifier les tâches répétitives susceptibles d'être automatisées (scripts, modèles, gabarits, check-lists).
- Mettre en place une démarche incrémentale : documentation → prototypes → automatisations pérennes.

## Méthode générale

1. **Inventaire**
   - Consolider la description des phases et des tâches récurrentes (à partir du PDF et des retours terrain).
   - Qualifier les entrées/sorties de chaque tâche (données, documents, acteurs).
2. **Priorisation**
   - Classer les tâches par volume, fréquence, douleur (temps, risques d'erreur).
   - Identifier les outils déjà utilisés (AutoCAD, Covadis, Mensura, AutoTurn, suite Office, GanttProject).
3. **Conception d'automatisations**
   - Définir pour chaque tâche prioritaire le scénario cible (macro, script, gabarit, formulaire, etc.).
   - Prévoir les données de référence à maintenir (bibliothèque de blocs, modèles, tableaux types).
4. **Prototypage et validation**
   - Produire des preuves de concept rapides.
   - Tester sur des projets passés ou cas fictifs.
   - Documenter les gains et les ajustements nécessaires.
5. **Industrialisation**
   - Formaliser la procédure (pas-à-pas, prérequis, points de contrôle).
   - Organiser les sources : scripts versionnés, modèles partagés, documentation.
6. **Suivi et amélioration continue**
   - Mettre à jour le plan et la todo à chaque sprint.
   - Collecter les retours d'usage pour décider des itérations suivantes.

## Phases de mission (référentiel validé)

| Phase MOE | Objectif principal | Livrables clés | Référence détaillée |
| --- | --- | --- | --- |
| Études préliminaires | Vérifier la faisabilité technique, réglementaire et financière | Note de faisabilité, plan de principe, estimation sommaire | `refs/phases_taches.md#1-études-préliminaires` |
| Avant-projet (AVP) | Définir les grandes lignes techniques et géométriques | Plans AVP, note technique, estimation détaillée | `refs/phases_taches.md#2-avant-projet-avp` |
| Projet (PRO) | Finaliser le dossier technique pour consultation | Plans d'exécution, CCTP, BPU, estimatif définitif | `refs/phases_taches.md#3-projet-pro` |
| Assistance à la passation des contrats (ACT) | Préparer et analyser la consultation des entreprises | DCE complet, rapport d'analyse des offres | `refs/phases_taches.md#4-assistance-à-la-passation-des-contrats-de-travaux-act` |
| Direction de l'exécution / VISA (DET/VISA) | Suivre et contrôler le chantier | Comptes rendus, ordres de service, suivi financier | `refs/phases_taches.md#5-direction-de-lexécution-des-travaux-det--visa` |
| Assistance aux opérations de réception (AOR) | Réceptionner et clôturer le chantier | PV de réception, registre des réserves, DOE | `refs/phases_taches.md#6-assistance-aux-opérations-de-réception-aor` |

> Action en cours : enrichir chaque phase avec ses fiches tâches détaillées (inputs/outputs/outils/priorité).

## Backlog initial (esquisse)

- [x] Extraire la liste complète des phases et tâches du PDF fourni (`Phases_MOE_VRD_reformate.pdf`).
- [ ] Compléter/valider les intitulés avec le vocabulaire interne utilisé habituellement.
- [ ] Pour chaque tâche, noter les livrables et outils mobilisés.
- [ ] Identifier rapidement les tâches les plus consommatrices de temps.

## Documents et ressources à préparer

- Gabarits : modèles Word/Excel, charte AutoCAD, légendes Covadis/Mensura.
- Scripts/macro : AutoCAD (AutoLISP), VBA Office, Python (si pertinent), `scripts/create_task_sheet.py` (assistant fiches Markdown).
- Tableaux de bord : suivi de projet (Excel ou Power BI/LibreOffice), diagrammes Gantt.
- Guides : procédures pour lancer chaque automatisation, vidéos courtes (optionnel).

## Prochaines étapes proposées

1. Confirmer la structure exacte des phases/tâches via le PDF et les retours terrain.
2. Décider d'un format type pour décrire chaque tâche (fiche standard en Markdown).
3. Définir les priorités à court terme (ex. automatiser la mise en forme des pièces écrites).
4. Établir un calendrier souple (sprints mensuels ou bimensuels).
5. Documenter les outils et langages à privilégier (VBA, scripts AutoCAD, etc.).
