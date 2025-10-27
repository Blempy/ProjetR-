import { useAuth } from "../context/AuthContext";
import { Link } from "react-router-dom";

export default function StaffDashboard() {
  const { user, logout } = useAuth();

  return (
    <div className="page">
      <h2>Espace staff</h2>
      {user ? (
        <>
          <p>Connecté en tant que <strong>{user.username}</strong></p>
          <p>Rôles : {user.roles.join(", ") || "aucun"}</p>
          <nav className="menu">
            <Link to="/staff/task-sheets/new">Nouvelle fiche tâche</Link>
          </nav>
        </>
      ) : (
        <p>Chargement des informations...</p>
      )}
      <button type="button" onClick={logout}>
        Se déconnecter
      </button>
    </div>
  );
}
