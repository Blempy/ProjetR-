import { FormEvent, useMemo, useState } from "react";
import {
  calculateEP,
  CollectorInput,
  ConstraintsInput,
  EPInputPayload,
  EPResult,
  ProjectInfo,
  RainParameters,
  SurfaceInput
} from "../api/ep";
import { useNavigate } from "react-router-dom";

const STEP_LABELS = ["Projet", "Pluies", "Surfaces", "Collecteurs", "Contraintes", "Récapitulatif"];

const DEFAULT_SURFACE: SurfaceInput = {
  label: "Chaussée principale",
  surface_m2: 0,
  coefficient: 0.9,
  drains_to: "T1"
};

const DEFAULT_COLLECTOR: CollectorInput = {
  id: "T1",
  length_m: 100,
  slope_percent: 0.5,
  roughness_n: 0.013
};

const DEFAULT_PROJECT: ProjectInfo = {
  name: "Projet EP",
  commune: "",
  reference: ""
};

const DEFAULT_RAIN: RainParameters = {
  method: "montana",
  a: 58.1,
  b: 18.2,
  c: 0.78,
  return_period: "10",
  safety_factor: 1.1
};

const DEFAULT_CONSTRAINTS: ConstraintsInput = {
  discharge_limit_lps_ha: 5,
  safety_factor: 1.1,
  min_velocity_ms: 0.6,
  max_velocity_ms: 3,
  minimum_tc_minutes: 10
};

function parseNumber(value: string): number {
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : 0;
}

