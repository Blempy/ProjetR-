import api from "./client";

export interface LoginPayload {
  username: string;
  password: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

export interface UserProfile {
  username: string;
  roles: string[];
}

export async function login(payload: LoginPayload): Promise<TokenResponse> {
  const params = new URLSearchParams();
  params.append("username", payload.username);
  params.append("password", payload.password);
  params.append("grant_type", "password");

  const { data } = await api.post<TokenResponse>("/auth/login", params, {
    headers: { "Content-Type": "application/x-www-form-urlencoded" }
  });
  return data;
}

export async function fetchProfile(token: string): Promise<UserProfile> {
  const { data } = await api.get<UserProfile>("/staff/profile", {
    headers: { Authorization: `Bearer ${token}` }
  });
  return data;
}
