import { useEffect, useState } from "react";
import { fetchTaskSheets, TaskSheetListItem } from "../api/taskSheets";

export default function StaffTaskSheetList() {
  const [items, setItems] = useState<TaskSheetListItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetchTaskSheets()
      .then(setItems)
      .catch((err) => {
        console.error(err);
        setError("Impossible de récupérer les fiches.");
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="page">
        <p>Chargement des fiches...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="page">
        <p className="error">{error}</p>
      </div>
    );
  }

  if (items.length === 0) {
    return (
      <div className="page">
        <h2>Fiches tâches</h2>
        <p>Aucune fiche enregistrée pour le moment.</p>
      </div>
    );
  }

  return (
    <div className="page">
      <h2>Fiches tâches</h2>
      <table className="list-table">
        <thead>
          <tr>
            <th>Intitulé</th>
            <th>Phase</th>
            <th>Dernière mise à jour</th>
            <th>Chemin</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <tr key={item.path}>
              <td>{item.task_name}</td>
              <td>{item.phase || "-"}</td>
              <td>{item.updated_at || "-"}</td>
              <td>
                <code>{item.path}</code>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
