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
