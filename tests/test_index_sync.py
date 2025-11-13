import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tools import ROOT_INDEX, WEB_INDEX, render_root_index


def test_root_index_matches_web():
    assert WEB_INDEX.exists(), "web/index.html is missing"
    assert ROOT_INDEX.exists(), "index.html is missing at repository root"

    expected = render_root_index(WEB_INDEX.read_text(encoding="utf-8"))
    actual = ROOT_INDEX.read_text(encoding="utf-8")

    assert (
        actual == expected
    ), "Run `python -m tools.sync_index` to refresh the repository root index.html"
