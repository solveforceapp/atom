"""Copy microsite assets from `web/` into the repository root.

Run with `python -m tools.sync_root` after editing files under `web/` to
refresh the root-level landing page and its accompanying static assets.
"""

from __future__ import annotations

from pathlib import Path

from . import ROOT, SYNCED_FILES, WEB_DIR


def _copy_file(source: Path, destination: Path) -> None:
    destination.write_bytes(source.read_bytes())


def sync_root_assets() -> list[str]:
    """Copy the index, stylesheet, and script from ``web/`` to the project root."""
    copied: list[str] = []
    for relative in SYNCED_FILES:
        source = WEB_DIR / relative
        if not source.exists():
            raise FileNotFoundError(f"Missing expected microsite asset: {source}")
        destination = ROOT / relative
        # Ensure parent directories exist (useful if syncing into fresh checkouts).
        destination.parent.mkdir(parents=True, exist_ok=True)
        _copy_file(source, destination)
        copied.append(relative)
    return copied


def main() -> None:
    copied = sync_root_assets()
    joined = ", ".join(copied)
    print(f"Synced assets to repository root: {joined}")


if __name__ == "__main__":
    main()
from pathlib import Path
import shutil
from . import ROOT, WEB_DIR, SYNCED_FILES

def sync_root() -> None:
    """Deterministically copy SYNCED_FILES from web/ to repository root,
    overwriting any existing root copy.
    """
    for rel in SYNCED_FILES:
        src = WEB_DIR / rel
        dst = ROOT / rel
        if not src.exists():
            raise FileNotFoundError(f"Expected web asset missing: {src}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)

if __name__ == "__main__":
    sync_root()
