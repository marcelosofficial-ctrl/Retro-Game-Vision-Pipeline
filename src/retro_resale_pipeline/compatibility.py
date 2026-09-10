from __future__ import annotations

from .domain import CompatibilityResult, MarketObservation, PhysicalObservation

SPECIFIC_EDITIONS = {"SATAKORE", "LIMITED", "REISSUE", "BUDGET"}


def compatible_copy(physical: PhysicalObservation, market: MarketObservation) -> CompatibilityResult:
    """Small public subset of the production compatibility layer."""
    if physical.item_id != market.item_id:
        return CompatibilityResult(False, "DIFFERENT_CANONICAL_ITEM")
    if physical.platform != market.platform:
        return CompatibilityResult(False, "PLATFORM_MISMATCH")
    if physical.region != market.region:
        return CompatibilityResult(False, "REGION_MISMATCH")
    if physical.edition in SPECIFIC_EDITIONS or market.edition in SPECIFIC_EDITIONS:
        if physical.edition != market.edition:
            return CompatibilityResult(False, "EDITION_MISMATCH")
    if physical.completeness in {"DISC_ONLY", "LOOSE"} and market.completeness == "CIB":
        return CompatibilityResult(False, "COMPLETENESS_MISMATCH")
    if physical.completeness == "CIB" and market.completeness not in {"CIB", "UNKNOWN"}:
        return CompatibilityResult(False, "COMPLETENESS_MISMATCH")
    return CompatibilityResult(True, "COMPATIBLE")
