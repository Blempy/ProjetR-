# Mémoire & contrôle des requêtes — Orchestrateur MOE VRD

> Version 0.1 — 2025-10-27 — Première ébauche pour limiter les appels LLM payants.

## 1. Rôle de l’agent contrôleur

| Élément | Description |
|---------|-------------|
| **Nom** | Agent Contrôleur / Mémoire (alias `memory_guard`) |
| **Position** | Intervient après l’agent d’accueil/clarification, avant le dispatch spécialiste. |
| **Objectif** | Déterminer si une demande utilisateur a déjà une réponse validée en base de connaissances locale ; sinon laisser passer vers le LLM. |
| **Bénéfices** | Réduction du coût API, cohérence des réponses, temps de traitement plus court pour les requêtes récurrentes. |

## 2. Flux décisionnel

1. **Réception de la demande** (`message.type = user_request` ou `follow_up`).  
2. Génération d’un embedding de la question (OpenAI `text-embedding-3-small`).  
3. Recherche de similarité cosine dans la table `responses` (seuil ≥ 0.85).  
4. - Si match :  
   - L’orchestrateur émet `next_agent = "memory_guard"` avec un `action` `respond_from_memory`.  
   - Le front/staff reçoit la réponse locale + métadonnées (source, score).  
   - Aucun appel LLM n’est fait.  
   - Historique enrichi d’un message `type = cached_response`.  
   - Optionnel : incrément du compteur d’usage.  
   -  
   - Si pas de match :  
     - L’orchestrateur continue le flux standard (`clarification` → `dispatch` → LLM).  
5. **Apprentissage** : lorsqu’un agent de synthèse (`caller = summary`, `message.type = response`) produit une réponse validée, l’orchestrateur enregistre question + réponse + contexte dans le store.

## 3. Structure des données

### Table `responses` (SQLite `data/agents_memory.db`)

| Colonne | Type | Description |
|---------|------|-------------|
| `id` | INTEGER PK | Identifiant interne |
| `key_hash` | TEXT | Hash SHA256 (phase + projet + question normalisée) |
| `question` | TEXT | Question originale (utilisateur) |
| `answer` | TEXT | Réponse synthétisée validée |
| `metadata` | TEXT (JSON) | Phase, projet, auteurs, score initial, tags |
| `embedding` | BLOB | Tableau float32 stocké via `array('f')` |
| `created_at` | TEXT | Timestamp ISO8601 |
| `usage_count` | INTEGER | Nombre de fois où l’entrée a servi |

Indices :  
- `CREATE INDEX idx_responses_key_hash ON responses(key_hash);`  
- `CREATE INDEX idx_responses_created_at ON responses(created_at);`

## 4. Logique de similarité

- Embedding de la requête : `OpenAI Embeddings API`.  
- Similarité cosine :
  ```
  sim = dot(u, v) / (||u|| * ||v||)
  ```
- Seuil par défaut : `0.85` (configurable).  
- En cas d’égalité, on choisit la réponse la plus récente (`created_at DESC`).  
- Si `sim >= 0.95`, on incrémente `usage_count + 2`, sinon +1.

## 5. Politique d’apprentissage

| Étape | Détails |
|-------|---------|
| **Acquisition** | Déclenchée lorsque `caller = summary` et `message.type = response`. |
| **Question sauvegardée** | Dernier message utilisateur (`context.history` speaker = "user"). |
| **Filtrage** | On évite de stocker les réponses contenant `<non valide>` / prompts incomplets. |
| **Révision** | Possibilité de marquer une réponse comme obsolète (future interface staff). |
| **Expiration** | Paramètres `max_age_days` (ex. 180) et `auto_prune=True` lors des lookups. |

## 6. Configuration

- Fichier `.env` :
  ```
  OPENAI_API_KEY=sk-...
  MEMORY_DB_PATH=data/agents_memory.db
  MEMORY_SIMILARITY_THRESHOLD=0.85
  ```
- Les paramètres sont exposés via `pydantic-settings` (module `backend/app/core/settings.py` à compléter si besoin).

## 7. Étapes suivantes

1. Implémenter le module Python `backend/app/agents/knowledge_base.py` (lookup/store).  
2. Ajouter un provider embeddings (`backend/app/agents/embeddings.py`).  
3. Connecter l’orchestrateur (`orchestrator.route`) au contrôleur de mémoire.  
4. Exposer une route staff pour auditer/supprimer les entrées (optionnel).  
5. Prévoir une UI dans l’espace staff (`/staff/memory`) pour visualiser/valider le cache.

---

*Document à réviser après mise en production initiale et retours utilisateurs.*
