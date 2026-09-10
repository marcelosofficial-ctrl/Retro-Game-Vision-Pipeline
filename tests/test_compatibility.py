import unittest

from retro_resale_pipeline.compatibility import compatible_copy
from retro_resale_pipeline.domain import EvidenceType, MarketObservation, PhysicalObservation


class CompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.physical = PhysicalObservation("OBS1", "ITEM1", 1_000, "SEGA_SATURN", "JP", "STANDARD", "DISC_ONLY", "ASSET1")

    def market(self, **overrides):
        row = dict(market_id="M1", item_id="ITEM1", price_jpy=5_000, platform="SEGA_SATURN", region="JP", edition="STANDARD", completeness="DISC_ONLY", evidence_type=EvidenceType.SOLD)
        row.update(overrides)
        return MarketObservation(**row)

    def test_exact_copy_is_compatible(self):
        self.assertTrue(compatible_copy(self.physical, self.market()).compatible)

    def test_platform_cross_comp_is_rejected(self):
        result = compatible_copy(self.physical, self.market(platform="PLAYSTATION"))
        self.assertFalse(result.compatible)
        self.assertEqual(result.reason, "PLATFORM_MISMATCH")

    def test_disc_only_cannot_borrow_cib_value(self):
        result = compatible_copy(self.physical, self.market(completeness="CIB"))
        self.assertFalse(result.compatible)
        self.assertEqual(result.reason, "COMPLETENESS_MISMATCH")

    def test_specific_edition_mismatch_is_rejected(self):
        satakore = PhysicalObservation("OBS2", "ITEM1", 1_000, "SEGA_SATURN", "JP", "SATAKORE", "CIB", "ASSET2")
        result = compatible_copy(satakore, self.market(completeness="CIB"))
        self.assertFalse(result.compatible)
        self.assertEqual(result.reason, "EDITION_MISMATCH")


if __name__ == "__main__":
    unittest.main()
