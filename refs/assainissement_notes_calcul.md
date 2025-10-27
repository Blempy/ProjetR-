# Notes de calcul — Assainissement EP (bassins de rétention & réseaux)

> Objectif : centraliser les formules, hypothèses et jeux de paramètres à utiliser pour l’automatisation de la fiche « Génération automatisée des notes de calcul d’assainissement ».

## 1. Hypothèses générales

- **Méthode de calcul** : méthode rationnelle pour le dimensionnement préliminaire, complétée par le calcul de volume de rétention.
- **Pluies de projet** :
  - Intensité `i` définie via la loi de Montana `i = a / (t + b)^c` (données à confirmer auprès des services météo / PLU).
  - Durée de pluie de référence : égale au temps de concentration du bassin versant ou valeur réglementaire.
- **Coefficients de ruissellement `C`** :
  - Table de valeurs indicatives à maintenir dans un onglet de référence (voir §2).
  - Ajustement selon les exigences du maître d’ouvrage / règlement local.
- **Débit de fuite autorisé** : valeur imposée par la collectivité (souvent en l/s/ha). À stocker dans la bibliothèque des paramètres.
- **Marges de sécurité** : appliquer un coefficient de sécurité (ex. +10 %) si exigé par la maîtrise d’ouvrage.

## 2. Coefficients de ruissellement (valeurs indicatives)

| Type de surface | Coefficient `C` proposé | Source / remarque |
| --- | --- | --- |
| Chaussée en enrobé | 0,90 – 0,95 | Fascicule 70 – à confirmer |
| Surface piétonne béton | 0,85 – 0,90 |  |
| Parkings pavés drainants | 0,45 – 0,60 | Dépend de la perméabilité |
| Espaces verts / sols perméables | 0,10 – 0,30 | Selon pente / nature du sol |
| Toitures terrasses | 0,80 – 0,90 |  |

> Action : compléter ce tableau avec les valeurs internes validées et les références bibliographiques.

## 3. Formules clés

### Débit de pointe (méthode rationnelle)

```
Q = C × i × A
```

- `Q` : débit (m³/s)
- `C` : coefficient de ruissellement
- `i` : intensité de pluie (mm/h → convertir en m/s)
- `A` : surface contributive (ha → convertir en m²)

### Volume de rétention requis

```
V = (Qin - Qfuite) × tc
```

- `Qin` : débit entrant (issu de la méthode rationnelle)
- `Qfuite` : débit de fuite autorisé (m³/s)
- `tc` : temps de vidange considéré (s)

> À adapter si la collectivité impose une durée spécifique ou une méthode volumétrique (méthode des pluviogrammes).

### Dimensionnement hydraulique du réseau

- Vérification des diamètres via la relation de Manning-Strickler :

```
Q = (1/n) × A × R^(2/3) × S^(1/2)
```

où :
- `n` : coefficient de rugosité (ex. 0,013 pour PVC),
- `A` : section pleine (m²),
- `R` : rayon hydraulique,
- `S` : pente du collecteur.

- Contrôle des vitesses : `v = Q / A` → vérifier min 0,6 m/s, max 3 m/s (à ajuster selon norme).

## 4. Données à préparer dans le modèle Excel/Word

1. **Onglet “Paramètres”** : pluies de référence, coefficients de ruissellement, débit de fuite autorisé, rugosité des matériaux.
2. **Onglet “Surfaces”** : export AutoCAD/Covadis (surface, type, coefficient affecté).
3. **Onglet “Collecteurs”** : longueur, pente, diamètre existant/proposé, débits calculés.
4. **Synthèse** : tableau récapitulatif (débits par tronçon, volume du bassin, contrôle des vitesses).
5. **Note Word** : texte type + tableaux importés depuis Excel (liaison automatique).

## 5. Points d’attention pour l’automatisation

- Vérifier la cohérence des unités (mm/h → m/s, ha → m²).
- Consigner dans la note les hypothèses : coefficients utilisés, date de la pluie de référence, débit de fuite autorisé.
- Prévoir un historique des versions : date de calcul, auteur, paramétrage.
- Documenter les cas particuliers (présence de bassins multiples, infiltration, surverse).

