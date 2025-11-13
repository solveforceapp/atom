"""Utilities for keeping repository root assets synchronized with the microsite."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEB_DIR = ROOT / "web"

SYNCED_FILES = [
    "index.html",
    "styles.css",
    "scripts.js",
]

# Keep the canonical JavaScript asset name in a single place so tests and
# helper scripts cannot drift from the actual synced file list.
SCRIPT_FILE = next((name for name in SYNCED_FILES if name.endswith(".js")), "scripts.js")

__all__ = ["ROOT", "WEB_DIR", "SYNCED_FILES", "SCRIPT_FILE"]
