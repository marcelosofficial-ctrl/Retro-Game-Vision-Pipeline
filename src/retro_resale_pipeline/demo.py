from __future__ import annotations

from .decision import screen
from .domain import CanonicalItem, EvidenceAsset, EvidenceType, MarketObservation, PhysicalObservation
from .evidence import make_region_key, sha256_bytes
from .repository import add_evidence, add_item, add_physical_idempotent, connect_memory, validate_database


def build_demo() -> tuple[PhysicalObservation, list[MarketObservation]]:
    asset_hash = sha256_bytes(b"synthetic-store-photo")
    physical = PhysicalObservation(
        "OBS-DEMO-001",
        "ITEM-DEMO-NEON-RACER-2",
        1_200,
        "SEGA_SATURN",
        "JP",
        "STANDARD",
        "CIB",
        "ASSET-SYNTHETIC-001",
        make_region_key(asset_hash, (20, 30, 420, 620)),
    )
    market = [
        MarketObservation("M1", physical.item_id, 3_200, "SEGA_SATURN", "JP", "STANDARD", "CIB", EvidenceType.SOLD),
        MarketObservation("M2", physical.item_id, 3_400, "SEGA_SATURN", "JP", "STANDARD", "CIB", EvidenceType.SOLD),
        MarketObservation("M3", physical.item_id, 3_600, "SEGA_SATURN", "JP", "STANDARD", "CIB", EvidenceType.SOLD),
        MarketObservation("M4", physical.item_id, 8_500, "PLAYSTATION", "JP", "STANDARD", "CIB", EvidenceType.SOLD),
        MarketObservation("M5", physical.item_id, 5_900, "SEGA_SATURN", "JP", "LIMITED", "CIB", EvidenceType.SOLD),
    ]
    return physical, market


def main() -> None:
    physical, market = build_demo()
    result = screen(physical, market)

    conn = connect_memory()
    asset = EvidenceAsset("ASSET-SYNTHETIC-001", physical.region_key.split(":", 1)[0], "synthetic_store_photo")
    item = CanonicalItem(physical.item_id, "Neon Racer 2", physical.platform, physical.region)
    add_evidence(conn, asset)
    add_item(conn, item)
    add_physical_idempotent(conn, physical)
    integrity, fk_count = validate_database(conn)

    print(f"{result.decision.value}  Neon Racer 2 (JP Saturn)")
    print(f"Buy price:        ¥{physical.price_jpy:,}")
    print(f"Expected sale:    ¥{result.expected_sale_jpy:,}")
    print(f"Expected profit:  ¥{result.expected_profit_jpy:,}")
    print(f"ROI:              {result.roi_percent:.1f}%")
    print(f"Evidence:         {result.compatible_sold_count} compatible sold observations")
    print(f"Database:         integrity={integrity}, foreign_keys={fk_count}")


if __name__ == "__main__":
    main()
