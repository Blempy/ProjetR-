import unittest

from backend.app.ep.engine import (
    EPCalculator,
    caquot_diameter_mm,
    compute_montana_intensity,
    compute_time_of_concentration,
    manning_full_flow_lps,
)
from backend.app.ep.schemas import (
    CollectorInput,
    ConstraintsInput,
    EPInput,
    ProjectInfo,
    RainParameters,
    SurfaceInput,
)


class TestEPEngine(unittest.TestCase):
    def test_montana_intensity(self) -> None:
        low = compute_montana_intensity(40, 15, 0.8, 20)
        high = compute_montana_intensity(60, 15, 0.8, 20)
        self.assertGreater(high, low)

    def test_time_of_concentration(self) -> None:
        tc = compute_time_of_concentration(30, 0.5, minimum_minutes=10)
        self.assertGreaterEqual(tc, 10)

    def test_caquot_diameter(self) -> None:
        self.assertGreater(caquot_diameter_mm(50, 1.0), 0)

    def test_manning_flow(self) -> None:
        q, v = manning_full_flow_lps(400, 1.0, 0.013)
        self.assertGreater(q, 0)
        self.assertGreater(v, 0)

    def test_calculator(self) -> None:
        data = EPInput(
            project=ProjectInfo(name="ZAC Test", commune="Ville"),
            rain=RainParameters(a=58.1, b=18.2, c=0.78, return_period="10", safety_factor=1.1),
            surfaces=[
                SurfaceInput(label="Chaussée principale", surface_m2=4500, coefficient=0.92, drains_to="T1"),
                SurfaceInput(label="Parking", surface_m2=1200, coefficient=0.55, drains_to="T1"),
            ],
            collectors=[
                CollectorInput(id="T1", length_m=150, slope_percent=0.6, diameter_existing_mm=315),
            ],
            constraints=ConstraintsInput(
                discharge_limit_lps_ha=5,
                safety_factor=1.1,
                min_velocity_ms=0.6,
                max_velocity_ms=3.0,
                minimum_tc_minutes=10.0,
            ),
        )

        result = EPCalculator(data).run()
        self.assertEqual(len(result.collectors), 1)

        collector = result.collectors[0]
        self.assertEqual(collector.id, "T1")
        self.assertAlmostEqual(collector.area_total_m2, 5700.0)
        expected_coeff = (4500 * 0.92 + 1200 * 0.55) / 5700
        self.assertAlmostEqual(collector.weighted_coefficient, round(expected_coeff, 3))
        self.assertGreaterEqual(collector.inflow_lps, collector.permitted_outflow_lps)
        self.assertGreaterEqual(collector.storage_volume_m3, 0)


if __name__ == "__main__":
    unittest.main()
