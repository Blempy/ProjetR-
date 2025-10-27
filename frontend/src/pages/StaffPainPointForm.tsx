import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";
import { createPainPoint } from "../api/painPoints";

export default function StaffPainPointForm() {
  const navigate = useNavigate();
  const [phase, setPhase] = useState("");
  const [task, setTask] = useState("");
  const [description, setDescription] = useState("");
  const [frequency, setFrequency] = useState(1);
  const [duration, setDuration] = useState(1);
  const [impact, setImpact] = useState(1);
  const [stress, setStress] = useState(1);
  const [automationIdea, setAutomationIdea] = useState("");
  const [comments, setComments] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError(null);
    setMessage(null);
    setLoading(true);

    try {
      const payload = {
        phase,
        task,
        description,
        frequency,
        duration,
        impact,
        stress,
        automation_idea: automationIdea,
        comments
      };
      const result = await createPainPoint(payload);
      setMessage(`Point de douleur enregistré : ${result.path}`);
      setTimeout(() => navigate("/staff/dashboard"), 1800);
    } catch (err) {
      console.error(err);
      setError("Impossible d'enregistrer le point de douleur.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <h2>Nouveau point de douleur</h2>
      <form onSubmit={handleSubmit} className="card form">
        <label>
          Phase
          <input value={phase} onChange={(e) => setPhase(e.target.value)} required />
        </label>
        <label>
          Tâche concernée
          <input value={task} onChange={(e) => setTask(e.target.value)} required />
        </label>
        <label>
          Description
          <textarea value={description} onChange={(e) => setDescription(e.target.value)} rows={3} required />
        </label>
        <label>
          Fréquence (1-5)
          <input
            type="number"
            min={1}
            max={5}
            value={frequency}
            onChange={(e) => setFrequency(Number(e.target.value))}
            required
          />
        </label>
        <label>
          Durée / charge (1-5)
          <input
            type="number"
            min={1}
            max={5}
            value={duration}
            onChange={(e) => setDuration(Number(e.target.value))}
            required
          />
        </label>
        <label>
          Impact (1-5)
          <input
            type="number"
            min={1}
            max={5}
            value={impact}
            onChange={(e) => setImpact(Number(e.target.value))}
            required
          />
        </label>
        <label>
          Stress / complexité (1-5)
          <input
            type="number"
            min={1}
            max={5}
            value={stress}
            onChange={(e) => setStress(Number(e.target.value))}
            required
          />
        </label>
        <label>
          Idée d'automatisation
          <input value={automationIdea} onChange={(e) => setAutomationIdea(e.target.value)} />
        </label>
        <label>
          Commentaires
          <textarea value={comments} onChange={(e) => setComments(e.target.value)} rows={2} />
        </label>

        {error && <p className="error">{error}</p>}
        {message && <p className="success">{message}</p>}

        <button type="submit" disabled={loading}>
          {loading ? "Enregistrement..." : "Enregistrer"}
        </button>
        <button
          type="button"
          className="secondary"
          onClick={() => navigate("/staff/dashboard")}
        >
          Retour
        </button>
      </form>
    </div>
  );
}
