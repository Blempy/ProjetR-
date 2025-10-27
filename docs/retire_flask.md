# Plan de retrait progressif de l'application Flask

Objectif : arrêter proprement l’ancienne interface Flask (`app.py` + `templates/` + `static/`) au profit de la stack FastAPI + React, tout en garantissant la continuité des fonctionnalités.

## 1. Cartographie des fonctionnalités actuelles

| Fonctionnalité | État côté Flask | État côté FastAPI/React | Action |
| --- | --- | --- | --- |
| Création de fiche tâche | Formulaire HTML (staff + public) | Portail staff (`/staff/task-sheets/new`) | ✅ Remplacer les liens vers Flask par React |
| Points de douleur | Formulaire HTML | Portail staff (`/staff/pain-points/new`) | ✅ |
| Page d’accueil générale | Page statique | Page d’accueil React (`/`) | ✅ |

> Restent à migrer : formulaires « utilisateur final » (notes de calcul, points de douleur public) et tout autre contenu spécifique qui vivait dans Flask.

## 2. Étapes de migration restante

1. **Inventorier les routes Flask** (preview voir `app.py`) pour vérifier qu’aucune fonctionnalité essentielle n’est oubliée.
2. **Porter les formulaires utilisateur** (non staff) dans React.
3. **Mettre à jour la documentation** (`README.md`, `refs/`) pour pointer uniquement vers FastAPI/React.
4. **Informer sur la nouvelle procédure** : scripts CLI → API (optionnel).

## 3. Retrait technique

1. Supprimer/archiver `app.py`, le dossier `templates/` et `static/` après confirmation.
2. Nettoyer `requirements.txt` (supprimer dépendances Flask) et scripts associées.
3. Adapter les commandes de démarrage (`README.md`, docs internes).

## 4. Check-list avant suppression finale

- [ ] Les tests manuels (ou automatisés) sur le portal React couvrent les cas d’usage existants.
- [ ] Aucun flux utilisateur ne dépend plus de Flask (ex : raccourcis, docs, scripts).
- [ ] Commit/documentation validée.
- [ ] Archive éventuelle des templates historiques (si tu veux les conserver).

## 5. Suivi

- **Responsable** : Blempy / IA
- **Date cible envisagée** : à confirmer (après migration user portal)
- **Documents liés** : `docs/migration_fastapi_react.md`, `README.md`, `refs/todo.md`

---

*Dernière mise à jour : 2025-10-27*
