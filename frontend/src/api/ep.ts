import api from "./client";

export interface ProjectInfo {
  name: string;
  commune?: string;
  reference?: string;
}

export interface RainParameters {
  method: string;
  a: number;
  b: number;
  c: number;
  return_period: string;
  safety_factor: number;
}

export interface SurfaceInput {
  label: string;
  surface_m2: number;
  coefficient: number;
  drains_to: string;
}

export interface CollectorInput {
  id: string;
  length_m: number;
  slope_percent: number;
  diameter_existing_mm?: number;
  roughness_n: number;
}

export interface ConstraintsInput {
  discharge_limit_lps_ha: number;
  safety_factor: number;
  min_velocity_ms: number;
  max_velocity_ms: number;
  minimum_tc_minutes: number;
}

export interface EPInputPayload {
  project: ProjectInfo;
  rain: RainParameters;
  surfaces: SurfaceInput[];
  collectors: CollectorInput[];
  constraints: ConstraintsInput;
}

export interface CollectorResult {
  id: string;
  area_total_m2: number;
  area_total_ha: number;
  weighted_coefficient: number;
  time_of_concentration_min: number;
  rain_intensity_mm_h: number;
  inflow_lps: number;
  permitted_outflow_lps: number;
  storage_volume_m3: number;
  recommended_diameter_mm: number;
  velocity_ms: number;
  full_flow_lps: number;
  conforms_autoclean: boolean;
  safety_factor_applied: number;
}

export interface EPResult {
  project: ProjectInfo;
  rain: RainParameters;
  collectors: CollectorResult[];
  total_storage_volume_m3: number;
  assumptions: string[];
  excel_path: string;
}

export async function calculateEP(payload: EPInputPayload): Promise<EPResult> {
  const { data } = await api.post<EPResult>("/ep/calc", payload);
  return data;
}
