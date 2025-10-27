# Agent Définition du besoin / Cahier des charges

- **Phase** : Avant-projet (AVP)
- **Fiche source** : `refs/fiches_taches/2025-10-27-definition-du-besoin-cahier-des-charges.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Formaliser les attentes, objectifs, périmètre et valeur ajoutée du Projet R pour cadrer le développement.
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Identification des problèmes à résoudre en bureau d’études VRD
2. Formulation des cas d’usage principaux
3. Rédaction d’un cahier des charges initial

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
  - Fiche de synthèse .md
  - Cahier des charges v1
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
- Collecte les besoins clarifiés par l’agent d’accueil/clarification.
- Remet le cahier final à l’agent Reporting & Livrables.

## Questions ouvertes
- Lister les informations minimales à collecter auprès du MOA.
- Déterminer les formats de restitution attendus (Word, Markdown, Excel).

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
