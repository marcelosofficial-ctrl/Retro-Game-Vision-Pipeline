from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class EvidenceType(str, Enum):
    SOLD = "SOLD"
    ACTIVE_ASK = "ACTIVE_ASK"
    BUYBACK = "BUYBACK"
    RETAIL_ASK = "RETAIL_ASK"
    GUIDE = "GUIDE"


class Decision(str, Enum):
    BUY = "BUY"
    MAYBE = "MAYBE"
    RESEARCH = "RESEARCH"
    SKIP = "SKIP"


@dataclass(frozen=True)
class CanonicalItem:
    item_id: str
    title: str
    platform: str
    region: str


@dataclass(frozen=True)
class EvidenceAsset:
    asset_id: str
    sha256: str
    source_name: str


@dataclass(frozen=True)
class PhysicalObservation:
    observation_id: str
    item_id: str
    price_jpy: int
    platform: str
    region: str
    edition: str
    completeness: str
    evidence_asset_id: str
    region_key: str = "WHOLE_IMAGE"


@dataclass(frozen=True)
class MarketObservation:
    market_id: str
    item_id: str
    price_jpy: int
    platform: str
    region: str
    edition: str
    completeness: str
    evidence_type: EvidenceType
    confidence: float = 1.0


@dataclass(frozen=True)
class CompatibilityResult:
    compatible: bool
    reason: str


@dataclass(frozen=True)
class DecisionResult:
    decision: Decision
    expected_sale_jpy: int | None
    expected_profit_jpy: int | None
    roi_percent: float | None
    compatible_sold_count: int
    reason: str
