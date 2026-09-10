import unittest

from retro_resale_pipeline.evidence import make_region_key, sha256_bytes


class EvidenceTests(unittest.TestCase):
    def test_hash_is_stable(self):
        self.assertEqual(sha256_bytes(b"same-photo"), sha256_bytes(b"same-photo"))

    def test_invalid_bbox_is_rejected(self):
        digest = sha256_bytes(b"photo")
        with self.assertRaises(ValueError):
            make_region_key(digest, (20, 20, 10, 30))


if __name__ == "__main__":
    unittest.main()
