# Agent Pilotage à distance / Slack / Webhook

- **Phase** : Support
- **Fiche source** : `refs/fiches_taches/2025-10-27-pilotage-a-distance-slack-webhook.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Permettre le lancement de tâches ou l'interaction avec le système depuis l’extérieur (Slack, API, etc.).
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Définition des commandes disponibles
2. Connexion à Slack / interface webhook
3. Traitement des commandes et retour utilisateur

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
  - Interface webhook active
  - Documentation des commandes
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
- Diffuse les notifications émises par l’agent Coordination.
- Peut lancer des workflows chez les agents spécialisés sur commande.

## Questions ouvertes
- Valider les espaces Slack / webhook disponibles.
- Définir les actions à déclencher automatiquement depuis Slack.

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
