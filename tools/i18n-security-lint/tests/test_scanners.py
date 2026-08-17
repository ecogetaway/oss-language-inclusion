import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from i18n_security_lint.extract import extract
from i18n_security_lint.scanners import (
    compare_placeholders,
    scan_bidi,
    scan_xss,
)

CORPUS = Path(__file__).parent / "corpus"

LRI, RLI, FSI, PDI = "\u2066", "\u2067", "\u2068", "\u2069"
LRE, RLE, PDF, LRO, RLO = "\u202a", "\u202b", "\u202c", "\u202d", "\u202e"


def _rules(findings):
    return {f.rule for f in findings}


# --- CHECK-01: classification by kind and balance -------------------------


def test_balanced_isolates_produce_no_findings():
    """The mechanism Unicode and W3C recommend must not be reported as a defect."""
    for wrapped in (
        f"Reply to {LRI}user@example.com{PDI} today",
        f"Opening {FSI}file.txt{PDI} now",
        f"Contact {RLI}name{PDI} for access",
    ):
        assert scan_bidi(wrapped) == [], f"false positive on {wrapped!r}"


def test_safe_corpus_file_is_clean():
    findings = [f for e in extract(CORPUS / "bidi-safe.json") for f in scan_bidi(e.value)]
    assert findings == [], f"expected clean, got {[f.rule for f in findings]}"


def test_override_is_high_severity():
    findings = scan_bidi(f"Amount: 1000{RLO} USD{PDF}")
    override = [f for f in findings if f.rule == "BIDI_OVERRIDE"]
    assert len(override) == 1
    assert override[0].severity == "high"


def test_override_reported_even_when_balanced():
    """Overrides are a defect on presence, not only when unterminated."""
    findings = scan_bidi(f"a{LRO}b{PDF}c")
    assert "BIDI_OVERRIDE" in _rules(findings)
    assert "BIDI_UNBALANCED" not in _rules(findings)


def test_unterminated_embedding_is_unbalanced():
    findings = scan_bidi(f"Right{LRE}to{RLE}left")
    assert "BIDI_UNBALANCED" in _rules(findings)


def test_unterminated_isolate_is_unbalanced():
    findings = scan_bidi(f"Open {LRI}user@example.com now")
    assert "BIDI_UNBALANCED" in _rules(findings)


def test_stray_pop_is_unbalanced():
    assert "BIDI_UNBALANCED" in _rules(scan_bidi(f"trailing{PDI}pop"))
    assert "BIDI_UNBALANCED" in _rules(scan_bidi(f"trailing{PDF}pop"))


def test_balanced_embedding_is_low_advisory_only():
    findings = scan_bidi(f"Paid {RLE}500{PDF} rupees")
    assert _rules(findings) == {"BIDI_DEPRECATED_EMBEDDING"}
    assert all(f.severity == "low" for f in findings)


def test_malicious_corpus_still_flags_high():
    findings = [f for e in extract(CORPUS / "malicious.json") for f in scan_bidi(e.value)]
    assert any(f.severity == "high" for f in findings)
    assert "BIDI_OVERRIDE" in _rules(findings)


# --- CHECK-02: XSS ---------------------------------------------------------


def test_xss_detected_in_json():
    findings = [f for e in extract(CORPUS / "malicious.json") for f in scan_xss(e.value)]
    assert any(f.rule == "XSS_PAYLOAD" for f in findings)


# --- CHECK-03 / CHECK-04: distinct rule ids --------------------------------


def test_format_specifier_drift_has_its_own_rule():
    findings = compare_placeholders("Your balance is %d", "Your balance is %s")
    assert _rules(findings) == {"FORMAT_SPECIFIER_DRIFT"}


def test_interpolation_drift_has_its_own_rule():
    findings = compare_placeholders("Welcome {user} to {app}", "Welcome {user} to the app")
    assert _rules(findings) == {"INTERPOLATION_DRIFT"}


def test_drift_families_are_independent():
    """A format-only defect must not raise an interpolation finding, and vice versa."""
    fmt = compare_placeholders("%d files in {folder}", "%s files in {folder}")
    assert _rules(fmt) == {"FORMAT_SPECIFIER_DRIFT"}

    interp = compare_placeholders("%d files in {folder}", "%d files in the folder")
    assert _rules(interp) == {"INTERPOLATION_DRIFT"}


def test_positional_and_named_specifiers_are_recognised():
    """The spec recommends positional specifiers, so they must not read as drift."""
    assert compare_placeholders("Show %1$s and %2$s", "Show %1$s and %2$s") == []
    assert compare_placeholders("Deleted %(count)s files", "%(count)s files deleted") == []


def test_reordering_is_not_drift():
    assert compare_placeholders("{a} then {b}", "{b} then {a}") == []


def test_no_source_means_no_finding():
    assert compare_placeholders(None, "Welcome %s") == []


def test_po_corpus_exercises_both_families():
    """Each drift family has its own corpus file; neither may raise the other's rule."""
    fmt = {
        f.rule
        for e in extract(CORPUS / "malicious.po")
        for f in compare_placeholders(e.source, e.value)
    }
    assert fmt == {"FORMAT_SPECIFIER_DRIFT"}

    interp = {
        f.rule
        for e in extract(CORPUS / "interpolation.po")
        for f in compare_placeholders(e.source, e.value)
    }
    assert interp == {"INTERPOLATION_DRIFT"}


def test_clean_corpus_stays_clean():
    for entry in extract(CORPUS / "clean.json"):
        assert scan_bidi(entry.value) == []
        assert scan_xss(entry.value) == []
