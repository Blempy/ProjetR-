# Fiche tâche — Génération automatisée des notes de calcul d’assainissement (bassins de rétention et réseaux EP)

> Phase : **Avant-projet (AVP)** · Dernière mise à jour : 2025-10-25

## Informations générales

- **Phase MOE** : Avant-projet (AVP)
- **Intitulé de la tâche** : Génération automatisée des notes de calcul d’assainissement (bassins de rétention et réseaux EP)
- **Responsable / intervenants** : Ingénieur hydrologue / Technicien VRD
- **Fréquence** : À chaque projet comportant un réseau d’eaux pluviales
- **Durée estimée** : 4 à 6 heures sans automatisation

## Description

- **Objectif** : Établir les notes de calcul nécessaires à la justification hydraulique des ouvrages d’assainissement (dimensionnement des bassins, volumes de stockage, débit de fuite, diamètres de canalisations, etc.) selon les pluies de référence et les coefficients de ruissellement.
- **Déclencheur** : Après la définition du projet de nivellement et du zonage d’imperméabilisation.
- **Étapes principales** :
  1. Collecte des surfaces imperméabilisées par zone.
  2. Calcul des volumes ruisselés selon les pluies de projet (méthode rationnelle ou pluviogramme).
  3. Dimensionnement du bassin de rétention et calcul du débit de fuite (loi de Darcy-Weisbach ou orifice calibré).
  4. Vérification des vitesses d’écoulement dans le réseau et ajustement des diamètres.
  5. Rédaction et mise en page de la note de calcul dans un document Word ou PDF.

## Entrées / ressources nécessaires

- **Données** :
  - Surfaces imperméabilisées par zone (export AutoCAD/Covadis → Excel avec ID de tronçon).
  - Pentes des collecteurs et longueurs (exports Covadis/Mensura structurés).
  - Coefficients de ruissellement par type de surface (tableau de références interne ou veille web).
  - Pluies décennales / centennales (coefficients de Montana ou données locales).
- **Documents de référence** :
  - Fascicule 70, DTU 60.11, arrêtés préfectoraux, règlement local d’assainissement.
- **Logiciels / outils** :
  - Excel, Covadis, AutoCAD, Word.

## Sorties attendues

- **Livrables** :
  - Note de calcul hydraulique (modèle Excel → PDF).
  - Schéma du réseau eaux pluviales annoté (AutoCAD/Covadis/Mensura).
  - Tableau de synthèse des débits et volumes (export Excel).
- **Formats** :
  - PDF, DOCX, DWG.
- **Destinataires / diffusion** :
  - Maître d’ouvrage, service urbanisme, bureau de contrôle.

## Points de douleur actuels

- Calculs manuels fastidieux et répétitifs entre Excel, Covadis et Word.
- Risques d’erreurs lors de la mise à jour des surfaces ou coefficients.
- Aucune traçabilité des hypothèses de calcul (version, pluie, coefficient).
- Temps perdu à reformater les tableaux et schémas dans la note finale.

## Pistes d'automatisation

- **Idées / solutions** :
  - Développer un module Python (AutoCAD + bibliothèque hydrologique) qui :
    - extrait automatiquement les surfaces et pentes depuis le dessin,
    - calcule les volumes de stockage et débits de fuite selon les paramètres hydrologiques,
    - remplit un modèle Excel/Word pour produire la note de calcul et les tableaux.
  - Mettre en place une bibliothèque de coefficients (ruissellement, pluies) centralisée pour alimenter les scripts.
- **Type** : Python + modèle Word automatisé.
- **Pré-requis** : Base de données des coefficients de ruissellement et pluies de référence.
- **Niveau d'effort** : Élevé.
- **Bénéfices attendus** :
  - Réduction de 70 % du temps d’étude, standardisation des rendus, diminution des erreurs et justification technique automatique.

## État et priorisation

- **Priorité** : Très haute.
- **Statut** : À lancer.
- **Prochaine action** :
  - [ ] Recenser les formules et méthodes de calcul utilisées (documentation interne, Fascicule 70).
  - [ ] Créer un modèle Excel avec feuilles de saisie + export PDF automatique.
  - [ ] Tester un export Covadis → Excel contenant surfaces/pentes identifiées.
- **Documents liés** :
  - `refs/phases_taches.md#2-avant-projet-avp`
  - Modèle de note (à créer) — à lier dès disponibilité.
