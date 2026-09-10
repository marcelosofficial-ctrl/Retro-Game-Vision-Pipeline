from __future__ import annotations

import sqlite3

from .domain import CanonicalItem, EvidenceAsset, PhysicalObservation

SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS evidence_asset (
    asset_id TEXT PRIMARY KEY,
    sha256 TEXT NOT NULL UNIQUE,
    source_name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS canonical_item (
    item_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    platform TEXT NOT NULL,
    region TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS physical_observation (
    observation_id TEXT PRIMARY KEY,
    item_id TEXT NOT NULL REFERENCES canonical_item(item_id),
    evidence_asset_id TEXT NOT NULL REFERENCES evidence_asset(asset_id),
    region_key TEXT NOT NULL,
    price_jpy INTEGER NOT NULL CHECK(price_jpy >= 0),
    platform TEXT NOT NULL,
    region TEXT NOT NULL,
    edition TEXT NOT NULL,
    completeness TEXT NOT NULL,
    UNIQUE(evidence_asset_id, region_key)
);
"""


def connect_memory() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    return conn


def add_evidence(conn: sqlite3.Connection, asset: EvidenceAsset) -> None:
    conn.execute(
        "INSERT OR IGNORE INTO evidence_asset(asset_id, sha256, source_name) VALUES (?, ?, ?)",
        (asset.asset_id, asset.sha256, asset.source_name),
    )


def add_item(conn: sqlite3.Connection, item: CanonicalItem) -> None:
    conn.execute(
        "INSERT OR IGNORE INTO canonical_item(item_id, title, platform, region) VALUES (?, ?, ?, ?)",
        (item.item_id, item.title, item.platform, item.region),
    )


def add_physical_idempotent(conn: sqlite3.Connection, physical: PhysicalObservation) -> bool:
    before = conn.total_changes
    conn.execute(
        """
        INSERT OR IGNORE INTO physical_observation(
            observation_id, item_id, evidence_asset_id, region_key, price_jpy,
            platform, region, edition, completeness
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            physical.observation_id,
            physical.item_id,
            physical.evidence_asset_id,
            physical.region_key,
            physical.price_jpy,
            physical.platform,
            physical.region,
            physical.edition,
            physical.completeness,
        ),
    )
    return conn.total_changes > before


def validate_database(conn: sqlite3.Connection) -> tuple[str, int]:
    integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
    foreign_key_violations = len(conn.execute("PRAGMA foreign_key_check").fetchall())
    return integrity, foreign_key_violations
