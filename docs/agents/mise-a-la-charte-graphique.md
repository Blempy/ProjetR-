# Agent Mise à la charte graphique

- **Phase** : Avant-projet (AVP)
- **Fiche source** : `refs/fiches_taches/2025-10-27-mise-a-la-charte-graphique.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : Responsable projet / Dev Python
- **Fréquence** : À chaque nouveau plan
- **Durée estimée** : 0.5 à 2h par tâche

## Mission
- **Objectif principal** : Uniformiser les calques, appliquer les conventions BE, structurer le plan DWG.
- **Déclencheurs connus** :
  - Lancement d’un nouveau projet ou réception de données sources

## Workflow cible
1. Récupération du plan DWG brut
2. Analyse des calques et objets
3. Renommage automatique
4. Application de la charte graphique définie

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
  - Plan DWG mis à jour
  - Rapport d’audit des calques (PDF/Excel)
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
- Réutilise les données nettoyées par l’agent Données d’Entrées.
- Informe l’agent Reporting & Livrables des écarts de charte.

## Questions ouvertes
- Rassembler les règles de charte graphique existantes.
- Prioriser les contrôles automatiques vs check manuel.

## Actions prioritaires
- Développement du module

## Documents liés
- config.json
- charte_graphique.json
