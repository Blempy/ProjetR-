# Agent Mise au norme des données d'entrées

- **Phase** : AVP
- **Fiche source** : `refs/fiches_taches/2025-10-27-mise-au-norme-des-donnes-dentres.md`
- **Priorité** : Haute
- **Statut** : À lancer
- **Responsable initial** : blempy
- **Fréquence** : À chaque projet
- **Durée estimée** : 6h

## Mission
- **Objectif principal** : Centraliser et harmoniser tous les jeux de données d’entrée (plans DWG/DXF, levés géomètre, couches SIG) pour qu’ils respectent la charte BE et puissent alimenter les calculs hydrauliques ou VRD sans retraitement manuel.
- **Déclencheurs connus** :
  - Réception d’un dossier DWG/DXF provenant d’un partenaire (architecte, géomètre, concessionnaire).
  - Lancement d’un nouveau projet nécessitant la constitution d’un socle terrain/métrés fiable.

## Workflow cible
1. Recenser les fichiers reçus (DWG/DXF, relevés, exports SIG) et inventorier les versions.
2. Contrôler le système de coordonnées et reprojeter si besoin vers le référentiel projet.
3. Appliquer la table de correspondance des calques / objets pour se conformer à la charte interne.
4. Vérifier les attributs (unités, altimétrie, surfaces) et consigner les écarts dans un rapport QA.
5. Livrer le « pack normalisé » (plans nettoyés + log des corrections) dans le dossier projet partagé.

## Entrées à mobiliser
- **Données** :
  - Plans DWG/DXF bruts des partenaires.
  - Levés topographiques / MNT fournis par le géomètre.
  - Couches SIG d’environnement (cadastre, réseaux, zonages).
  - Table de correspondance calques / objets (charte BE).
- **Documents de référence** :
  - Charte graphique et nomenclature des calques BE.
  - Procédure interne de contrôle qualité (check-list Excel).
  - Plan masse ou arrêté fixant le système de coordonnées du projet.
- **Logiciels / outils** :
  - AutoCAD / Covadis pour les opérations sur DWG/DXF.
  - QGIS ou FME pour les conversions SIG.
  - Scripts Python (pyautocad, ezdxf) pour l’automatisation.
  - Tableur (Excel/LibreOffice) pour la check-list et le log d’anomalies.

## Sorties attendues
- **Livrables** :
  - Dossier `02_Donnees_normalisees` avec les DWG/DXF nettoyés.
  - Rapport de contrôle / log des modifications et incohérences.
  - Check-list validée (coordonnées, calques, unités, attributs).
- **Formats** :
  - DWG/DXF nettoyés, SHP/GeoPackage reprojetés.
  - CSV ou XLSX pour le log et la check-list.
  - PDF de synthèse QA (facultatif pour diffusion externe).
- **Destinataires / diffusion** :
  - Équipe études VRD (agent Calculs VRD, agent Notes de calcul EP).
  - Agent Charte Graphique pour contrôle visuel final.
  - Stockage projet partagé (SharePoint, Nextcloud, Git LFS).

## Points de douleur à traiter
- Renommage manuel des calques et blocs pour chaque partenaire.
- Incohérences de projection entraînant des décalages de plusieurs mètres.
- Noms de fichiers / versions multiples sans traçabilité.
- Manque de visibilité sur les corrections appliquées (pas de log standard).

## Idées d'automatisation
- **Pistes actuelles** :
  - Script Python appliquant la table de correspondance calques/blocs et générant un fichier log.
  - Modèle QGIS/FME pour reprojeter et découper les couches SIG au périmètre projet.
  - Check-list automatisée (Excel + macros) qui valide unités, altitude, polylignes fermées, doublons.
- **Type envisagé** : Automatisation locale (scripts Python + gabarits QGIS/Excel).
- **Pré-requis** : Charte validée et table de correspondance à jour, arborescence projet standard, liste des EPSG autorisés.
- **Niveau d'effort** : Moyen.
- **Bénéfices attendus** :
  - Réduction du temps de mise au propre (≈ -50 %).
  - Fiabilité accrue des données d’entrée pour les calculs et exports.
  - Traçabilité des corrections et des sources initiales.

## Interactions et dépendances
- Alimente l’agent Calculs VRD avec des fichiers homogènes.
- Travaille avec l’agent SIG pour maintenir les projections cohérentes.
- Coordonne les contrôles avec l’agent Charte Graphique (lint visuel).

## Questions ouvertes
- Recenser les jeux de données prioritaires à normaliser.
- Valider les règles de nommage et calques par discipline.
- Choisir le format du mapping (CSV, JSON) pour le script de renaming.

## Actions prioritaires
- Collecter les plans types récents et construire la table de correspondance calques/blocs.
- Formaliser la check-list QC (coordonnées, unités, attributs obligatoires) dans un tableur partagé.
- Prototyper le script Python d’automatisation (renommage + log) sur un jeu pilote.

## Documents liés
- `config/charte_graphique.json` (à compléter).
- Check-list QA Excel (à créer).
