import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools import ROOT, SCRIPT_FILE, SYNCED_FILES, WEB_DIR

SCRIPT_TAG = f'<script src="{SCRIPT_FILE}"></script>'


@pytest.mark.parametrize("relative", SYNCED_FILES)
def test_root_asset_matches_web(relative: str) -> None:
    root_file = ROOT / relative
    web_file = WEB_DIR / relative

    assert root_file.exists(), f"Missing root asset: {relative}"
    assert web_file.exists(), f"Missing web asset: {relative}"
    root_text = root_file.read_text(encoding="utf-8")
    web_text = web_file.read_text(encoding="utf-8")

    assert root_text == web_text

    if relative == "index.html":
        message = (
            "index.html should include the shared script via "
            f"{SCRIPT_TAG!r} so root and web copies stay aligned"
        )
        assert SCRIPT_TAG in root_text, message
        assert SCRIPT_TAG in web_text, message
