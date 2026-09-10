import unittest

from retro_resale_pipeline.decision import screen
from retro_resale_pipeline.demo import build_demo
from retro_resale_pipeline.domain import Decision, EvidenceType


class DecisionTests(unittest.TestCase):
    def test_demo_ignores_incompatible_high_prices(self):
        physical, market = build_demo()
        result = screen(physical, market)
        self.assertEqual(result.decision, Decision.BUY)
        self.assertEqual(result.expected_sale_jpy, 3_400)
        self.assertEqual(result.compatible_sold_count, 3)

    def test_insufficient_sold_evidence_returns_research(self):
        physical, market = build_demo()
        sold = [row for row in market if row.evidence_type == EvidenceType.SOLD][:1]
        result = screen(physical, sold)
        self.assertEqual(result.decision, Decision.RESEARCH)
        self.assertIsNone(result.expected_sale_jpy)


if __name__ == "__main__":
    unittest.main()
