"""Synchronize the repository root index.html with the microsite markup.

The ATOM microsite lives under ``web/`` so that static hosting providers can
serve the directory directly. Some platforms, however, expect a landing page at
``/``. This script copies the canonical ``web/index.html`` to the repository
root and rewrites the stylesheet/script paths so the page renders correctly
from either location.

Run this script whenever ``web/index.html`` changes:

    python tools/sync_root_index.py
"""

from __future__ import annotations

import pathlib
from typing import Iterable

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
WEB_INDEX_PATH = PROJECT_ROOT / "web" / "index.html"
ROOT_INDEX_PATH = PROJECT_ROOT / "index.html"


def _rewrite_paths(html: str, replacements: Iterable[tuple[str, str]]) -> str:
    """Apply the asset path replacements to ``html`` in order."""
    for old, new in replacements:
        html = html.replace(old, new)
    return html


def sync_root_index() -> None:
    """Copy ``web/index.html`` to the repo root with updated asset paths."""
    if not WEB_INDEX_PATH.exists():
        raise FileNotFoundError(f"Missing web index: {WEB_INDEX_PATH}")

    html = WEB_INDEX_PATH.read_text(encoding="utf-8")
    replacements = (
        ('href="styles.css"', 'href="web/styles.css"'),
        ("href='styles.css'", "href='web/styles.css'"),
        ('src="scripts.js"', 'src="web/scripts.js"'),
        ("src='scripts.js'", "src='web/scripts.js'"),
    )
    transformed = _rewrite_paths(html, replacements)
    ROOT_INDEX_PATH.write_text(transformed, encoding="utf-8")


if __name__ == "__main__":
    sync_root_index()
