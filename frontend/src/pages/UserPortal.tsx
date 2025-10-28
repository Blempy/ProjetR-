import { Link } from "react-router-dom";

export default function UserPortal() {
  return (
    <div className="page">
      <h2>Portail utilisateur</h2>
      <p>Soumettez vos tâches ou points de douleur pour alimenter le référentiel.</p>
      <nav className="menu">
        <Link to="/user/task-sheets/new">Proposer une fiche tâche</Link>
        <Link to="/user/pain-points/new">Déclarer un point de douleur</Link>
        <Link to="/user/ep">Calcul note EP</Link>
      </nav>
    </div>
  );
}
