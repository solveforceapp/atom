"""Synchronize the repository root index.html with the microsite copy.

This keeps https://atom.solveforce.com/ (root) consistent with the content that
lives under the /web directory, while rewriting asset paths so both entry points
share the same CSS and JavaScript bundles.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WEB_INDEX = REPO_ROOT / "web" / "index.html"
ROOT_INDEX = REPO_ROOT / "index.html"

STYLE_REWRITE = {
    'href="styles.css"': 'href="web/styles.css"',
    "href='styles.css'": "href='web/styles.css'",
    'src="scripts.js"': 'src="web/scripts.js"',
    "src='scripts.js'": "src='web/scripts.js'",
}


def _load(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _rewrite_assets(html: str) -> str:
    """Rewrite asset paths so they resolve from the repository root."""

    updated = html
    for old, new in STYLE_REWRITE.items():
        updated = updated.replace(old, new)
    return updated


def render_root_index(web_html: str) -> str:
    """Return the root index markup based on the microsite source."""

    rewritten = _rewrite_assets(web_html)
    return rewritten if rewritten.endswith("\n") else f"{rewritten}\n"


def sync() -> None:
    """Synchronize the root index with the microsite copy."""

    web_html = _load(WEB_INDEX)
    ROOT_INDEX.write_text(render_root_index(web_html), encoding="utf-8")


if __name__ == "__main__":
    sync()
