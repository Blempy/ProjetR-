# Fiche tâche — Mise au norme des données d'entrées

> Phase : **AVP** · Dernière mise à jour : 2025-10-27

## Informations générales

- **Phase MOE** : AVP
- **Intitulé de la tâche** : Mise au norme des données d'entrées
- **Responsable / intervenants** : blempy
- **Fréquence** : À chaque projet
- **Durée estimée** : 6h

## Description

- **Objectif** : Centraliser et harmoniser tous les jeux de données d’entrée (plans DWG/DXF, levés géomètre, couches SIG) pour qu’ils respectent la charte BE et puissent alimenter les calculs VRD sans retraitement manuel.
- **Déclencheur** : Réception d’un dossier DWG/DXF partenaire ou lancement d’un projet nécessitant un socle terrain fiabilisé.
- **Étapes principales** :
  1. Recenser les fichiers reçus (DWG/DXF, levés, SIG) et inventorier les versions.
  2. Contrôler le système de coordonnées et reprojeter si besoin vers le référentiel projet.
  3. Appliquer la table de correspondance des calques/objets pour aligner la charte interne.
  4. Vérifier unités, altimétrie, surfaces et consigner les écarts dans un rapport QA.
  5. Livrer le « pack normalisé » (plans nettoyés + log) dans le dossier projet partagé.

## Entrées / ressources nécessaires

- **Données** :
  - Plans DWG/DXF bruts (architecte, géomètre, concessionnaire).
  - Levés topographiques / MNT fournis par le géomètre.
  - Couches SIG (cadastre, réseaux, zonages, servitudes).
  - Table de correspondance calques / objets validée (charte BE).
- **Documents de référence** :
  - Charte graphique et nomenclature des calques BE.
  - Procédure interne de contrôle qualité (check-list Excel).
  - Plan masse ou arrêté fixant le système de coordonnées du projet.
- **Logiciels / outils** :
  - AutoCAD / Covadis, scripts Python (pyautocad, ezdxf).
  - QGIS / FME pour les reprojections et conversions SIG.
  - Tableur (Excel/LibreOffice) pour la check-list et le log d’anomalies.

## Sorties attendues

- **Livrables** :
  - Dossier `02_Donnees_normalisees` avec les DWG/DXF nettoyés.
  - Rapport de contrôle / log des modifications et incohérences.
  - Check-list validée (coordonnées, unités, attributs).
- **Formats** :
  - DWG/DXF, SHP/GeoPackage reprojetés.
  - CSV ou XLSX pour la check-list et le log.
  - PDF de synthèse QA si diffusion externe.
- **Destinataires / diffusion** :
  - Équipe études VRD (agents Calculs VRD et Notes de calcul).
  - Agent Charte Graphique pour contrôle visuel final.
  - Stockage projet partagé (SharePoint / Nextcloud / Git LFS).

## Points de douleur actuels

- Renommage manuel des calques et blocs selon la provenance.
- Incohérences de projection entraînant des décalages métriques.
- Versions multiples sans traçabilité des corrections.
- Absence de log standard pour consigner les contrôles.

## Pistes d'automatisation

- **Idées / solutions** :
  - Script Python appliquant la table de correspondance calques/blocs et générant un log.
  - Modèle QGIS/FME pour reprojeter et découper les couches SIG au périmètre projet.
  - Check-list automatisée (Excel + macros) validant unités, altitude, polylignes fermées et doublons.
- **Type** : Automatisation locale (scripts Python + gabarits SIG/Excel).
- **Pré-requis** : Charte et table de correspondance à jour, arborescence projet standard, liste EPSG autorisés.
- **Niveau d'effort** : Moyen
- **Bénéfices attendus** :
  - Réduction du temps de mise au propre (~50 %).
  - Fiabilité accrue des données d’entrée.
  - Traçabilité des corrections et sources initiales.

## État et priorisation

- **Priorité** : Haute
- **Statut** : À lancer
- **Prochaine action** : Compiler les plans types récents et construire la table de correspondance calques/blocs.
- **Documents liés** :
  - `config/charte_graphique.json` (à compléter).
  - Check-list QA Excel (à créer).
