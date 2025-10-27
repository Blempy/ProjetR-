# Frontend React — MOE VRD Automatisation

Projet React (Vite + TypeScript) servant trois espaces :
- Accueil général
- Portail utilisateur final (formulaires automatisations)
- Portail staff (gestion interne, nécessite authentification : création de fiches, points de douleur)
- Portail utilisateur (soumission publique avec contrôles : fiches, points de douleur)

## Installation

```
npm install
npm run dev
```

L’API FastAPI doit être disponible sur `http://127.0.0.1:8000` (proxy configuré dans `vite.config.ts`).

## Structure

- `src/App.tsx` : routes principales.
- `src/main.tsx` : point d’entrée React.
- Ajoutez des pages dans `src/pages/` et des composants partagés dans `src/components/` lors des futures itérations.

## TODO

- Formulaires dynamiques (notes de calcul)
- Interface staff (suivi fiches, points de douleur, todo)
- Interface utilisateur finale (tableaux, dashboards, validations)
