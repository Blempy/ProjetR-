from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, validator


class ProjectInfo(BaseModel):
    name: str
    commune: Optional[str] = None
    reference: Optional[str] = None


class RainParameters(BaseModel):
    method: str = Field("montana", description="Méthode utilisée (montana)")
    a: float = Field(..., description="Paramètre a de Montana")
    b: float = Field(..., description="Paramètre b de Montana")
    c: float = Field(..., description="Paramètre c de Montana")
    return_period: str = Field("10", description="Période de retour (années) sous forme de chaîne")
    safety_factor: float = Field(1.0, ge=1.0, description="Coefficient de sécurité appliqué à la pluie")


class SurfaceInput(BaseModel):
    label: str
    surface_m2: float = Field(..., ge=0)
    coefficient: float = Field(..., ge=0, le=1)
    drains_to: str


class CollectorInput(BaseModel):
    id: str
    length_m: float = Field(..., gt=0)
    slope_percent: float = Field(..., gt=0)
    diameter_existing_mm: Optional[float] = Field(None, gt=0)
    roughness_n: float = Field(0.013, gt=0)


class ConstraintsInput(BaseModel):
    discharge_limit_lps_ha: float = Field(5.0, ge=0)
    safety_factor: float = Field(1.1, ge=1.0)
    min_velocity_ms: float = Field(0.6, ge=0)
    max_velocity_ms: float = Field(3.0, ge=0)
    minimum_tc_minutes: float = Field(10.0, ge=1)


class EPInput(BaseModel):
    project: ProjectInfo
    rain: RainParameters
    surfaces: List[SurfaceInput]
    collectors: List[CollectorInput]
    constraints: ConstraintsInput

    @validator("collectors")
    def ensure_unique_collectors(cls, value: List[CollectorInput]) -> List[CollectorInput]:
        ids = [c.id for c in value]
        if len(set(ids)) != len(ids):
            raise ValueError("Les identifiants de collecteurs doivent être uniques.")
        return value

    @validator("surfaces")
    def ensure_surface_assignments(cls, value: List[SurfaceInput]) -> List[SurfaceInput]:
        if not value:
            raise ValueError("Au moins une surface doit être fournie.")
        return value


class CollectorResult(BaseModel):
    id: str
    area_total_m2: float
    area_total_ha: float
    weighted_coefficient: float
    time_of_concentration_min: float
    rain_intensity_mm_h: float
    inflow_lps: float
    permitted_outflow_lps: float
    storage_volume_m3: float
    recommended_diameter_mm: float
    velocity_ms: float
    full_flow_lps: float
    conforms_autoclean: bool
    safety_factor_applied: float


class EPResult(BaseModel):
    project: ProjectInfo
    rain: RainParameters
    collectors: List[CollectorResult]
    total_storage_volume_m3: float
    assumptions: List[str]
