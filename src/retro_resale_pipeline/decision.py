from __future__ import annotations

from statistics import median

from .compatibility import compatible_copy
from .domain import Decision, DecisionResult, EvidenceType, MarketObservation, PhysicalObservation

# Deliberately simplified public-demo values. These are not production policy.
PLATFORM_FEE_RATE = 0.10
SHIPPING_JPY = 350
PACKING_JPY = 120
MIN_SOLD_FOR_ACTION = 2
BUY_MIN_PROFIT_JPY = 1_000
BUY_MIN_ROI = 50.0
MAYBE_MIN_PROFIT_JPY = 500


def screen(physical: PhysicalObservation, market_rows: list[MarketObservation]) -> DecisionResult:
    sold = [
        row
        for row in market_rows
        if row.evidence_type == EvidenceType.SOLD and compatible_copy(physical, row).compatible
    ]
    if len(sold) < MIN_SOLD_FOR_ACTION:
        return DecisionResult(
            Decision.RESEARCH,
            None,
            None,
            None,
            len(sold),
            "INSUFFICIENT_COMPATIBLE_SOLD_EVIDENCE",
        )

    expected_sale = round(median(row.price_jpy for row in sold))
    proceeds = expected_sale * (1 - PLATFORM_FEE_RATE) - SHIPPING_JPY - PACKING_JPY
    profit = round(proceeds - physical.price_jpy)
    roi = round((profit / physical.price_jpy) * 100, 1)

    if profit >= BUY_MIN_PROFIT_JPY and roi >= BUY_MIN_ROI:
        decision, reason = Decision.BUY, "DEMO_BUY_THRESHOLDS_MET"
    elif profit >= MAYBE_MIN_PROFIT_JPY:
        decision, reason = Decision.MAYBE, "DEMO_MAYBE_THRESHOLD_MET"
    else:
        decision, reason = Decision.SKIP, "DEMO_PROFIT_THRESHOLD_NOT_MET"

    return DecisionResult(decision, expected_sale, profit, roi, len(sold), reason)
