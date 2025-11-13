"""Synchronize the repository root landing page with the microsite copy.

Unlike the first iteration of this helper, we now mirror the microsite assets
(`styles.css` and `scripts.js`) into the repository root so that
``https://atom.solveforce.com/`` renders correctly without depending on nested
paths. The HTML itself stays identical between locations which keeps authoring
simple while guaranteeing the homepage works when the repository root is
deployed as-is.
"""

from __future__ import annotations

from pathlib import Path
from shutil import copy2

REPO_ROOT = Path(__file__).resolve().parent.parent
WEB_DIR = REPO_ROOT / "web"
WEB_INDEX = WEB_DIR / "index.html"
ROOT_INDEX = REPO_ROOT / "index.html"

# Assets that must exist alongside index.html at both the root and the web copy.
ASSET_FILES = ["styles.css", "scripts.js"]


def _load(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def render_root_index(web_html: str) -> str:
    """Return the root index markup based on the microsite source."""

    return web_html if web_html.endswith("\n") else f"{web_html}\n"


def _sync_assets() -> None:
    """Copy shared assets into the repository root."""

    for filename in ASSET_FILES:
        source = WEB_DIR / filename
        target = REPO_ROOT / filename
        if not source.exists():
            raise FileNotFoundError(f"Missing expected asset: {source}")
        target.parent.mkdir(parents=True, exist_ok=True)
        copy2(source, target)


def sync() -> None:
    """Synchronize the root index with the microsite copy."""

    web_html = _load(WEB_INDEX)
    ROOT_INDEX.write_text(render_root_index(web_html), encoding="utf-8")
    _sync_assets()


if __name__ == "__main__":
    sync()
