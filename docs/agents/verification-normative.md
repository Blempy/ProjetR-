# Agent Vérification normative

- **Phase** : Avant-projet (AVP)
- **Fiche source** : `refs/fiches_taches/2025-10-27-verification-normative.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Contrôler la conformité des plans et données avec les normes en vigueur (pentes minimales, accessibilité, etc.).
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Analyse des objets selon leur usage (voirie, trottoir, accès PMR…)
2. Application des seuils de conformité
3. Signalement des non-conformités

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
  - Rapport de conformité
  - Fichier JSON des erreurs
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
- Contrôle les livrables des agents Calculs VRD et Notes de calcul.
- Retourne les écarts à l’agent Reporting & Livrables.

## Questions ouvertes
- Fournir la liste des normes et référentiels à intégrer.
- Déterminer le format de rapport d’écart attendu.

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
