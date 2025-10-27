# Agent Intégration SIG

- **Phase** : AVP
- **Fiche source** : `refs/fiches_taches/2025-10-27-integration-sig.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Utiliser les couches géographiques comme support d’analyse ou enrichissement du projet.
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Chargement de couches SIG (shapefile, GeoJSON)
2. Projection et calage spatial
3. Croisement avec objets projet

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
  - Fichiers SIG enrichis
  - Cartes d’analyse
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
- Importe les flux de l’agent Données Publiques.
- Diffuse des couches à l’agent Coordination & Communication.

## Questions ouvertes
- Préciser les systèmes de coordonnées utilisés.
- Déterminer les fréquences de mise à jour des fonds externes.

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
