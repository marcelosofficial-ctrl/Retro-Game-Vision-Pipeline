import sqlite3
import unittest

from retro_resale_pipeline.domain import CanonicalItem, EvidenceAsset, PhysicalObservation
from retro_resale_pipeline.repository import add_evidence, add_item, add_physical_idempotent, connect_memory, validate_database


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.conn = connect_memory()
        add_evidence(self.conn, EvidenceAsset("A1", "abc123", "synthetic"))
        add_item(self.conn, CanonicalItem("I1", "Synthetic Game", "SEGA_SATURN", "JP"))
        self.obs = PhysicalObservation("O1", "I1", 900, "SEGA_SATURN", "JP", "STANDARD", "CIB", "A1", "abc123:0,0,100,100")

    def test_physical_ingest_is_idempotent(self):
        self.assertTrue(add_physical_idempotent(self.conn, self.obs))
        self.assertFalse(add_physical_idempotent(self.conn, self.obs))
        count = self.conn.execute("SELECT COUNT(*) FROM physical_observation").fetchone()[0]
        self.assertEqual(count, 1)

    def test_foreign_keys_are_enforced(self):
        bad = PhysicalObservation("O2", "MISSING", 900, "SEGA_SATURN", "JP", "STANDARD", "CIB", "A1")
        with self.assertRaises(sqlite3.IntegrityError):
            add_physical_idempotent(self.conn, bad)

    def test_database_validates_cleanly(self):
        add_physical_idempotent(self.conn, self.obs)
        self.assertEqual(validate_database(self.conn), ("ok", 0))


if __name__ == "__main__":
    unittest.main()