## 6. Références

- Fascicule 70 — Titre II.
- DTU 60.11 — Réseaux d'évacuation.
- Guides techniques des collectivités locales (à référencer au cas par cas).
- Ouvrages d’hydrologie urbaine (ex. guide Certu).
- Exemples de notes de calcul (fichiers fournis) :
  - `refs/379910604-Verification-autocurage-xls.xls`
  - `refs/379910726-NOTE-CALCUL-Hydraulique-Caquot.xls`
  - `refs/384329471-Dim des-ea ux-use es-E xcel.xls`

## 7. Analyse des gabarits existants

### 7.1 `379910604-Verification-autocurage-xls.xls`

- Onglet unique « Vérification autocurage ».
- Sections :
  - Rappel des formules Manning-Strickler, calculs géométriques pour section circulaire partiellement remplie.
  - Tableau principal (lignes 16-18 et 37-39) avec les colonnes : DN, pente, Q dimensionné, Q pleine section, vitesses correspondantes, angle θ, niveaux 0,1D/0,2D, vitesses résiduelles.
  - Commentaires automatiques (« Q ps > Q dim. », « < 4 ») pour vérifier les critères.
- Utilisation : contrôle ponctuel de l’autocurage pour un collecteur donné. À intégrer dans la future note comme section de vérification.

### 7.2 `379910726-NOTE-CALCUL-Hydraulique-Caquot.xls`

- Onglet unique « note de calcul hydraulique » très orienté VRD EP.
- Entête descriptive (projet, commune) suivie de rappels de formules Caquot :
  - `Q = 1,2676 × A^0,7659 × C^1,2254 × I^0,3223`
  - `m = (4A/L^2)^0,30`, `Qc = Q × m`, `D = 0,30 × I^-0,1875 × Q^0,375`
  - Vitesse pleine section : `V = 31,748 × I^0,5 × D^0,67`.
- Tableau d’agrégation par bassin/collateur (lignes 10-19) avec surfaces, coefficients, longueurs, pentes, débits, diamètres calculés/adoptés, vitesses.
- Constitue un excellent modèle pour l’onglet « Collecteurs » et la synthèse du futur template.

### 7.3 `384329471-Dim des-ea ux-use es-E xcel.xls`

- Feuille principale « Eaux usées » structurée comme une mini-note :
  - Bloc « Données de l’étude » (type de collecteur, Ks, population, pente, consommation).
  - Bloc « Résultats » (débit moyen/pointe, diamètre théorique/commercial, conditions d’autocurage).
  - Vérifications successives (vitesse pleine section, h/D, etc.) basées sur des tableaux annexes (onglets 2-6 vides ici, probablement des tables lookup).
- Applicable pour formaliser la page de synthèse « Résultats + conformité » dans le modèle Word.

### Conclusions pour le futur modèle

- **Structure cible** :
  1. Onglet « Paramètres » (pluies, coefficients, données projet).
  2. Onglet « Bassins/Tronçons » (inspiré du tableau Caquot).
  3. Onglet « Autocurage » (grille dérivée du premier fichier, automatisée par calcul vs. seuils).
  4. Onglet « Synthèse » (données clefs et validation, reprise du style du troisième fichier).
- **Outputs** :
  - Export PDF standardisé (note + annexes).
  - Liaison possible vers un modèle Word (sections texte + insertion des tableaux Excel).

---

*Dernière mise à jour : 2025-10-27 — compléter au fur et à mesure des retours terrain.*

## 8. Architecture cible (draft 2025-10-27)

### 8.1 Vue d’ensemble

```
Frontend React (assistant EP)
  → API FastAPI /calcul-ep
      ├─ Ingestion paramètres (pluies, coefficients, débits)
      ├─ Calcul hydrologique (méthode rationnelle / Caquot)
      ├─ Vérification réseau (Manning, autocurage)
      ├─ Génération livrables (Excel + PDF + JSON résumé)
      └─ Registry versions (paramètres, hypothèses)
  → Stockage projet (exports/<projet>/EP_<date>)
```

### 8.2 Modules prévus

