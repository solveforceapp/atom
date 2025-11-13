"""Utility scripts for maintaining the ATOM repository."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WEB_DIR = REPO_ROOT / "web"
ROOT_INDEX = REPO_ROOT / "index.html"
WEB_INDEX = WEB_DIR / "index.html"
STYLES_PATH = WEB_DIR / "styles.css"
SCRIPTS_PATH = WEB_DIR / "scripts.js"


def _asset_files() -> list[str]:
    return [path.name for path in (STYLES_PATH, SCRIPTS_PATH)]

__all__ = [
    "REPO_ROOT",
    "WEB_DIR",
    "ROOT_INDEX",
    "WEB_INDEX",
    "STYLES_PATH",
    "SCRIPTS_PATH",
    "render_root_index",
    "sync",
    "ASSET_FILES",
]

ASSET_FILES = _asset_files()


def __getattr__(name: str):
    if name == "render_root_index":
        from .sync_index import render_root_index as fn

        return fn
    if name == "sync":
        from .sync_index import sync as fn

        return fn
    raise AttributeError(name)
