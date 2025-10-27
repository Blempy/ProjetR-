# Agent Gestion des données de terrain

- **Phase** : Avant-projet (AVP)
- **Fiche source** : `refs/fiches_taches/2025-10-27-gestion-des-donnees-de-terrain.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Analyser les altitudes, importer les levés, générer les profils en long et en travers.
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Import de données topographiques (points, MNT)
2. Génération automatique des profils
3. Analyse des pentes et ruptures

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
  - Profils au format PDF
  - Données altimétriques structurées
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
- Partage les levés avec l’agent SIG pour intégration géoréférencée.
- Prépare les données pour l’agent Calculs VRD.

## Questions ouvertes
- Lister les formats fournis par les géomètres (CSV, DXF, LandXML).
- Identifier les conversions nécessaires pour l’intégration SIG.

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
