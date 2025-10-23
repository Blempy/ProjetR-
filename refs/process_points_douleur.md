# Processus de collecte des points de douleur par phase

> Objectif : identifier rapidement les tâches les plus chronophages ou risquées afin de prioriser les automatismes à développer.  
> Outil recommandé : formulaire web (`python3 app.py` → onglet « Point de douleur ») ou saisie directe dans les fichiers Markdown.

## Étape 1 — Préparer la revue de phase

1. Ouvrir la synthèse des phases (`refs/phases_taches.md`) et la transcription détaillée (`refs/Phases_MOE_VRD.md`).
2. Pour la phase étudiée, lister les tâches connues en créant des fiches avec l'assistant :
   ```bash
   ./scripts/create_task_sheet.py
   ```
3. Si certaines tâches ne sont pas encore formalisées, utiliser la fiche générique (`refs/modele_fiche_tache.md`) pour prendre quelques notes rapides.

## Étape 2 — Identifier les irritants

Pour chaque tâche :

- Décrire les incidents récents (retards, erreurs, reprises de plans, incompréhensions avec le MOA).
- Quantifier l'effort : temps passé, nombre d'intervenants, fréquence.
- Noter les dépendances critiques (données manquantes, validations externes).

Recommandation : réaliser un mini atelier (30 min) après chaque phase ou projet type, en répondant à trois questions :

1. **Qu'est-ce qui a pris trop de temps ?**
2. **Quelles erreurs ou oublis récurrents ?**
3. **Qu'est-ce qui pourrait être préparé automatiquement ?**

## Étape 3 — Coter la douleur

Attribuer pour chaque tâche une note (1 à 5) sur :

- **Fréquence** : à quelle fréquence la tâche revient.
- **Durée** : temps moyen consommé.
- **Impact** : conséquences en cas d'erreur (technique, client, financière).
- **Stress / complexité** : difficulté perçue.

Insérer ces informations dans la section « Points de douleur actuels » de la fiche.

## Étape 4 — Synthèse par phase

Créer un tableau récapitulatif par phase (exemple dans `refs/phases_taches.md`) :

| Tâche | Fréquence | Douleur (1-5) | Commentaire | Idée d'automatisation |
| --- | --- | --- | --- | --- |
| Vérification réseau concessionnaires | 5 | 4 | Retours tardifs, re-saisie | Checklist + relance automatique |

Ce tableau peut être intégré soit à la fin de `refs/phases_taches.md`, soit dans un fichier dédié (ex : `refs/phase_AVP_points_douleur.md`).

## Étape 5 — Prioriser

- Classer les tâches avec les scores les plus élevés.
- Vérifier quels outils sont déjà disponibles (scripts, gabarits).
- Planifier la création du prototype d'automatisation (entrée dans `refs/todo.md`).

## Bonnes pratiques

- Garder la trace de la date et des participants à chaque revue.
- Joindre les documents sources (CR de chantier, mails) si l'information est utile.
- Mettre à jour le plan de développement après chaque séance.