| Module | Description | Technologies envisagées |
| --- | --- | --- |
| **Assistant React** | Formulaire multi-étapes (Projet, Pluies, Surfaces, Collecteurs, Export). Gestion du tableau de surfaces et import CSV. | React + React Hook Form + Zustand/Context. |
| **API `/calcul-ep`** | Endpoint POST recevant le JSON de saisie, renvoyant résultats + chemins de livrables. | FastAPI, Pydantic. |
| **Engine hydrologique** | Fonctions Python pour calculs surfaces pondérées, débits (Rationnelle/Caquot), volumes, diamètres, vitesses. | NumPy léger ou pur Python. |
| **Paramètres de référence** | Service chargeant coefficients/pluies depuis `config/ep/*.json` (versionnés). | Pydantic, JSON/YAML. |
| **Génération Excel** | Template `templates/excel/note_ep.xlsx` renseigné via `openpyxl` (phase 1). | openpyxl / xlsxwriter. |
| **Export PDF** | Conversion Excel → PDF (LibreOffice headless) ou HTML → PDF (phase 2). | LibreOffice ou WeasyPrint. |
| **Journalisation** | Export JSON synthèse + entrée dans la mémoire orchestrateur. | JSON + contrôleur mémoire. |

### 8.3 Schéma de données (entrée API)

```json
{
  "project": {
    "name": "ZAC XYZ",
    "commune": "Ville",
    "reference": "EP-2025-001"
  },
  "rain": {
    "method": "montana",
    "a": 58.1,
    "b": 18.2,
    "c": 0.78,
    "return_period": "10 ans"
  },
  "surfaces": [
    {
      "label": "Chaussée principale",
      "area_m2": 4500,
      "coefficient": 0.9,
      "drains_to": "T1"
    }
  ],
  "collectors": [
    {
      "id": "T1",
      "length_m": 120,
      "slope_percent": 0.6,
      "diameter_existing_mm": 315,
      "connected_surfaces": ["Chaussée principale"],
      "roughness_n": 0.013
    }
  ],
  "constraints": {
    "discharge_limit_lps_ha": 5,
    "safety_factor": 1.1,
    "min_velocity_ms": 0.6,
    "max_velocity_ms": 3.0
  }
}
```

### 8.4 Calculs attendus

1. Agrégation surfaces pondérées (`A_effective = Σ area × coeff`).  
2. Intensité pluie via loi de Montana (en fonction du temps de concentration).  
3. Débit `Qin = C × i × A`.  
4. Débit de fuite `Qf = min(Qin, seuil collectivité)`.  
5. Volume bassin `(Qin - Qf) × tc`.  
6. Diamètre recommandé (Caquot + vérification Manning).  
7. Autocurage : vitesses, h/D, comparatif `Qps / Qdim`.  
8. Synthèse : conformité (OK/KO), hypothèses, marges.

### 8.5 Livrables générés

| Fichier | Contenu |
| --- | --- |
| `exports/<projet>/EP_<AAAA-MM-JJ>.xlsx` | Onglets Paramètres, Surfaces, Collecteurs, Autocurage, Synthèse. |
| `exports/<projet>/EP_<AAAA-MM-JJ>.json` | Résumé structuré des calculs (pour mémoire/orchestrateur). |
| `exports/<projet>/EP_<AAAA-MM-JJ>.pdf` | Optionnel (phase 2), version prête à diffusion. |

### 8.6 Roadmap proposée

1. **Sprint 1**  
   - Finaliser bibliothèques de paramètres (`config/ep/coefficients.json`, `pluies.json`).  
   - Créer le template Excel (onglets structurés, formules placeholders).  
   - Implémenter le moteur de calcul Python + tests unitaires.
2. **Sprint 2**  
   - Exposer l’API FastAPI (`POST /api/ep/calc`).  
   - Générer l’Excel et renvoyer JSON + fichier téléchargeable.  
   - Créer le formulaire React (saisie surfaces, constraints).  
3. **Sprint 3**  
   - Export PDF / liaison Word.  
   - Script d’import AutoCAD/Covadis vers JSON surfaces.  
  - Intégration orchestrateur (agent spécialiste EP) + mémoire cache.
