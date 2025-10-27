from __future__ import annotations

import math
from typing import Dict, Iterable, List, Tuple

from .schemas import (
    CollectorInput,
    CollectorResult,
    EPInput,
    EPResult,
    SurfaceInput,
)


def compute_montana_intensity(a: float, b: float, c: float, duration_minutes: float) -> float:
    """Return intensity in mm/h using Montana law."""
    duration = max(duration_minutes, 1.0)
    return a / ((duration + b) ** c)


def compute_time_of_concentration(length_m: float, slope_percent: float, minimum_minutes: float) -> float:
    """Kirpich empirical formula in minutes with minimum floor."""
    slope_ratio = max(slope_percent / 100.0, 0.0001)
    tc = 0.01947 * (length_m ** 0.77) * (slope_ratio ** -0.385)
    return max(tc, minimum_minutes)


def caquot_diameter_mm(q_lps: float, slope_percent: float) -> float:
    """Return recommended diameter (mm) using Caquot empirical relation."""
    if q_lps <= 0 or slope_percent <= 0:
        return 0.0
    slope_ratio = slope_percent / 100.0
    d_m = 0.30 * (slope_ratio ** -0.1875) * ((q_lps / 1000.0) ** 0.375)
    return d_m * 1000.0


def manning_full_flow_lps(diameter_mm: float, slope_percent: float, roughness_n: float) -> Tuple[float, float]:
    """Return (Q_full l/s, velocity m/s) for a circular conduit flowing full."""
    if diameter_mm <= 0 or slope_percent <= 0 or roughness_n <= 0:
        return 0.0, 0.0

    diameter_m = diameter_mm / 1000.0
    slope = slope_percent / 100.0
    area = math.pi * (diameter_m ** 2) / 4.0
    hydraulic_radius = diameter_m / 4.0
    q_m3s = (1.0 / roughness_n) * area * (hydraulic_radius ** (2.0 / 3.0)) * (slope ** 0.5)
    velocity = q_m3s / area if area > 0 else 0.0
    return q_m3s * 1000.0, velocity


def _group_surfaces_by_collector(surfaces: Iterable[SurfaceInput]) -> Dict[str, List[SurfaceInput]]:
    grouped: Dict[str, List[SurfaceInput]] = {}
    for surface in surfaces:
        grouped.setdefault(surface.drains_to, []).append(surface)
    return grouped


class EPCalculator:
    """Central calculation service for EP notes."""

    def __init__(self, data: EPInput) -> None:
        self.data = data

    def run(self) -> EPResult:
        grouped = _group_surfaces_by_collector(self.data.surfaces)
        results: List[CollectorResult] = []

        total_volume = 0.0
        assumptions = [
            f"Méthode de pluie : {self.data.rain.method} (retour {self.data.rain.return_period} ans)",
            f"Débit de fuite max : {self.data.constraints.discharge_limit_lps_ha} l/s/ha",
            f"Coefficient de sécurité pluie : {self.data.rain.safety_factor}",
            f"Coefficient de sécurité hydraulique : {self.data.constraints.safety_factor}",
        ]

        for collector in self.data.collectors:
            surfaces = grouped.get(collector.id, [])
            result = self._compute_collector(collector, surfaces)
            total_volume += result.storage_volume_m3
            results.append(result)

        return EPResult(
            project=self.data.project,
            rain=self.data.rain,
            collectors=results,
            total_storage_volume_m3=round(total_volume, 3),
            assumptions=assumptions,
        )

    def _compute_collector(
        self,
        collector: CollectorInput,
        surfaces: List[SurfaceInput],
    ) -> CollectorResult:
        area_total_m2 = sum(s.surface_m2 for s in surfaces)
        area_total_ha = area_total_m2 / 10000.0

        if area_total_m2 > 0:
            weighted_coefficient = sum(s.surface_m2 * s.coefficient for s in surfaces) / area_total_m2
        else:
            weighted_coefficient = 0.0

        tc_minutes = compute_time_of_concentration(
            collector.length_m,
            collector.slope_percent,
            self.data.constraints.minimum_tc_minutes,
        )

        intensity_mm_h = compute_montana_intensity(
            self.data.rain.a,
            self.data.rain.b,
            self.data.rain.c,
            tc_minutes,
        ) * self.data.rain.safety_factor

        intensity_m_s = (intensity_mm_h / 1000.0) / 3600.0

        q_in_m3s = weighted_coefficient * intensity_m_s * area_total_m2 * self.data.constraints.safety_factor
        q_in_lps = q_in_m3s * 1000.0

        discharge_limit_lps = (
            self.data.constraints.discharge_limit_lps_ha * area_total_ha
            if self.data.constraints.discharge_limit_lps_ha > 0
            else q_in_lps
        )
        q_out_lps = min(q_in_lps, discharge_limit_lps)
        q_out_m3s = q_out_lps / 1000.0

        tc_seconds = tc_minutes * 60.0
        storage_volume = max(q_in_m3s - q_out_m3s, 0.0) * tc_seconds

        recommended_diameter_mm = caquot_diameter_mm(q_in_lps, collector.slope_percent)
        if collector.diameter_existing_mm:
            recommended_diameter_mm = max(recommended_diameter_mm, collector.diameter_existing_mm)

        diameter_for_flow = recommended_diameter_mm or (collector.diameter_existing_mm or 0.0)
        full_flow_lps, velocity_ms = manning_full_flow_lps(
            diameter_for_flow,
            collector.slope_percent,
            collector.roughness_n,
        )

        conforms = (
            self.data.constraints.min_velocity_ms <= velocity_ms <= self.data.constraints.max_velocity_ms
            and full_flow_lps >= q_in_lps
        )

        return CollectorResult(
            id=collector.id,
            area_total_m2=round(area_total_m2, 2),
            area_total_ha=round(area_total_ha, 4),
            weighted_coefficient=round(weighted_coefficient, 3),
            time_of_concentration_min=round(tc_minutes, 2),
            rain_intensity_mm_h=round(intensity_mm_h, 2),
            inflow_lps=round(q_in_lps, 2),
            permitted_outflow_lps=round(q_out_lps, 2),
            storage_volume_m3=round(storage_volume, 3),
            recommended_diameter_mm=round(recommended_diameter_mm, 1),
            velocity_ms=round(velocity_ms, 3),
            full_flow_lps=round(full_flow_lps, 2),
            conforms_autoclean=conforms,
            safety_factor_applied=self.data.constraints.safety_factor,
        )
