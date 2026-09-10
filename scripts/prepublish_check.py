from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BLOCKED_SUFFIXES = {".db", ".sqlite", ".sqlite3", ".zip", ".heic", ".jpg", ".jpeg", ".webp"}
BLOCKED_DIR_NAMES = {"backups", "evidence", "market", "imports", "private", "production", "checkpoints"}
TEXT_PATTERNS = {
    "container/local path": re.compile(r"(?:/mnt/data/|[A-Za-z]:\\\\)"),
    "private checkpoint marker": re.compile(r"c6_[0-9]", re.I),
    "cookie/session token": re.compile(r"(?:sessionid|auth_token|cookie:)\s*[:=]?\s*\S+", re.I),
}


def main() -> int:
    failures: list[str] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in BLOCKED_DIR_NAMES for part in rel.parts):
            failures.append(f"blocked directory: {rel}")
        if path.suffix.lower() in BLOCKED_SUFFIXES:
            failures.append(f"blocked file type: {rel}")
        if rel == Path("scripts/prepublish_check.py"):
            continue
        if path.suffix.lower() in {".md", ".py", ".json", ".toml", ".yml", ".yaml", ".txt", ".html", ".svg"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for label, pattern in TEXT_PATTERNS.items():
                if pattern.search(text):
                    failures.append(f"{label}: {rel}")
    if failures:
        print("Pre-publication check FAILED:")
        for failure in sorted(set(failures)):
            print(f" - {failure}")
        return 1
    print("Pre-publication check PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
