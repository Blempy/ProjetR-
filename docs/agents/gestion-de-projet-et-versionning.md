# Agent Gestion de projet et versionning

- **Phase** : Toutes phases
- **Fiche source** : `refs/fiches_taches/2025-10-27-gestion-de-projet-et-versionning.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Suivre l’évolution du projet, archiver les versions, tracer les actions automatiques.
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Initialisation du projet (config.json, dossiers, logs)
2. Suivi des versions et des livrables générés
3. Archivage automatique des livrables

## Entrées à mobiliser
- **Données** :
  - Fichiers DWG / DXF
  - Configuration charte / paramètres projet
- **Documents de référence** :
  - Charte graphique BE
- **Logiciels / outils** :
  - AutoCAD, Python, Librairie interne Projet R

## Sorties attendues
- **Livrables** :
  - Fichiers de logs
  - Historique des versions
  - Structure de projet normalisée
- **Formats** :
  - DWG, PDF, Excel, JSON
- **Destinataires / diffusion** :
  - Équipe projet, archivage automatique

## Points de douleur à traiter
- Tâche répétitive et chronophage
- Risque d’erreur humaine sur les noms/calques

## Idées d'automatisation
- **Pistes actuelles** :
  - Script Python de renommage automatique
  - Vérification par rapport à un fichier de référence
- **Type envisagé** : Automatisation locale
- **Pré-requis** : Plan DWG propre et configuration BE
- **Niveau d'effort** : Moyen
- **Bénéfices attendus** :
  - Gain de temps
  - Standardisation et fiabilité

## Interactions et dépendances
- Assure la traçabilité des livrables de tous les agents spécialisés.
- Déclenche des rappels via l’agent Pilotage à distance (Slack/Webhook).

## Questions ouvertes
- Choisir les outils cibles (Git, Notion, GanttProject…).
- Clarifier la fréquence de synchronisation attendue.

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
