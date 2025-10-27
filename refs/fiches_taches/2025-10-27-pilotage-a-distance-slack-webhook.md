> Phase : **Support** · Dernière mise à jour : 2025-10-27

## Informations générales

- **Phase MOE** : Support
- **Intitulé de la tâche** : Pilotage à distance / Slack / Webhook
- **Responsable / intervenants** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Description

- **Objectif** : Permettre le lancement de tâches ou l'interaction avec le système depuis l’extérieur (Slack, API, etc.).
- **Déclencheur** : Lancement d’un nouveau projet ou réception de données sources
- **Étapes principales** :
  1. Définition des commandes disponibles
  1. Connexion à Slack / interface webhook
  1. Traitement des commandes et retour utilisateur


## Entrées / ressources nécessaires

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

## Points de douleur actuels

- Tâche répétitive et chronophage
- Risque d’erreur humaine sur les noms/calques

## Pistes d'automatisation

- **Idées / solutions** :
  - Script Python de renommage automatique
  - Vérification par rapport à un fichier de référence
- **Type** : Automatisation locale
- **Pré-requis** : Plan DWG propre et configuration BE
- **Niveau d'effort** : Moyen
- **Bénéfices attendus** :
  - Gain de temps
  - Standardisation et fiabilité

## État et priorisation

- **Priorité** : Haute
- **Statut** : À lancer
- **Prochaine action** : Développement du module
- **Documents liés** :
  - config.json, charte_graphique.json
