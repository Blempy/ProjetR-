# Agent Intégration de données publiques

- **Phase** : Avant-projet (AVP)
- **Fiche source** : `refs/fiches_taches/2025-10-27-integration-de-donnees-publiques.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Importer automatiquement les données cadastrales, réseaux, PLU, etc. à partir de sources ouvertes.
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Requête sur les sources disponibles (cadastre, data.gouv.fr, etc.)
2. Téléchargement et formatage des données
3. Injection dans le projet

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
  - Fichiers SIG ou tabulaires
  - Documentation associée
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
- Alimente l’agent SIG en données réglementaires.
- Informe l’agent Cahier des Charges des contraintes relevées.

## Questions ouvertes
- Établir la liste des APIs open data prioritaires.
- Qualifier les licences et conditions d’utilisation.

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
