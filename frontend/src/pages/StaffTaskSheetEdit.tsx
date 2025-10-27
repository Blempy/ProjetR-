import { FormEvent, useEffect, useMemo, useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import {
  fetchTaskSheetDetail,
  updateTaskSheet
} from "../api/taskSheets";
import {
  PHASE_OPTIONS,
  PRIORITY_OPTIONS,
  STATUS_OPTIONS,
  FREQUENCY_OPTIONS
} from "../constants/formOptions";
import { joinLines, splitLines } from "../utils/text";

function ensureOption(options: string[], value: string): string[] {
  if (!value || options.includes(value)) {
    return options;
  }
  return [...options, value];
}

function todayISO(): string {
  return new Date().toISOString().slice(0, 10);
}

export default function StaffTaskSheetEdit() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const requestedPath = searchParams.get("path");

  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);

  const [pathValue, setPathValue] = useState("");
  const [lastUpdated, setLastUpdated] = useState("");

  const [phase, setPhase] = useState("");
  const [taskName, setTaskName] = useState("");
  const [responsable, setResponsable] = useState("");
  const [frequency, setFrequency] = useState("");
  const [duration, setDuration] = useState("");
  const [objective, setObjective] = useState("");
  const [trigger, setTrigger] = useState("");
  const [steps, setSteps] = useState("");
  const [dataNeeded, setDataNeeded] = useState("");
  const [docsNeeded, setDocsNeeded] = useState("");
  const [toolsNeeded, setToolsNeeded] = useState("");
  const [outputs, setOutputs] = useState("");
  const [formats, setFormats] = useState("");
  const [recipients, setRecipients] = useState("");
  const [pains, setPains] = useState("");
  const [automationIdeas, setAutomationIdeas] = useState("");
  const [automationType, setAutomationType] = useState("");
  const [automationPrereq, setAutomationPrereq] = useState("");
  const [automationEffort, setAutomationEffort] = useState("");
  const [automationBenefits, setAutomationBenefits] = useState("");
  const [priority, setPriority] = useState("");
  const [status, setStatus] = useState("");
  const [nextAction, setNextAction] = useState("");
  const [linkedDocs, setLinkedDocs] = useState("");

  useEffect(() => {
    if (!requestedPath) {
      setError("Chemin de fiche manquant.");
      setLoading(false);
      return;
    }

    setLoading(true);
    fetchTaskSheetDetail(requestedPath)
      .then((detail) => {
        setPathValue(detail.path);
        setLastUpdated(detail.last_updated);
        setPhase(detail.phase);
        setTaskName(detail.task_name);
        setResponsable(detail.responsable ?? "");
        setFrequency(detail.frequency ?? "");
        setDuration(detail.duration ?? "");
        setObjective(detail.objective ?? "");
        setTrigger(detail.trigger ?? "");
        setSteps(joinLines(detail.steps));
        setDataNeeded(joinLines(detail.data_needed));
        setDocsNeeded(joinLines(detail.docs_needed));
        setToolsNeeded(joinLines(detail.tools_needed));
        setOutputs(joinLines(detail.outputs));
        setFormats(joinLines(detail.formats));
        setRecipients(joinLines(detail.recipients));
        setPains(joinLines(detail.pains));
        setAutomationIdeas(joinLines(detail.automation_ideas));
        setAutomationType(detail.automation_type ?? "");
        setAutomationPrereq(detail.automation_prereq ?? "");
        setAutomationEffort(detail.automation_effort ?? "");
        setAutomationBenefits(joinLines(detail.automation_benefits));
        setPriority(detail.priority ?? "");
        setStatus(detail.status ?? "");
        setNextAction(detail.next_action ?? "");
        setLinkedDocs(joinLines(detail.linked_docs));
        setError(null);
      })
      .catch((err) => {
        console.error(err);
        setError("Impossible de charger la fiche demandée.");
      })
      .finally(() => setLoading(false));
  }, [requestedPath]);

  const phaseOptions = useMemo(() => ensureOption(PHASE_OPTIONS, phase), [phase]);
  const priorityOptions = useMemo(() => ensureOption(PRIORITY_OPTIONS, priority), [priority]);
  const statusOptions = useMemo(() => ensureOption(STATUS_OPTIONS, status), [status]);
  const frequencyOptions = useMemo(() => ensureOption(FREQUENCY_OPTIONS, frequency), [frequency]);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError(null);
    setMessage(null);

    if (!pathValue) {
      setError("Chemin de fiche introuvable.");
      return;
    }
    if (!taskName.trim()) {
      setError("Le nom de la tâche est obligatoire.");
      return;
    }
    if (!objective.trim()) {
      setError("Merci de préciser l'objectif de la fiche.");
      return;
    }

    setSaving(true);
    try {
      await updateTaskSheet({
        path: pathValue,
        phase: phase.trim(),
        task_name: taskName.trim(),
        responsable: responsable,
        frequency: frequency,
        duration: duration,
        objective: objective.trim(),
        trigger: trigger,
        steps: splitLines(steps),
        data_needed: splitLines(dataNeeded),
        docs_needed: splitLines(docsNeeded),
        tools_needed: splitLines(toolsNeeded),
        outputs: splitLines(outputs),
        formats: splitLines(formats),
        recipients: splitLines(recipients),
        pains: splitLines(pains),
        automation_ideas: splitLines(automationIdeas),
        automation_type: automationType,
        automation_prereq: automationPrereq,
        automation_effort: automationEffort,
        automation_benefits: splitLines(automationBenefits),
        priority: priority,
        status: status,
        next_action: nextAction,
        linked_docs: splitLines(linkedDocs)
      });
      setMessage("Fiche mise à jour avec succès.");
      setLastUpdated(todayISO());
    } catch (err) {
      console.error(err);
      setError(
        err instanceof Error ? err.message : "Impossible d'enregistrer la fiche."
      );
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return (
      <div className="page">
        <p>Chargement de la fiche…</p>
      </div>
    );
  }

  if (error && !pathValue) {
    return (
      <div className="page">
        <p className="error">{error}</p>
        <button type="button" className="secondary" onClick={() => navigate("/staff/task-sheets")}>
          Retour
        </button>
      </div>
    );
  }

  return (
    <div className="page">
      <h2>Modifier une fiche tâche</h2>
      {pathValue && (
        <p>
          <strong>Chemin :</strong> <code>{pathValue}</code>
        </p>
      )}
      {lastUpdated && (
        <p>
          <strong>Dernière mise à jour :</strong> {lastUpdated}
        </p>
      )}
      {error && <p className="error">{error}</p>}
      {message && <p className="success">{message}</p>}
      <form onSubmit={handleSubmit} className="card form">
        <fieldset>
          <legend>Informations générales</legend>
          <label>
            Phase MOE
            <select value={phase} onChange={(e) => setPhase(e.target.value)} required>
              {phaseOptions.map((option) => (
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
            Responsable / intervenants
            <input value={responsable} onChange={(e) => setResponsable(e.target.value)} />
          </label>
          <label>
            Fréquence
            <select value={frequency} onChange={(e) => setFrequency(e.target.value)}>
              {frequencyOptions.map((option) => (
                <option key={option} value={option}>
                  {option}
                </option>
              ))}
            </select>
          </label>
          <label>
            Durée estimée
            <input value={duration} onChange={(e) => setDuration(e.target.value)} />
          </label>
          <label>
            Priorité
            <select value={priority} onChange={(e) => setPriority(e.target.value || "")}>
              {priorityOptions.map((option) => (
                <option key={option} value={option}>
                  {option}
                </option>
              ))}
            </select>
          </label>
          <label>
            Statut
            <select value={status} onChange={(e) => setStatus(e.target.value || "")}>
              {statusOptions.map((option) => (
                <option key={option} value={option}>
                  {option}
                </option>
              ))}
            </select>
          </label>
          <label>
            Prochaine action
            <input value={nextAction} onChange={(e) => setNextAction(e.target.value)} />
          </label>
        </fieldset>

        <fieldset>
          <legend>Description</legend>
          <label>
            Objectif
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
        </fieldset>

        <fieldset>
          <legend>Entrées nécessaires</legend>
          <label>
            Données (une par ligne)
            <textarea value={dataNeeded} onChange={(e) => setDataNeeded(e.target.value)} rows={3} />
          </label>
          <label>
            Documents de référence
            <textarea value={docsNeeded} onChange={(e) => setDocsNeeded(e.target.value)} rows={3} />
          </label>
          <label>
            Logiciels / outils
            <textarea value={toolsNeeded} onChange={(e) => setToolsNeeded(e.target.value)} rows={3} />
          </label>
        </fieldset>

        <fieldset>
          <legend>Sorties attendues</legend>
          <label>
            Livrables
            <textarea value={outputs} onChange={(e) => setOutputs(e.target.value)} rows={3} />
          </label>
          <label>
            Formats
            <textarea value={formats} onChange={(e) => setFormats(e.target.value)} rows={3} />
          </label>
          <label>
            Destinataires / diffusion
            <textarea value={recipients} onChange={(e) => setRecipients(e.target.value)} rows={3} />
          </label>
        </fieldset>

        <fieldset>
          <legend>Points de douleur & automatisations</legend>
          <label>
            Points de douleur (une par ligne)
            <textarea value={pains} onChange={(e) => setPains(e.target.value)} rows={4} />
          </label>
          <label>
            Idées d'automatisation
            <textarea value={automationIdeas} onChange={(e) => setAutomationIdeas(e.target.value)} rows={4} />
          </label>
          <label>
            Type d'automatisation
            <input value={automationType} onChange={(e) => setAutomationType(e.target.value)} />
          </label>
          <label>
            Pré-requis
            <input value={automationPrereq} onChange={(e) => setAutomationPrereq(e.target.value)} />
          </label>
          <label>
            Niveau d'effort
            <input value={automationEffort} onChange={(e) => setAutomationEffort(e.target.value)} />
          </label>
          <label>
            Bénéfices attendus
            <textarea value={automationBenefits} onChange={(e) => setAutomationBenefits(e.target.value)} rows={3} />
          </label>
        </fieldset>

        <fieldset>
          <legend>Documents liés</legend>
          <label>
            Documents liés (une entrée par ligne)
            <textarea value={linkedDocs} onChange={(e) => setLinkedDocs(e.target.value)} rows={3} />
          </label>
        </fieldset>

        <div className="form-actions">
          <button type="submit" disabled={saving}>
            {saving ? "Enregistrement..." : "Mettre à jour"}
          </button>
          <button
            type="button"
            className="secondary"
            onClick={() => navigate("/staff/task-sheets")}
          >
            Retour
          </button>
        </div>
      </form>
    </div>
  );
}
