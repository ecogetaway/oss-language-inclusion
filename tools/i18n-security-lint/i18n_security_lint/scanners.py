"""Security scanners for translated strings."""
import re
from dataclasses import dataclass
from typing import List, Optional

BIDI_CHARS = "\u202a\u202b\u202c\u202d\u202e\u2066\u2067\u2068\u2069"
_BIDI_RE = re.compile("[" + re.escape(BIDI_CHARS) + "]")

_XSS_RE = re.compile(
    r"(<script|</script|<iframe|javascript:|on\w+\s*=|<img|<svg|<body|<style)",
    re.IGNORECASE,
)

# Placeholder patterns: %s %d {0} {name} {{var}} $t(...) %(name)s
_PLACEHOLDER_RE = re.compile(
    r"(%[sd]|"  # printf style
    r"\{\d+\}|"  # numbered {0}
    r"\{\{?\w+\}?\}|"  # {{var}} or {var}
    r"\$\w+\(|\$[a-zA-Z_]\w*)"  # $t( or $var
)


@dataclass
class Finding:
    rule: str
    severity: str
    message: str


def scan_bidi(value: str) -> List[Finding]:
    findings = []
    for ch in value:
        if ch in BIDI_CHARS:
            findings.append(
                Finding(
                    rule="BIDI_OVERRIDE",
                    severity="high",
                    message=f"Unicode bidirectional control character U+{ord(ch):04X} detected",
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
    """Flag placeholder multiset drift between source and translation."""
    if not source:
        return []
    src = sorted(_PLACEHOLDER_RE.findall(source))
    dst = sorted(_PLACEHOLDER_RE.findall(translation))
    if src != dst:
        return [
            Finding(
                rule="PLACEHOLDER_DRIFT",
                severity="medium",
                message=f"Placeholder set mismatch: source={src} translation={dst}",
            )
        ]
    return []
