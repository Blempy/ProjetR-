import { FormEvent, useState } from "react";
import { createPainPoint } from "../api/painPoints";
import { PHASE_OPTIONS, SCORE_OPTIONS } from "../constants/formOptions";

export default function UserPainPointForm() {
  const [phase, setPhase] = useState(PHASE_OPTIONS[0]);
  const [task, setTask] = useState("");
  const [description, setDescription] = useState("");
  const [frequency, setFrequency] = useState(3);
  const [duration, setDuration] = useState(3);
  const [impact, setImpact] = useState(3);
  const [stress, setStress] = useState(3);
  const [automationIdea, setAutomationIdea] = useState("");
  const [comments, setComments] = useState("");
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

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
      setFrequency(3);
      setDuration(3);
      setImpact(3);
      setStress(3);
      setAutomationIdea("");
      setComments("");
    } catch (err) {
      console.error(err);
      setError(
        err instanceof Error ? err.message : "Erreur lors de l'enregistrement."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <h2>Déclarer un point de douleur</h2>
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
          {loading ? "Envoi..." : "Soumettre"}
        </button>
      </form>
    </div>
  );
}
