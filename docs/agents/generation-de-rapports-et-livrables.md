# Agent Génération de rapports et livrables

- **Phase** : PRO / DCE
- **Fiche source** : `refs/fiches_taches/2025-10-27-generation-de-rapports-et-livrables.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Créer automatiquement les documents finaux : métrés, rapports d’audit, plans annotés.
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Collecte des résultats depuis les modules précédents
2. Mise en page automatique des livrables
3. Export en PDF, Excel, DWG annoté

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
  - Rapports PDF
  - Tableaux Excel
  - Plans annotés
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
- Assemble les productions des agents Budgétisation, Notes de calcul, Coordination.
- Sollicite l’agent Charte Graphique pour le contrôle visuel.

## Questions ouvertes
- Recenser les gabarits Word/PDF existants.
- Définir les règles de nommage des livrables finaux.

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
