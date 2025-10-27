import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

interface Props {
  children: JSX.Element;
}

export default function ProtectedRoute({ children }: Props) {
  const { token, loading } = useAuth();

  if (loading) {
    return <p>Chargement...</p>;
  }

  if (!token) {
    return <Navigate to="/staff/login" replace />;
  }

  return children;
}
