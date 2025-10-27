> Phase : **Avant-projet (AVP)** · Dernière mise à jour : 2025-10-27

## Informations générales

- **Phase MOE** : Avant-projet (AVP)
- **Intitulé de la tâche** : Intégration de données publiques
- **Responsable / intervenants** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Description

- **Objectif** : Importer automatiquement les données cadastrales, réseaux, PLU, etc. à partir de sources ouvertes.
- **Déclencheur** : Lancement d’un nouveau projet ou réception de données sources
- **Étapes principales** :
  1. Requête sur les sources disponibles (cadastre, data.gouv.fr, etc.)
  1. Téléchargement et formatage des données
  1. Injection dans le projet


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
  - Fichiers SIG ou tabulaires
  - Documentation associée

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
