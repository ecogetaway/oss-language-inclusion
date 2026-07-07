"""CLI entry point for i18n-security-lint."""
import argparse
import glob
import json
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List

from .extract import extract
from .scanners import Finding, compare_placeholders, scan_bidi, scan_xss


def _scan_file(path: Path) -> Dict[str, List[Finding]]:
    results: Dict[str, List[Finding]] = {}
    for entry in extract(path):
        found: List[Finding] = []
        found += scan_bidi(entry.value)
        found += scan_xss(entry.value)
        found += compare_placeholders(entry.source, entry.value)
        if found:
            results[entry.location] = found
    return results


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="i18n-security-lint",
        description="Scan locale files for translated-string security defects.",
    )
    parser.add_argument("paths", nargs="+", help="Files or glob patterns to scan")
    parser.add_argument("--json", action="store_true", help="Emit JSON report")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 1 if any finding is reported",
    )
    args = parser.parse_args(argv)

    files: List[Path] = []
    for pattern in args.paths:
        matches = [Path(p) for p in glob.glob(pattern, recursive=True)]
        files.extend(matches if matches else [Path(pattern)])
    files = [f for f in files if f.exists() and f.is_file()]

    total: Dict[str, Dict[str, List[Finding]]] = {}
    finding_count = 0
    for f in files:
        file_findings = _scan_file(f)
        if file_findings:
            total[str(f)] = {
                loc: [asdict(x) for x in fnd] for loc, fnd in file_findings.items()
            }
            finding_count += sum(len(v) for v in file_findings.values())

    if args.json:
        print(json.dumps(total, indent=2, ensure_ascii=False))
    else:
        if not total:
            print("PASS: no translated-string security defects found.")
        else:
            print("FAIL: translated-string security defects found:\n")
            for fname, locs in total.items():
                print(f"== {fname}")
                for loc, fnds in locs.items():
                    print(f"   {loc}")
                    for fnd in fnds:
                        print(f"     [{fnd['severity'].upper()}] {fnd['rule']}: {fnd['message']}")

    if args.strict and finding_count:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
