import { Link, Route, Routes } from "react-router-dom";
import UserPortal from "./pages/UserPortal";
import UserTaskSheetForm from "./pages/UserTaskSheetForm";
import UserPainPointForm from "./pages/UserPainPointForm";
import StaffLogin from "./pages/StaffLogin";
import StaffDashboard from "./pages/StaffDashboard";
import StaffTaskSheetForm from "./pages/StaffTaskSheetForm";
import StaffPainPointForm from "./pages/StaffPainPointForm";
import ProtectedRoute from "./components/ProtectedRoute";

function Home() {
  return (
    <div className="page">
      <h1>MOE VRD Automatisation</h1>
      <nav className="menu">
        <Link to="user">Espace utilisateur</Link>
        <Link to="staff/login">Espace staff</Link>
      </nav>
    </div>
  );
}

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="user" element={<UserPortal />} />
      <Route path="user/task-sheets/new" element={<UserTaskSheetForm />} />
      <Route path="user/pain-points/new" element={<UserPainPointForm />} />
      <Route path="staff/login" element={<StaffLogin />} />
      <Route
        path="staff/dashboard"
        element={
          <ProtectedRoute>
            <StaffDashboard />
          </ProtectedRoute>
        }
      />
      <Route
        path="staff/task-sheets/new"
        element={
          <ProtectedRoute>
            <StaffTaskSheetForm />
          </ProtectedRoute>
        }
      />
      <Route
        path="staff/pain-points/new"
        element={
          <ProtectedRoute>
            <StaffPainPointForm />
          </ProtectedRoute>
        }
      />
    </Routes>
  );
}
