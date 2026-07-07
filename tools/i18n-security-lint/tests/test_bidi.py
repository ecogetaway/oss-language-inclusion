import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from i18n_security_lint.extract import extract
from i18n_security_lint.scanners import scan_bidi, scan_xss, compare_placeholders

CORPUS = Path(__file__).parent / "corpus"


def test_bidi_detected_in_json():
    findings = [f for e in extract(CORPUS / "malicious.json") for f in scan_bidi(e.value)]
    assert any(f.rule == "BIDI_OVERRIDE" for f in findings)


def test_xss_detected_in_json():
    findings = [f for e in extract(CORPUS / "malicious.json") for f in scan_xss(e.value)]
    assert any(f.rule == "XSS_PAYLOAD" for f in findings)


def test_placeholder_drift_in_po():
    po = list(extract(CORPUS / "malicious.po"))
    drift = [f for e in po for f in compare_placeholders(e.source, e.value)]
    assert any(f.rule == "PLACEHOLDER_DRIFT" for f in drift)
