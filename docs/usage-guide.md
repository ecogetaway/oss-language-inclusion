# Usage Guide — i18n-security-lint

This guide explains how to install and run the translated-string security linter,
and how to wire it into CI.

## 1. Install

From the `tools/i18n-security-lint/` directory:

```bash
pip install -e .
```

This installs the `i18n-security-lint` command.

## 2. Scan locale files

```bash
# One or more files
i18n-security-lint locale/fr.po locale/es.json

# A whole directory (recursive glob)
i18n-security-lint "locale/**/*.po"

# Emit a JSON report (for dashboards / archiving)
i18n-security-lint --json locale/

# Fail the build on any finding (for CI)
i18n-security-lint --strict locale/
```

## 3. Understanding output

A clean run prints:

```
PASS: no translated-string security defects found.
```

A run with findings prints each file, location, and finding:

```
FAIL: translated-string security defects found:

== locale/ar.po
   locale/ar.po:'greeting'
     [HIGH] BIDI_OVERRIDE: Unicode bidirectional control character U+202B detected
     [HIGH] XSS_PAYLOAD: Possible XSS payload fragment: <script
   locale/ar.po:'welcome'
     [MEDIUM] PLACEHOLDER_DRIFT: Placeholder set mismatch: source=['%s'] translation=[]
```

Severities:

| Severity | Rule | Meaning |
| --- | --- | --- |
| high | `BIDI_OVERRIDE` | Bidirectional control char that can alter displayed text |
| high | `XSS_PAYLOAD` | Script/markup fragment that may execute when rendered |
| medium | `PLACEHOLDER_DRIFT` | Format specifier or interpolation variable changed vs source |

## 4. Supported formats

| Format | Extension | Source pair used |
| --- | --- | --- |
| JSON | `.json` | translation-only (bidi + XSS) |
| gettext | `.po` | `msgid` → `msgstr` (all checks) |
| XLIFF | `.xliff`, `.xlf` | `<target>` text (bidi + XSS) |
| Fluent | `.ftl` | `key = value` (bidi + XSS) |

For `.po`, the `msgid` is treated as the trusted source so format-specifier and
interpolation checks can compare against the translation. Translation-only
formats without a paired source run the bidi and XSS checks only.

## 5. CI integration (GitHub Action)

Add to `.github/workflows/i18n-security.yml`:

```yaml
name: i18n security lint
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install ./tools/i18n-security-lint
      - run: i18n-security-lint --strict "locale/**/*.po"
```

Or use the bundled action directly:

```yaml
- uses: ecogetaway/oss-language-inclusion/tools/i18n-security-lint@main
  with:
    path: "locale/"
    strict: "true"
```

## 6. Remediation workflow

1. Read the finding's rule and message.
2. Open the reported location in the locale file.
3. For `BIDI_OVERRIDE`: remove the control character unless bidirectional text
   is genuinely required (then terminate it properly).
4. For `XSS_PAYLOAD`: remove markup; ensure rendered locale content is sanitized.
5. For `PLACEHOLDER_DRIFT`: restore the exact placeholder set / variable names
   from the source string.
6. Re-run the linter until it reports `PASS`.

## 7. Reference corpus

`tools/i18n-security-lint/tests/corpus/` ships deliberately malformed strings
(`malicious.json`, `malicious.po`). Use them to verify your own CI or as a
fixture when building similar tooling.
