# Agent Coût et budgétisation automatique

- **Phase** : PRO / DCE
- **Fiche source** : `refs/fiches_taches/2025-10-27-cout-et-budgetisation-automatique.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Estimer automatiquement les coûts des travaux à partir des métrés et ratios.
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Récupération des quantités
2. Application des prix unitaires du bordereau
3. Calcul du budget global

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
  - Bordereau estimatif
  - Synthèse économique
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
- Utilise les quantités fournies par l’agent Calculs VRD.
- Transmet les estimations à l’agent Reporting & Livrables.

## Questions ouvertes
- Confirmer la structure de la base de prix à exploiter.
- Préciser les validations humaines nécessaires avant diffusion.

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
