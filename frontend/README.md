# Frontend React — MOE VRD Automatisation

Projet React (Vite + TypeScript) servant trois espaces :
- Accueil général
- Portail utilisateur final (formulaires automatisations)
- Portail staff (gestion interne, nécessite authentification)

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

- Formulaires dynamiques (notes de calcul, points de douleur)
- Interface staff (création fiches, todo)
- Interface utilisateur finale (tableaux, dashboards)
