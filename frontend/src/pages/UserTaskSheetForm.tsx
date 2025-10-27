import { FormEvent, useState } from "react";
import { createTaskSheet } from "../api/taskSheets";
import { PHASE_OPTIONS, PRIORITY_OPTIONS, STATUS_OPTIONS } from "../constants/formOptions";

function splitLines(value: string): string[] {
  return value
    .split(/\r?\n/u)
    .map((line) => line.trim())
    .filter((line) => line.length > 0);
}

export default function UserTaskSheetForm() {
  const [phase, setPhase] = useState(PHASE_OPTIONS[0]);
  const [taskName, setTaskName] = useState("");
  const [objective, setObjective] = useState("");
  const [steps, setSteps] = useState("");
  const [status, setStatus] = useState(STATUS_OPTIONS[0]);
  const [priority, setPriority] = useState(PRIORITY_OPTIONS[1]);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError(null);
    setMessage(null);
    setLoading(true);

    try {
      const trimmedObjective = objective.trim();
      if (trimmedObjective.length < 10) {
        throw new Error("L'objectif doit comporter au moins 10 caractères.");
      }

      const payload = {
        phase,
        task_name: taskName.trim(),
        objective: trimmedObjective,
        steps: splitLines(steps),
        status,
        priority
      };
      const result = await createTaskSheet(payload);
      setMessage(`Fiche soumise. Chemin : ${result.path}`);
      setPhase(PHASE_OPTIONS[0]);
      setTaskName("");
      setObjective("");
      setSteps("");
      setStatus(STATUS_OPTIONS[0]);
      setPriority(PRIORITY_OPTIONS[1]);
    } catch (err) {
      console.error(err);
      setError(
        err instanceof Error ? err.message : "Erreur lors de l'enregistrement de la fiche."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <h2>Proposer une fiche tâche</h2>
      <form onSubmit={handleSubmit} className="card form">
        <label>
          Phase MOE
          <select value={phase} onChange={(e) => setPhase(e.target.value)} required>
            {PHASE_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>
        <label>
          Intitulé de la tâche
          <input value={taskName} onChange={(e) => setTaskName(e.target.value)} required />
        </label>
        <label>
          Objectif principal
          <textarea value={objective} onChange={(e) => setObjective(e.target.value)} rows={3} required />
        </label>
        <label>
          Étapes principales (une par ligne)
          <textarea value={steps} onChange={(e) => setSteps(e.target.value)} rows={4} />
        </label>
        <label>
          Statut suggéré
          <select value={status} onChange={(e) => setStatus(e.target.value)}>
            {STATUS_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>
        <label>
          Priorité suggérée
          <select value={priority} onChange={(e) => setPriority(e.target.value)}>
            {PRIORITY_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>

        {error && <p className="error">{error}</p>}
        {message && <p className="success">{message}</p>}

        <button type="submit" disabled={loading}>
          {loading ? "Envoi..." : "Soumettre"}
        </button>
      </form>
    </div>
  );
}
