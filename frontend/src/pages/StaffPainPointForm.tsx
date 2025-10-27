import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";
import { createPainPoint } from "../api/painPoints";
import { PHASE_OPTIONS, SCORE_OPTIONS } from "../constants/formOptions";

export default function StaffPainPointForm() {
  const navigate = useNavigate();
  const [phase, setPhase] = useState(PHASE_OPTIONS[0]);
  const [task, setTask] = useState("");
  const [description, setDescription] = useState("");
  const [frequency, setFrequency] = useState(SCORE_OPTIONS[0]);
  const [duration, setDuration] = useState(SCORE_OPTIONS[0]);
  const [impact, setImpact] = useState(SCORE_OPTIONS[0]);
  const [stress, setStress] = useState(SCORE_OPTIONS[0]);
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
      const trimmedDescription = description.trim();
      if (trimmedDescription.length < 10) {
        throw new Error("La description doit comporter au moins 10 caractères.");
      }

      const payload = {
        phase,
        task: task.trim(),
        description: trimmedDescription,
        frequency,
        duration,
        impact,
        stress,
        automation_idea: automationIdea.trim(),
        comments: comments.trim()
      };
      const result = await createPainPoint(payload);
      setMessage(`Point de douleur enregistré : ${result.path}`);
      setPhase(PHASE_OPTIONS[0]);
      setTask("");
      setDescription("");
      setFrequency(SCORE_OPTIONS[0]);
      setDuration(SCORE_OPTIONS[0]);
      setImpact(SCORE_OPTIONS[0]);
      setStress(SCORE_OPTIONS[0]);
      setAutomationIdea("");
      setComments("");
      setTimeout(() => navigate("/staff/dashboard"), 1800);
    } catch (err) {
      console.error(err);
      setError(err instanceof Error ? err.message : "Impossible d'enregistrer le point de douleur.");
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
          <select value={phase} onChange={(e) => setPhase(e.target.value)} required>
            {PHASE_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
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
          <select value={frequency} onChange={(e) => setFrequency(Number(e.target.value))} required>
            {SCORE_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>
        <label>
          Durée / charge (1-5)
          <select value={duration} onChange={(e) => setDuration(Number(e.target.value))} required>
            {SCORE_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>
        <label>
          Impact (1-5)
          <select value={impact} onChange={(e) => setImpact(Number(e.target.value))} required>
            {SCORE_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>
        <label>
          Stress / complexité (1-5)
          <select value={stress} onChange={(e) => setStress(Number(e.target.value))} required>
            {SCORE_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
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
