import {
  createContext,
  ReactNode,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState
} from "react";
import api from "../api/client";
import { fetchProfile, login, TokenResponse, UserProfile } from "../api/auth";

interface AuthContextValue {
  token: string | null;
  user: UserProfile | null;
  loading: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

const STORAGE_KEY = "staff_token";

export function AuthProvider({ children }: { children: ReactNode }) {
  const [token, setToken] = useState<string | null>(() => localStorage.getItem(STORAGE_KEY));
  const [user, setUser] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState<boolean>(!!token);

  useEffect(() => {
    if (!token) {
      setUser(null);
      setLoading(false);
      delete api.defaults.headers.common.Authorization;
      return;
    }
    api.defaults.headers.common.Authorization = `Bearer ${token}`;
    setLoading(true);
    fetchProfile(token)
      .then(setUser)
      .catch(() => {
        setToken(null);
        localStorage.removeItem(STORAGE_KEY);
      })
      .finally(() => setLoading(false));
  }, [token]);

  const handleLogin = useCallback(async (username: string, password: string) => {
    const data: TokenResponse = await login({ username, password });
    setToken(data.access_token);
    localStorage.setItem(STORAGE_KEY, data.access_token);
  }, []);

  const handleLogout = useCallback(() => {
    setToken(null);
    setUser(null);
    localStorage.removeItem(STORAGE_KEY);
    delete api.defaults.headers.common.Authorization;
  }, []);

  const value = useMemo<AuthContextValue>(
    () => ({ token, user, loading, login: handleLogin, logout: handleLogout }),
    [token, user, loading, handleLogin, handleLogout]
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return ctx;
}
