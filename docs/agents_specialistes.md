# Agents spécialistes — MOE VRD Automatisation

Chaque fiche tâche (préfixe `2025-10-27-`) inspire un agent spécialisé. Les informations ci-dessous servent de base pour définir leurs responsabilités, les informations qu’ils consomment et les livrables attendus.

| Agent | Fiche source | Phase MOE | Objectif principal | Domaine / périmètre |
| --- | --- | --- | --- | --- |
| **Agent Architecture Fonctionnelle** | 2025-10-27-architecture-fonctionnelle-du-projet.md | AVP | Définir les blocs fonctionnels et leurs interactions | Modélisation, documentation YAML/JSON, schémas fonctionnels |
| **Agent Gestion du Cahier des Charges** | 2025-10-27-definition-du-besoin-cahier-des-charges.md | AVP | Formaliser le besoin et le cahier des charges | Collecte d’informations, génération Markdown/Word |
| **Agent Charte Graphique** | 2025-10-27-mise-a-la-charte-graphique.md | AVP | Uniformiser calques et conventions BE | Lint DWG/DXF, scripts AutoCAD |
| **Agent Données d’Entrées** | 2025-10-27-mise-au-norme-des-donnes-dentres.md | AVP | Mettre à jour/normaliser les plans sources | Harmonisation données, conversions, checklists |
| **Agent Gestion de Projet & Versionning** | 2025-10-27-gestion-de-projet-et-versionning.md | Toutes phases | Suivre versions et actions automatiques | Git, Notion, suivi des tâches |
| **Agent Calculs VRD** | 2025-10-27-calculs-vrd.md | AVP | Calculer surfaces, volumes, métrés | Interfaces calculs VRD, extraction quantités |
| **Agent Données Terrain** | 2025-10-27-gestion-des-donnees-de-terrain.md | AVP | Gérer les levés et profils | Import DXF, profils en long et travers |
| **Agent SIG** | 2025-10-27-integration-sig.md | AVP | Intégrer les couches géographiques | Imports/exports SIG, synchronisation base projet |
| **Agent Données Publiques** | 2025-10-27-integration-de-donnees-publiques.md | AVP | Ingérer données ouvertes (cadastre, PLU…) | Connexion APIs publiques, enrichissement |
| **Agent Calcul Budgétaire** | 2025-10-27-cout-et-budgetisation-automatique.md | PRO / DCE | Estimer automatiquement les coûts | Base de prix, métrés, simulation financière |
| **Agent Reporting & Livrables** | 2025-10-27-generation-de-rapports-et-livrables.md | PRO / DCE | Industrialiser la production des rapports | Templates Word/PDF, assemblage automatique |
| **Agent Compte rendu** | 2025-10-27-compte-rendu-de-reunion.md | PRO / EXE | Générer des CR à partir des notes/audio | Résumés automatiques, traçabilité décisions |
| **Agent Coordination** | 2025-10-27-coordination-et-communication.md | EXE | Faciliter l’échange et le suivi actions | Emails, tableaux de bord, notifications |
| **Agent Normes & Conformité** | 2025-10-27-verification-normative.md | AVP | Contrôler la conformité aux normes | Règles métier, rapport d’écart |
| **Agent Pilotage distant** | 2025-10-27-pilotage-a-distance-slack-webhook.md | Support | Permettre le pilotage via Slack/Webhook | Intégrations externes, déclencheurs distants |
| **Agent QA API** | 2025-10-27-test-api-fiche.md | AVP | Valider la création via API | Tests automatisés des endpoints |

## Notes

- Tous les agents sont actuellement en priorité *Haute* et statut *À lancer* (voir fiche).  
- Chaque fiche précise les “Points de douleur” et “Pistes d’automatisation” à implémenter.  
- Pour chaque agent, on préparera un dossier `docs/agents/<agent>.md` détaillant : inputs/outputs, dépendances, règles de décision, prompts à employer.  
- Ces agents seront orchestrés par l’agent de dispatch décrit dans `docs/agents_architecture.md`.

*Mise à jour : 2025-10-27*
