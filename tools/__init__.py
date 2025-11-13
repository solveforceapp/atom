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

__all__ = ["ROOT", "WEB_DIR", "SYNCED_FILES"]
