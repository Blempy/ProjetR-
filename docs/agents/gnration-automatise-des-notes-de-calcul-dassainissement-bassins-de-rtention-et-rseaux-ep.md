# Agent Génération automatisée des notes de calcul d’assainissement (bassins de rétention et réseaux EP)

- **Phase** : Avant-projet (AVP)
- **Fiche source** : `refs/fiches_taches/2025-10-25-gnration-automatise-des-notes-de-calcul-dassainissement-bassins-de-rtention-et-rseaux-ep.md`
- **Priorité** : Très haute.
- **Statut** : À lancer.
- **Responsable initial** : Ingénieur hydrologue / Technicien VRD
- **Fréquence** : À chaque projet comportant un réseau d’eaux pluviales
- **Durée estimée** : 4 à 6 heures sans automatisation

## Mission
- **Objectif principal** : Établir les notes de calcul nécessaires à la justification hydraulique des ouvrages d’assainissement (dimensionnement des bassins, volumes de stockage, débit de fuite, diamètres de canalisations, etc.) selon les pluies de référence et les coefficients de ruissellement.
- **Déclencheurs connus** :
  - Après la définition du projet de nivellement et du zonage d’imperméabilisation.

## Workflow cible
1. Collecte des surfaces imperméabilisées par zone.
2. Calcul des volumes ruisselés selon les pluies de projet (méthode rationnelle ou pluviogramme).
3. Dimensionnement du bassin de rétention et calcul du débit de fuite (loi de Darcy-Weisbach ou orifice calibré).
4. Vérification des vitesses d’écoulement dans le réseau et ajustement des diamètres.
5. Rédaction et mise en page de la note de calcul dans un document Word ou PDF.

## Entrées à mobiliser
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

## Points de douleur à traiter
- Calculs manuels fastidieux et répétitifs entre Excel, Covadis et Word.
- Risques d’erreurs lors de la mise à jour des surfaces ou coefficients.
- Aucune traçabilité des hypothèses de calcul (version, pluie, coefficient).
- Temps perdu à reformater les tableaux et schémas dans la note finale.

## Idées d'automatisation
- **Pistes actuelles** :
  - Développer un module Python (AutoCAD + bibliothèque hydrologique) qui :
  - extrait automatiquement les surfaces et pentes depuis le dessin,
  - calcule les volumes de stockage et débits de fuite selon les paramètres hydrologiques,
  - remplit un modèle Excel/Word pour produire la note de calcul et les tableaux.
  - Mettre en place une bibliothèque de coefficients (ruissellement, pluies) centralisée pour alimenter les scripts.
- **Type envisagé** : Python + modèle Word automatisé.
- **Pré-requis** : Base de données des coefficients de ruissellement et pluies de référence.
- **Niveau d'effort** : Élevé.
- **Bénéfices attendus** :
  - Réduction de 70 % du temps d’étude, standardisation des rendus, diminution des erreurs et justification technique automatique.

## Interactions et dépendances
- Travaille avec l’agent Calculs VRD pour consolider les données hydrauliques.
- Consulte l’agent Normes & Conformité pour valider les hypothèses réglementaires.

## Questions ouvertes
- Confirmer les sources officielles des pluies de projet pour chaque territoire.
- Définir le format cible des exports Covadis/Mensura (colonnes, identifiants).

## Actions prioritaires
- [ ] Recenser les formules et méthodes de calcul utilisées (documentation interne, Fascicule 70).
- [ ] Créer un modèle Excel avec feuilles de saisie + export PDF automatique.
- [ ] Tester un export Covadis → Excel contenant surfaces/pentes identifiées.

## Documents liés
- `refs/phases_taches.md#2-avant-projet-avp`
- Modèle de note (à créer) — à lier dès disponibilité.
