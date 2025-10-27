# Agent Compte rendu de réunion

- **Phase** : PRO / EXE
- **Fiche source** : `refs/fiches_taches/2025-10-27-compte-rendu-de-reunion.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Générer automatiquement les comptes rendus à partir des échanges ou notes audio/texte.
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Transcription des échanges (manuelle ou IA)
2. Structuration en CR normalisé
3. Archivage et diffusion

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
  - Compte rendu PDF
  - Journal des décisions
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
- S’appuie sur les notes collectées par l’agent Coordination.
- Diffuse les comptes rendus via l’agent Reporting & Livrables.

## Questions ouvertes
- Savoir si des enregistrements audio sont disponibles.
- Définir la structure standard du compte rendu souhaité.

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
