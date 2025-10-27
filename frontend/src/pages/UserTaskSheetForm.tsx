import { FormEvent, useState } from "react";
import { createTaskSheet } from "../api/taskSheets";

function splitLines(value: string): string[] {
  return value
    .split(/\r?\n/u)
    .map((line) => line.trim())
    .filter((line) => line.length > 0);
}

export default function UserTaskSheetForm() {
  const [phase, setPhase] = useState("");
  const [taskName, setTaskName] = useState("");
  const [objective, setObjective] = useState("");
  const [steps, setSteps] = useState("");
  const [status, setStatus] = useState("À qualifier");
  const [priority, setPriority] = useState("À qualifier");
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError(null);
    setMessage(null);
    setLoading(true);

    try {
      const payload = {
        phase,
        task_name: taskName,
        objective,
        steps: splitLines(steps),
        status,
        priority
      };
      const result = await createTaskSheet(payload);
      setMessage(`Fiche soumise. Chemin : ${result.path}`);
      setPhase("");
      setTaskName("");
      setObjective("");
      setSteps("");
      setStatus("À qualifier");
      setPriority("À qualifier");
    } catch (err) {
      console.error(err);
      setError("Erreur lors de l'enregistrement de la fiche.");
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
          <input value={phase} onChange={(e) => setPhase(e.target.value)} required />
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
          <input value={status} onChange={(e) => setStatus(e.target.value)} />
        </label>
        <label>
          Priorité suggérée
          <input value={priority} onChange={(e) => setPriority(e.target.value)} />
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
