import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";
import { createTaskSheet } from "../api/taskSheets";
import { useAuth } from "../context/AuthContext";

function splitLines(value: string): string[] {
  return value
    .split(/\r?\n/u)
    .map((line) => line.trim())
    .filter((line) => line.length > 0);
}

export default function StaffTaskSheetForm() {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [phase, setPhase] = useState("");
  const [taskName, setTaskName] = useState("");
  const [responsable, setResponsable] = useState(user?.username ?? "");
  const [frequency, setFrequency] = useState("À chaque projet");
  const [duration, setDuration] = useState("");
  const [objective, setObjective] = useState("");
  const [trigger, setTrigger] = useState("");
  const [steps, setSteps] = useState("");
  const [pains, setPains] = useState("");
  const [priority, setPriority] = useState("Haute");
  const [status, setStatus] = useState("À lancer");
  const [nextAction, setNextAction] = useState("");
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
        responsable,
        frequency,
        duration,
        objective,
        trigger,
        steps: splitLines(steps),
        pains: splitLines(pains),
        priority,
        status,
        next_action: nextAction
      };
      const result = await createTaskSheet(payload);
      setMessage(`Fiche créée : ${result.path}`);
      setTimeout(() => navigate("/staff/dashboard"), 1800);
    } catch (err) {
      console.error(err);
      setError("Impossible de créer la fiche. Vérifiez les champs obligatoires.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <h2>Nouvelle fiche tâche</h2>
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
          Responsable / intervenants
          <input value={responsable} onChange={(e) => setResponsable(e.target.value)} />
        </label>
        <label>
          Fréquence
          <input value={frequency} onChange={(e) => setFrequency(e.target.value)} />
        </label>
        <label>
          Durée estimée
          <input value={duration} onChange={(e) => setDuration(e.target.value)} />
        </label>
        <label>
          Objectif principal
          <textarea value={objective} onChange={(e) => setObjective(e.target.value)} required rows={3} />
        </label>
        <label>
          Déclencheur
          <input value={trigger} onChange={(e) => setTrigger(e.target.value)} />
        </label>
        <label>
          Étapes principales (une par ligne)
          <textarea value={steps} onChange={(e) => setSteps(e.target.value)} rows={4} />
        </label>
        <label>
          Points de douleur (une par ligne)
          <textarea value={pains} onChange={(e) => setPains(e.target.value)} rows={4} />
        </label>
        <label>
          Priorité
          <input value={priority} onChange={(e) => setPriority(e.target.value)} />
        </label>
        <label>
          Statut
          <input value={status} onChange={(e) => setStatus(e.target.value)} />
        </label>
        <label>
          Prochaine action
          <input value={nextAction} onChange={(e) => setNextAction(e.target.value)} />
        </label>

        {error && <p className="error">{error}</p>}
        {message && <p className="success">{message}</p>}

        <button type="submit" disabled={loading}>
          {loading ? "Enregistrement..." : "Créer la fiche"}
        </button>
      </form>
    </div>
  );
}
