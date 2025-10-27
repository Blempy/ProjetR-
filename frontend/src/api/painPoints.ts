import api from "./client";

export interface PainPointPayload {
  phase: string;
  task: string;
  description: string;
  frequency: number;
  duration: number;
  impact: number;
  stress: number;
  automation_idea?: string;
  comments?: string;
}

export interface PainPointResponse {
  path: string;
  phase: string;
  task: string;
}

export async function createPainPoint(payload: PainPointPayload): Promise<PainPointResponse> {
  const { data } = await api.post<PainPointResponse>("/staff/pain-points", payload);
  return data;
}
