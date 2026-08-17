"""Security scanners for translated strings."""
import re
from dataclasses import dataclass
from typing import List, Optional

# Unicode bidirectional formatting characters (UAX #9).
#
# Two independent groups, with different terminators and different risk:
#   - Embeddings/overrides are popped by PDF (U+202C).
#   - Isolates are popped by PDI (U+2069).
#
# Isolates are the mechanism Unicode and W3C recommend; their presence is not a
# defect. Overrides are the Trojan Source vector; their presence always is.
# Written as escapes on purpose: this file must not itself contain invisible
# direction-changing characters.
LRE, RLE, PDF, LRO, RLO = "\u202a", "\u202b", "\u202c", "\u202d", "\u202e"
LRI, RLI, FSI, PDI = "\u2066", "\u2067", "\u2068", "\u2069"

_OVERRIDES = {LRO, RLO}
_EMBEDDINGS = {LRE, RLE}
_ISOLATE_INITIATORS = {LRI, RLI, FSI}

_BIDI_CHARS = _OVERRIDES | _EMBEDDINGS | _ISOLATE_INITIATORS | {PDF, PDI}

# Retained for callers that want to test "does this string carry any bidi
# control at all"; it is deliberately not the basis of a finding on its own.
BIDI_CHARS = "".join(sorted(_BIDI_CHARS))

_XSS_RE = re.compile(
    r"(<script|</script|<iframe|javascript:|on\w+\s*=|<img|<svg|<body|<style)",
    re.IGNORECASE,
)

# printf/gettext-family format specifiers: %s %d %i %u %f %x, positional %1$d,
# and named %(user)s.
_FORMAT_SPEC_RE = re.compile(r"%(?:\(\w+\)|\d+\$)?[sdiufxX]")

# Brace/template-family interpolation variables: {0} {name} {{var}} $t(key) $var.
# Longest alternatives first so {{var}} matches as one token.
_INTERPOLATION_RE = re.compile(
    r"\{\{\w+\}\}|\{\d+\}|\{\w+\}|\$t\([^)]*\)|\$[a-zA-Z_]\w*"
)


@dataclass
class Finding:
    rule: str
    severity: str
    message: str


def _describe(ch: str) -> str:
    names = {
        LRE: "LRE", RLE: "RLE", PDF: "PDF", LRO: "LRO", RLO: "RLO",
        LRI: "LRI", RLI: "RLI", FSI: "FSI", PDI: "PDI",
    }
    return f"U+{ord(ch):04X} ({names[ch]})"


def scan_bidi(value: str) -> List[Finding]:
    """Classify bidi control usage by kind and by balance, not by presence.

    Balanced isolates produce no finding: they are the recommended way to embed
    text of unknown direction. Overrides are always reported. Embeddings and
    isolates that are left unterminated are reported, because the unterminated
    control is what spills formatting into surrounding text.
    """
    findings: List[Finding] = []
    embed_depth = 0  # LRE/RLE/LRO/RLO ... PDF
    isolate_depth = 0  # LRI/RLI/FSI ... PDI
    stray_pdf = stray_pdi = False

    for ch in value:
        if ch in _OVERRIDES:
            embed_depth += 1
            findings.append(
                Finding(
                    rule="BIDI_OVERRIDE",
                    severity="high",
                    message=(
                        f"Bidirectional override {_describe(ch)}: displayed text "
                        "can differ from file content"
                    ),
                )
            )
        elif ch in _EMBEDDINGS:
            embed_depth += 1
            findings.append(
                Finding(
                    rule="BIDI_DEPRECATED_EMBEDDING",
                    severity="low",
                    message=(
                        f"Deprecated embedding {_describe(ch)}: prefer isolates "
                        "U+2066-U+2068 closed by U+2069"
                    ),
                )
            )
        elif ch == PDF:
            if embed_depth == 0:
                stray_pdf = True
            else:
                embed_depth -= 1
        elif ch in _ISOLATE_INITIATORS:
            isolate_depth += 1
        elif ch == PDI:
            if isolate_depth == 0:
                stray_pdi = True
            else:
                isolate_depth -= 1

    if embed_depth > 0:
        findings.append(
            Finding(
                rule="BIDI_UNBALANCED",
                severity="high",
                message=(
                    f"{embed_depth} unterminated embedding/override: needs "
                    "U+202C (PDF); direction leaks into surrounding text"
                ),
            )
        )
    if stray_pdf:
        findings.append(
            Finding(
                rule="BIDI_UNBALANCED",
                severity="high",
                message="Stray U+202C (PDF): no embedding or override to close",
            )
        )
    if isolate_depth > 0:
        findings.append(
            Finding(
                rule="BIDI_UNBALANCED",
                severity="high",
                message=(
                    f"{isolate_depth} unterminated isolate: needs U+2069 (PDI)"
                ),
            )
        )
    if stray_pdi:
        findings.append(
            Finding(
                rule="BIDI_UNBALANCED",
                severity="high",
                message="Stray U+2069 (PDI): no isolate initiator to close",
            )
        )

    return findings


def scan_xss(value: str) -> List[Finding]:
    m = _XSS_RE.search(value)
    if m:
        return [
            Finding(
                rule="XSS_PAYLOAD",
                severity="high",
                message=f"Possible XSS payload fragment: {m.group(1)}",
            )
        ]
    return []


def compare_placeholders(source: Optional[str], translation: str) -> List[Finding]:
    """Flag drift between source and translation, reported per placeholder family.

    Format specifiers and interpolation variables fail differently and are
    remediated differently, so they carry distinct rule ids.
    """
    findings: List[Finding] = []
    if not source:
        return findings

    for rule, regex, label in (
        ("FORMAT_SPECIFIER_DRIFT", _FORMAT_SPEC_RE, "Format specifier"),
        ("INTERPOLATION_DRIFT", _INTERPOLATION_RE, "Interpolation variable"),
    ):
        src = sorted(regex.findall(source))
        dst = sorted(regex.findall(translation))
        if src != dst:
            findings.append(
                Finding(
                    rule=rule,
                    severity="medium",
                    message=f"{label} set mismatch: source={src} translation={dst}",
                )
            )

    return findings
