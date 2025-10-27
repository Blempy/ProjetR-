# Agent Architecture fonctionnelle du projet

- **Phase** : Avant-projet (AVP)
- **Fiche source** : `refs/fiches_taches/2025-10-27-architecture-fonctionnelle-du-projet.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Définir les blocs fonctionnels, les interactions entre modules et les flux de données du Projet R.
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Identification des blocs fonctionnels (moteur métier, connecteurs, interface, etc.)
2. Cartographie des interactions entre blocs
3. Production d’un schéma et documentation associée

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
  - Diagramme fonctionnel
  - Documentation structurée (.md)
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
- Synchronise la cartographie fonctionnelle avec l’agent Gestion de Projet & Versionning.
- Diffuse les schémas via l’agent Coordination & Communication.

## Questions ouvertes
- Définir les niveaux de détail attendus (macro vs micro) dans les schémas.
- Identifier les outils de modélisation privilégiés (Mermaid, Draw.io, etc.).

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
