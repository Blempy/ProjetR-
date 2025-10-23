## Référentiel d'automatisation MOE VRD

Ce dossier rassemble toute la documentation de travail pour préparer et piloter l'automatisation des tâches de maîtrise d'œuvre (urbanisme, VRD, infrastructures).

Contenu actuel :

- `Phases_MOE_VRD_reformate.pdf` : référence des phases et tâches existantes (source fournie par le client).
- `Phases_MOE_VRD.md` : transcription markdown validée du PDF (référentiel phases/tâches).
- `phases_taches.md` : synthèse enrichie avec pistes d'automatisation par phase.
- `modele_fiche_tache.md` : gabarit à cloner pour documenter chaque tâche.
- `fiches_taches/` : fiches individuelles créées à partir du gabarit ou via le script/app web.
- `points_douleur/` : tableaux Markdown des irritants par phase (alimentés depuis le formulaire ou manuellement).
- `process_points_douleur.md` : méthode pour collecter et noter les irritants par phase.
- `plan_developpement.md` : feuille de route globale pour structurer les travaux.
- `todo.md` : liste des actions à lancer ou à suivre.

Scripts utiles :

- `scripts/create_task_sheet.py` : assistant interactif (ligne de commande) pour générer rapidement une fiche tâche dans `refs/fiches_taches/`.
- `app.py` : application web locale (Flask) proposant des formulaires pour créer les fiches et enregistrer les points de douleur.
- Atelier points de douleur : suivre `refs/process_points_douleur.md`.

Exécution :

```bash
# Assistant CLI
./scripts/create_task_sheet.py

# Application web locale (après installation des dépendances)
python3 app.py
```

Le script vous guidera question par question, puis créera un fichier Markdown dont le nom suit le format `AAAA-MM-JJ-intitule.md`.  
L'application web accessible sur <http://127.0.0.1:5000> propose les mêmes fonctionnalités via une interface graphique et enregistre directement les fichiers dans `refs/`.

Règles d'usage :

1. Garder les documents en Markdown pour faciliter la relecture et les mises à jour.
2. Documenter systématiquement les hypothèses et les décisions (date, auteur).
3. Lier chaque tâche planifiée à une phase et à un livrable attendu (script, modèle, rapport).
4. Mettre à jour le dossier à chaque avancée en suivant l'ordre : plan → tâches → preuves/références.
