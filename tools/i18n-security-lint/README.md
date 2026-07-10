# i18n-security-lint

A command-line tool and CI action that scans locale files for security defects
introduced through unreviewed translated strings.

It checks the four vulnerability classes documented in the parent repository's
[Security Scope](https://github.com/ecogetaway/oss-language-inclusion#security-scope):

1. **Unicode bidirectional override attacks** — Right-to-left control characters
   (`U+202A`–`U+202E`, `U+2066`–`U+2069`) that make displayed text differ from
   actual file content.
2. **Cross-site scripting (XSS) in rendered locale content** — HTML/script
   fragments embedded in translated strings.
3. **Format-specifier tampering** — added, removed, or renamed placeholders
   (`%s`, `{0}`, `{{variable}}`) that cause crashes or undefined behaviour.
4. **Interpolation-variable integrity failures** — variable names renamed or
   omitted during translation, breaking string interpolation.

## Supported formats

| Format | Extension | Source pair used for checks 3–4 |
| --- | --- | --- |
| JSON | `.json` | translation-only (checks 1–2) |
| gettext | `.po` | `msgid` → `msgstr` (all checks) |
| XLIFF | `.xliff`, `.xlf` | `<target>` text (checks 1–2) |
| Fluent | `.ftl` | `key = value` (checks 1–2) |

## Install

```bash
pip install -e .
```

## Usage

```bash
# Scan one or more locale files
i18n-security-lint locale/*.po

# Scan a directory recursively, emit JSON, fail CI on any finding
i18n-security-lint --json --strict locale/
```

Exit code is `1` when `--strict` is set and at least one finding is reported,
so the tool drops straight into a CI pipeline.

## GitHub Action

```yaml
- uses: ecogetaway/oss-language-inclusion/tools/i18n-security-lint@main
  with:
    path: locale/
```

## Status

Working scaffolding. All four checks are implemented: bidi and XSS for every
supported format, format-specifier and interpolation-variable drift for `.po`
source/translation pairs. The test suite covers each check across JSON, gettext,
XLIFF, and Fluent corpus files, and the repository's CI dogfoods the scanner
against the malicious corpus on every push (it must flag every malicious file
and pass the clean one). This is the flagship security deliverable of the Open
Source Language Inclusion initiative, demonstrated as required.

Known limitations: detection is pattern-based, not parser-accurate — see the
repository's [SECURITY.md](../../SECURITY.md) for scope and how to report
bypasses.

## License

Apache-2.0 (inherited from the parent repository).
