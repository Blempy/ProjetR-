# Agent Coordination et communication

- **Phase** : EXE
- **Fiche source** : `refs/fiches_taches/2025-10-27-coordination-et-communication.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Faciliter l’échange entre les membres du projet via des outils numériques.
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Partage automatique des livrables
2. Centralisation des échanges par canal
3. Historisation des commentaires

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
  - Journal de communication
  - Historique des échanges
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
- Partage les plans d’action avec l’agent Gestion de Projet.
- Déclenche des alertes via l’agent Pilotage à distance.

## Questions ouvertes
- Identifier les canaux de communication privilégiés (mail, Teams, Slack).
- Définir les indicateurs de suivi à afficher.

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
