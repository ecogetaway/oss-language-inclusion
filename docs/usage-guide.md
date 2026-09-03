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

# A whole directory: walked recursively, picking up every supported
# locale format (.json, .po, .xliff/.xlf, .ftl) and ignoring everything else
i18n-security-lint locale/

# Or narrow it with an explicit glob
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
     [HIGH] BIDI_OVERRIDE: Bidirectional override U+202E (RLO): displayed text can differ from file content
     [HIGH] XSS_PAYLOAD: Possible XSS payload fragment: <script
   locale/ar.po:'welcome'
     [MEDIUM] FORMAT_SPECIFIER_DRIFT: Format specifier set mismatch: source=['%s'] translation=[]
```

Severities:

| Severity | Rule | Meaning |
| --- | --- | --- |
| high | `BIDI_OVERRIDE` | Direction override (`U+202D`/`U+202E`) that can make displayed text differ from file content |
| high | `BIDI_UNBALANCED` | Bidi control left unterminated, or a terminator with no initiator |
| high | `XSS_PAYLOAD` | Script/markup fragment that may execute when rendered |
| medium | `FORMAT_SPECIFIER_DRIFT` | printf-family specifier (`%s`, `%1$d`, `%(name)s`) changed vs source |
| medium | `INTERPOLATION_DRIFT` | Interpolation variable (`{0}`, `{name}`, `{{var}}`) changed vs source |
| low | `BIDI_DEPRECATED_EMBEDDING` | Balanced embedding (`U+202A`/`U+202B`); legal, but isolates are preferred |

Balanced isolates (`U+2066`–`U+2069`) are correct usage and produce no finding.

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
- uses: ecogetaway/oss-language-inclusion/tools/i18n-security-lint@v0.2.1
  with:
    path: "locale/"
    strict: "true"
```

## 6. Remediation workflow

1. Read the finding's rule and message.
2. Open the reported location in the locale file.
3. For `BIDI_OVERRIDE`: remove the override. If the string must carry text of a
   different direction, wrap that run in an isolate (`U+2066`/`U+2067`/`U+2068`
   … `U+2069`) instead.
4. For `BIDI_UNBALANCED`: add the correct terminator — `U+202C` closes an
   embedding or override, `U+2069` closes an isolate. They are not
   interchangeable.
5. For `XSS_PAYLOAD`: remove markup; ensure rendered locale content is sanitized.
6. For `FORMAT_SPECIFIER_DRIFT` / `INTERPOLATION_DRIFT`: restore the exact
   specifier set or variable names from the source string. Reordering is
   allowed and is not reported; use positional specifiers (`%1$d`) if the target
   grammar needs a different order.
7. Re-run the linter until it reports `PASS`.

## 7. Reference corpus

`tools/i18n-security-lint/tests/corpus/` ships both deliberately malformed and
deliberately correct strings:

| File | Expectation |
| --- | --- |
| `malicious.json` | override, unterminated embeddings, a stray pop, XSS — must FAIL |
| `malicious.po` | format-specifier drift — must FAIL |
| `interpolation.po` | interpolation-variable drift — must FAIL |
| `malicious.xlf` | XSS and an override in `<target>` — must FAIL |
| `malicious.ftl` | XSS and an override in a Fluent value — must FAIL |
| `clean.json` | ordinary strings, no defects — must PASS |
| `bidi-safe.json` | balanced isolates — must PASS |

Use them to verify your own CI or as a fixture when building similar tooling.
The safe fixture is the important one: it is what stops a checker regressing
into flagging correct bidi usage.
