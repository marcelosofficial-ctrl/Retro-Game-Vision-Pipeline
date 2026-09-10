from __future__ import annotations

import hashlib


def sha256_bytes(data: bytes) -> str:
    """Return a stable content identity for one evidence asset."""
    return hashlib.sha256(data).hexdigest()


def make_region_key(asset_sha256: str, bbox: tuple[int, int, int, int] | None = None) -> str:
    """Create a deterministic key for a whole image or one derived image region."""
    if bbox is None:
        return f"{asset_sha256}:WHOLE_IMAGE"
    x1, y1, x2, y2 = bbox
    if min(x1, y1, x2, y2) < 0 or x2 <= x1 or y2 <= y1:
        raise ValueError("invalid bounding box")
    return f"{asset_sha256}:{x1},{y1},{x2},{y2}"
