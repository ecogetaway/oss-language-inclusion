"""Coverage for the remaining check/format combinations beyond test_bidi.py:
interpolation-variable drift, XLIFF and Fluent extraction, and CLI exit codes."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from i18n_security_lint.cli import main
from i18n_security_lint.extract import extract
from i18n_security_lint.scanners import compare_placeholders, scan_bidi, scan_xss

CORPUS = Path(__file__).parent / "corpus"


def test_interpolation_variable_drift_in_po():
    # {userName} renamed to {user_name} in the translation must be flagged.
    entries = list(extract(CORPUS / "interpolation.po"))
    drift = [f for e in entries for f in compare_placeholders(e.source, e.value)]
    assert any(f.rule == "PLACEHOLDER_DRIFT" for f in drift)


def test_matching_interpolation_variables_pass():
    # {email} kept identical in source and translation must NOT be flagged.
    entries = [e for e in extract(CORPUS / "interpolation.po") if "{email}" in e.value]
    assert entries, "corpus entry with {email} not extracted"
    assert not [f for e in entries for f in compare_placeholders(e.source, e.value)]


def test_xss_detected_in_xliff_target():
    # Regression test for the extractor bug where markup was stripped from
    # <target> before scanning, deleting the payload the scanner looks for.
    findings = [f for e in extract(CORPUS / "malicious.xlf") for f in scan_xss(e.value)]
    assert any(f.rule == "XSS_PAYLOAD" for f in findings)


def test_bidi_detected_in_xliff_target():
    findings = [f for e in extract(CORPUS / "malicious.xlf") for f in scan_bidi(e.value)]
    assert any(f.rule == "BIDI_OVERRIDE" for f in findings)


def test_xss_and_bidi_detected_in_fluent():
    entries = list(extract(CORPUS / "malicious.ftl"))
    assert any(f.rule == "XSS_PAYLOAD" for e in entries for f in scan_xss(e.value))
    assert any(f.rule == "BIDI_OVERRIDE" for e in entries for f in scan_bidi(e.value))


def test_cli_strict_fails_on_malicious_corpus(capsys):
    exit_code = main(["--strict", str(CORPUS / "malicious.json")])
    assert exit_code == 1
    assert "FAIL" in capsys.readouterr().out


def test_cli_strict_passes_on_clean_file(capsys):
    exit_code = main(["--strict", str(CORPUS / "clean.json")])
    assert exit_code == 0
    assert "PASS" in capsys.readouterr().out


def test_cli_json_output_is_valid_json(capsys):
    main(["--json", str(CORPUS / "malicious.json")])
    report = json.loads(capsys.readouterr().out)
    assert report, "expected findings in JSON report"
