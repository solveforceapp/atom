import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools import ROOT, SYNCED_FILES, WEB_DIR

SCRIPT_FILE = next((name for name in SYNCED_FILES if name.endswith(".js")), "scripts.js")


@pytest.mark.parametrize("relative", SYNCED_FILES)
def test_root_asset_matches_web(relative: str) -> None:
    root_file = ROOT / relative
    web_file = WEB_DIR / relative

    assert root_file.exists(), f"Missing root asset: {relative}"
    assert web_file.exists(), f"Missing web asset: {relative}"
    root_text = root_file.read_text(encoding="utf-8")
    web_text = web_file.read_text(encoding="utf-8")

    # Normalize CRLF vs LF and ignore a final trailing newline so minor differences
    # in how files are written don't make the test fail.
    root_normalized = root_text.replace('\r\n', '\n').rstrip('\n')
    web_normalized = web_text.replace('\r\n', '\n').rstrip('\n')

    assert root_normalized == web_normalized

    if relative == "index.html":
        expected_tag = f'<script src="{SCRIPT_FILE}"></script>'
        assert (
            expected_tag in root_text
        ), f"index.html should reference {SCRIPT_FILE} via {expected_tag!r}"
