# Architecture des agents — MOE VRD Automatisation

## 1. Vue d’ensemble

```
Orchestrateur général
├── Agent d’accueil / front (dialogue utilisateur)
│   ├── Agent Clarification (reformulation)
│   └── Agent de compréhension du contexte (lecture docs)
├── Agent de sélection / dispatch (router vers spécialistes)
│   └── Agents spécialistes (VRD, SIG, Budget, etc.)
└── Agent Synthèse / Explicatif (réponse finale)
```
*(possibilité d’un “Observer” qui surveille les échanges et déclenche des clarifications)*

## 2. Rôles détaillés

| Agent | Rôle | Interactions |
|-------|------|--------------|
| **Agent d’accueil / front** | Interlocuteur principal, garde le ton, transmet. | Dialogue utilisateur, baton relais avec Clarification/Synthèse. |
| **Agent Clarification** | Reformule, détecte ambiguïtés, pose questions. | Interagit avec accueil + agent contexte. |
| **Agent de compréhension du contexte** | Va lire fiches/docs/todo, synthétise. | Fournit un résumé actionable aux autres. |
| **Agent de sélection / dispatch** | Choisit le(s) spécialiste(s) pertinent(s), gère l’ordre. | Reçoit demande clarifiée + contexte, dialogue avec spécialistes. |
| **Agents spécialistes** (Architecture, SIG, VRD, Budget, etc.) | Comprennent leur domaine, proposent plan d’action. | Coopèrent d’un agent à l’autre, renvoient vers Synthèse. |
| **Agent Synthèse / Explicatif** | Agrège, explique la réponse finale. | Rassemble les sorties et répond via agent d’accueil. |
| **Agent Observateur** (optionnel) | Surveille cohérence, escalade si besoin. | Parle à orchestrateur ou à l’accueil. |

## 3. Choix de stack

- **Phase 1** : intégrer les agents dans la stack FastAPI existante (modules Python + orchestrateur).  
- **Phase 2** (option) : séparer si besoin (microservice ou framework d’agents).
- **Front** : React continue de dialoguer avec l’orchestrateur via endpoints/WebSocket.

## 4. Prochaines étapes

1. Valider/ajuster la liste d’agents spécialistes (liée aux fiches 2025-10-27-…).  
2. Décrire pour chaque agent : responsabilités, inputs/outputs, triggers.  
3. Définir les flux de communication (séquence type).  
4. Concevoir la structure technique (classes, prompts) et templates d’échange.  
5. Implémenter progressivement : orchestrateur minimal, agent contexte, premier spécialiste.

---

*Mise à jour : 2025-10-27 — structure initiale validée par Blempy. Ajuster à mesure des besoins.*