export default function EPCalcForm() {
  const navigate = useNavigate();
  const [step, setStep] = useState(0);
  const [project, setProject] = useState<ProjectInfo>(DEFAULT_PROJECT);
  const [rain, setRain] = useState<RainParameters>(DEFAULT_RAIN);
  const [surfaces, setSurfaces] = useState<SurfaceInput[]>([DEFAULT_SURFACE]);
  const [collectors, setCollectors] = useState<CollectorInput[]>([DEFAULT_COLLECTOR]);
  const [constraints, setConstraints] = useState<ConstraintsInput>(DEFAULT_CONSTRAINTS);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<EPResult | null>(null);

  const mapQuery = useMemo(() => {
    const commune = project.commune?.trim();
    if (commune && commune.length > 2) {
      return commune;
    }
    const name = project.name.trim();
    return name.length > 0 ? name : null;
  }, [project]);
  const mapSrc = mapQuery ? `https://www.google.com/maps?q=${encodeURIComponent(mapQuery)}&output=embed` : null;

  const isLastStep = step === STEP_LABELS.length - 1;

  const payload = useMemo<EPInputPayload>(
    () => ({ project, rain, surfaces, collectors, constraints }),
    [project, rain, surfaces, collectors, constraints]
  );

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError(null);

    if (!isLastStep) {
      setStep((prev) => Math.min(prev + 1, STEP_LABELS.length - 1));
      return;
    }

    setLoading(true);
    try {
      const data = await calculateEP(payload);
      setResult(data);
    } catch (calcError) {
      console.error(calcError);
      setError(calcError instanceof Error ? calcError.message : "Erreur lors du calcul EP.");
    } finally {
      setLoading(false);
    }
  };

  const currentStepLabel = STEP_LABELS[step];

  const addSurface = () => setSurfaces((prev) => [...prev, { ...DEFAULT_SURFACE, label: `Surface ${prev.length + 1}` }]);
  const removeSurface = (index: number) => setSurfaces((prev) => prev.filter((_, i) => i !== index));

  const addCollector = () => setCollectors((prev) => [...prev, { ...DEFAULT_COLLECTOR, id: `T${prev.length + 1}` }]);
  const removeCollector = (index: number) => setCollectors((prev) => prev.filter((_, i) => i !== index));

  const handleSurfaceChange = (index: number, field: keyof SurfaceInput, value: string) => {
    setSurfaces((prev) => {
      const copy = [...prev];
      copy[index] = {
        ...copy[index],
        [field]: field === "label" || field === "drains_to" ? value : parseNumber(value)
      } as SurfaceInput;
      return copy;
    });
  };

  const handleCollectorChange = (index: number, field: keyof CollectorInput, value: string) => {
    setCollectors((prev) => {
      const copy = [...prev];
      if (field === "id") {
        copy[index] = { ...copy[index], id: value };
      } else if (field === "diameter_existing_mm") {
        const parsed = parseNumber(value);
        copy[index] = { ...copy[index], diameter_existing_mm: Number.isFinite(parsed) && parsed > 0 ? parsed : undefined };
      } else {
        copy[index] = { ...copy[index], [field]: parseNumber(value) } as CollectorInput;
      }
      return copy;
    });
  };

  const renderStep = () => {
    switch (step) {
      case 0:
        return (
          <div className="card form">
            <label>
              Nom du projet
              <input value={project.name} onChange={(e) => setProject({ ...project, name: e.target.value })} required />
            </label>
            <label>
              Commune
              <input value={project.commune ?? ""} onChange={(e) => setProject({ ...project, commune: e.target.value })} />
            </label>
            <label>
              Référence du projet
              <input value={project.reference ?? ""} onChange={(e) => setProject({ ...project, reference: e.target.value })} />
            </label>
            {mapSrc && (
              <div className="map-preview" style={{ marginTop: "1rem", marginBottom: "1.5rem" }}>
                <iframe
                  title="Carte commune"
                  src={mapSrc}
                  width="100%"
                  height="250"
                  style={{ border: 0 }}
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                />
              </div>
            )}
          </div>
        );
      case 1:
        return (
          <div className="card form">
            <label>
              Méthode de pluie
              <select value={rain.method} onChange={(e) => setRain({ ...rain, method: e.target.value })}>
                <option value="montana">Montana</option>
              </select>
            </label>
            <label>
              Paramètre a
              <input type="number" step="0.01" value={rain.a} onChange={(e) => setRain({ ...rain, a: parseNumber(e.target.value) })} required />
            </label>
            <label>
              Paramètre b
              <input type="number" step="0.01" value={rain.b} onChange={(e) => setRain({ ...rain, b: parseNumber(e.target.value) })} required />
            </label>
            <label>
              Paramètre c
              <input type="number" step="0.01" value={rain.c} onChange={(e) => setRain({ ...rain, c: parseNumber(e.target.value) })} required />
            </label>
            <label>
              Période de retour (années)
              <input value={rain.return_period} onChange={(e) => setRain({ ...rain, return_period: e.target.value })} required />
            </label>
            <label>
              Coefficient de sécurité
              <input
                type="number"
                step="0.01"
                value={rain.safety_factor}
                onChange={(e) => setRain({ ...rain, safety_factor: parseNumber(e.target.value) })}
                required
              />
            </label>
          </div>
        );
      case 2:
        return (
          <div className="card">
            <h3>Surfaces contributives</h3>
            {surfaces.map((surface, index) => (
              <div key={index} className="form-row">
                <label>
                  Libellé
                  <input value={surface.label} onChange={(e) => handleSurfaceChange(index, "label", e.target.value)} required />
                </label>
                <label>
                  Surface (m²)
                  <input
                    type="number"
                    min="0"
                    step="0.01"
                    value={surface.surface_m2}
                    onChange={(e) => handleSurfaceChange(index, "surface_m2", e.target.value)}
                    required
                  />
                </label>
                <label>
                  Coefficient C
                  <input
                    type="number"
                    min="0"
                    max="1"
                    step="0.01"
                    value={surface.coefficient}
                    onChange={(e) => handleSurfaceChange(index, "coefficient", e.target.value)}
                    required
                  />
                </label>
                <label>
                  Collecteur
                  <input value={surface.drains_to} onChange={(e) => handleSurfaceChange(index, "drains_to", e.target.value)} required />
                </label>
                {surfaces.length > 1 && (
                  <button type="button" className="secondary" onClick={() => removeSurface(index)}>
                    Supprimer
                  </button>
                )}
              </div>
            ))}
            <button type="button" className="secondary" onClick={addSurface}>
              Ajouter une surface
            </button>
          </div>
        );
      case 3:
        return (
          <div className="card">
            <h3>Collecteurs</h3>
            {collectors.map((collector, index) => (
              <div key={index} className="form-row">
                <label>
                  ID
                  <input value={collector.id} onChange={(e) => handleCollectorChange(index, "id", e.target.value)} required />
                </label>
                <label>
                  Longueur (m)
                  <input
                    type="number"
                    min="1"
                    step="0.1"
                    value={collector.length_m}
                    onChange={(e) => handleCollectorChange(index, "length_m", e.target.value)}
                    required
                  />
                </label>
                <label>
                  Pente (%)
                  <input
                    type="number"
                    min="0.01"
                    step="0.01"
                    value={collector.slope_percent}
                    onChange={(e) => handleCollectorChange(index, "slope_percent", e.target.value)}
                    required
                  />
                </label>
                <label>
                  Diamètre existant (mm)
                  <input
                    type="number"
                    min="0"
                    step="1"
                    value={collector.diameter_existing_mm ?? ""}
                    onChange={(e) => handleCollectorChange(index, "diameter_existing_mm", e.target.value)}
                  />
                </label>
                <label>
                  Rugosité n
                  <input
                    type="number"
                    min="0.001"
                    step="0.001"
                    value={collector.roughness_n}
                    onChange={(e) => handleCollectorChange(index, "roughness_n", e.target.value)}
                    required
                  />
                </label>
                {collectors.length > 1 && (
                  <button type="button" className="secondary" onClick={() => removeCollector(index)}>
                    Supprimer
                  </button>
                )}
              </div>
            ))}
            <button type="button" className="secondary" onClick={addCollector}>
              Ajouter un collecteur
            </button>
          </div>
        );
      case 4:
        return (
          <div className="card form">
            <label>
              Débit de fuite limite (l/s/ha)
              <input
                type="number"
                min="0"
                step="0.1"
                value={constraints.discharge_limit_lps_ha}
                onChange={(e) => setConstraints({ ...constraints, discharge_limit_lps_ha: parseNumber(e.target.value) })}
                required
              />
            </label>
            <label>
              Coefficient de sécurité hydraulique
              <input
                type="number"
                min="1"
                step="0.01"
                value={constraints.safety_factor}
                onChange={(e) => setConstraints({ ...constraints, safety_factor: parseNumber(e.target.value) })}
                required
              />
            </label>
            <label>
              Vitesse min (m/s)
              <input
                type="number"
                min="0"
                step="0.01"
                value={constraints.min_velocity_ms}
                onChange={(e) => setConstraints({ ...constraints, min_velocity_ms: parseNumber(e.target.value) })}
                required
              />
            </label>
            <label>
              Vitesse max (m/s)
              <input
                type="number"
                min="0"
                step="0.1"
                value={constraints.max_velocity_ms}
                onChange={(e) => setConstraints({ ...constraints, max_velocity_ms: parseNumber(e.target.value) })}
                required
              />
            </label>
            <label>
              Temps de concentration minimum (min)
              <input
                type="number"
                min="1"
                step="1"
                value={constraints.minimum_tc_minutes}
                onChange={(e) => setConstraints({ ...constraints, minimum_tc_minutes: parseNumber(e.target.value) })}
                required
              />
            </label>
          </div>
        );
      case 5:
        return (
          <div className="card">
            <h3>Récapitulatif</h3>
            <p>
              <strong>Projet :</strong> {project.name}
            </p>
            <p>
              <strong>Collecteurs :</strong> {collectors.map((c) => c.id).join(", ")}
            </p>
            <p>
              <strong>Surfaces :</strong> {surfaces.length}
            </p>
            <p>
              <strong>Période de retour :</strong> {rain.return_period} ans
            </p>
            <p>
              <strong>Débit de fuite :</strong> {constraints.discharge_limit_lps_ha} l/s/ha
            </p>
            <p>Cliquer sur « Lancer le calcul » pour générer les résultats et le fichier Excel.</p>
          </div>
        );
      default:
        return null;
    }
  };

  return (
    <div className="page">
      <h2>Note de calcul EP — Assistant</h2>
      <p>
        Étape {step + 1} / {STEP_LABELS.length} : {currentStepLabel}
      </p>
      <form onSubmit={handleSubmit} className="wizard">
        {renderStep()}

        {error && <p className="error">{error}</p>}
        {result && (
          <div className="card">
            <h3>Résultat</h3>
            <p>
              <strong>Volume total :</strong> {result.total_storage_volume_m3} m³
            </p>
            <p>
              <strong>Assumptions :</strong>
            </p>
            <ul>
              {result.assumptions.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
            <h4>Collecteurs</h4>
            <table className="list-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Surface (m²)</th>
                  <th>Q in (l/s)</th>
                  <th>Q fuite (l/s)</th>
                  <th>Volume (m³)</th>
                  <th>Diamètre (mm)</th>
                  <th>Autocurage</th>
                </tr>
              </thead>
              <tbody>
                {result.collectors.map((collector) => (
                  <tr key={collector.id}>
                    <td>{collector.id}</td>
                    <td>{collector.area_total_m2}</td>
                    <td>{collector.inflow_lps}</td>
                    <td>{collector.permitted_outflow_lps}</td>
                    <td>{collector.storage_volume_m3}</td>
                    <td>{collector.recommended_diameter_mm}</td>
                    <td>{collector.conforms_autoclean ? "OK" : "À contrôler"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
            <p>
              Fichier Excel généré :<code> {result.excel_path}</code>
            </p>
          </div>
        )}
        <div className="form-actions">
          <button type="button" className="secondary" onClick={() => navigate("/user")}>
            Retour portail
          </button>
          {step > 0 && (
            <button
              type="button"
              className="secondary"
              onClick={() => setStep((prev) => Math.max(prev - 1, 0))}
            >
              Précédent
            </button>
          )}
          <button type="submit" disabled={loading}>
            {loading ? "Calcul en cours..." : isLastStep ? "Lancer le calcul" : "Suivant"}
          </button>
        </div>
      </form>
    </div>
  );
}
