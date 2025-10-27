import { Link } from "react-router-dom";

export default function NavBar() {
  return (
    <header className="nav-bar">
      <div className="nav-content">
        <h1 className="logo">MOE VRD Automatisation</h1>
        <nav className="nav-links">
          <Link to="/user">Espace utilisateur</Link>
          <Link to="/staff/login">Espace staff</Link>
        </nav>
      </div>
    </header>
  );
}
