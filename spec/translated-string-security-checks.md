# Translated-String Security Checks — Specification

This document specifies the checks performed by
[`tools/i18n-security-lint`](../tools/i18n-security-lint/). It is the machine-readable
companion to the parent repository's
[Security Scope](https://github.com/ecogetaway/oss-language-inclusion#security-scope)
and is intended to be referenced by maintainers, auditors, and CI pipelines.

Status: v0.1 (scaffolding). The bidirectional-override check is the first and
highest-signal implementation; format, interpolation, and XSS checks are
implemented for `.po` source/translation pairs and basic JSON/XLIFF/Fluent text.

---

## Scope

Translated strings enter production with no automated security review, unlike
code, which passes through linters, static analysis, and CI. This specification
defines the defect classes a locale-file linter should detect, the detection
method, severity, and remediation guidance.

Supported formats: `.json`, `.po`, `.xliff`/`.xlf`, `.ftl` (Fluent).

---

## CHECK-01 — Unicode Bidirectional Override

- **Rule id:** `BIDI_OVERRIDE`
- **Severity:** high
- **Description:** Right-to-left override control characters can make displayed
  text differ from the actual file content. In legal, financial, or civic
  software this is an integrity risk (e.g., a translated label that *appears*
  to say one thing but *contains* a different instruction or value).
- **Detection:** flag any occurrence of the ranges
  `U+202A`–`U+202E` and `U+2066`–`U+2069`.
- **Example (malicious):**
  ```
  "Click ‮revres olleh‮ to continue"
  ```
  Displays left-to-right as benign text while the underlying buffer is reversed.
- **Remediation:** remove the control characters unless the locale legitimately
  requires bidirectional text; if required, isolate them with matching
  `U+202C`/`U+2069` terminators and document the intent.

---

## CHECK-02 — Cross-Site Scripting (XSS) in Rendered Locale Content

- **Rule id:** `XSS_PAYLOAD`
- **Severity:** high
- **Description:** HTML tags or script fragments embedded in translated strings
  can execute where locale content is rendered without sanitization (web UIs,
  email templates, rich-text surfaces).
- **Detection:** flag substrings matching
  `<script`, `</script`, `<iframe`, `javascript:`, `on\w+=`, `<img`, `<svg`,
  `<body`, `<style` (case-insensitive).
- **Example (malicious):**
  ```
  "Hello <script>alert(1)</script>"
  ```
- **Remediation:** sanitize all rendered locale content; treat translator
  input as untrusted. Prefer translation systems that disallow markup or
  escape it by default.

---

## CHECK-03 — Format-Specifier Tampering

- **Rule id:** `PLACEHOLDER_DRIFT`
- **Severity:** medium
- **Description:** Translators may add, remove, or rename format specifiers
  (`%s`, `%d`, `{0}`, `{{variable}}`), causing runtime crashes or undefined
  behaviour when the application substitutes values.
- **Detection:** compare the multiset of placeholders in the source string
  against the translation. Source is available for `.po` (`msgid` → `msgstr`);
  for translation-only formats without a paired source, this check is skipped
  and a manual review note is emitted.
- **Example (malicious):**
  ```
  source:  "Your balance is %d"
  trans:   "Your balance is %s"   # type changed -> drift
  ```
- **Remediation:** keep the placeholder set identical to source; if the target
  language's grammar requires reordering, use positional specifiers
  (`%1$d`) rather than changing the set.

---

## CHECK-04 — Interpolation-Variable Integrity Failure

- **Rule id:** `PLACEHOLDER_DRIFT` (shared with CHECK-03)
- **Severity:** medium
- **Description:** Variable names used in string interpolation may be renamed or
  omitted during translation, producing empty UI strings or application crashes.
- **Detection:** same placeholder-multiset comparison as CHECK-03, covering
  named forms (`{name}`, `{{var}}`, `$t(...)`, `$var`).
- **Example (malicious):**
  ```
  source:  "Welcome {user} to {app}"
  trans:   "Welcome {user} to the app"   # {app} dropped -> broken interpolation
  ```
- **Remediation:** preserve interpolation variable names exactly; only the
  surrounding natural-language text should be translated.

---

## Severity & Exit Semantics

| Severity | CI default |
| --- | --- |
| high (BIDI_OVERRIDE, XSS_PAYLOAD) | fail build |
| medium (PLACEHOLDER_DRIFT) | fail build (configurable) |

With `--strict`, the linter exits `1` on any finding so it drops into CI.

---

## Reference Corpus

The first public corpus of deliberately malformed translated strings ships with
the tool at
[`tools/i18n-security-lint/tests/corpus/`](../tools/i18n-security-lint/tests/corpus/)
(`malicious.json`, `malicious.po`). It is intended as a reusable test fixture
for any locale-file security tool.

---

## Relationship to Other Work

- **Parent security checklist:** see
  [Security Scope](https://github.com/ecogetaway/oss-language-inclusion#security-scope)
  in the repository README.
- **Companion tool:** `tools/cldr-plural-check/` (CLDR plural-rule conformance)
  forms a combined "i18n quality gate" when run alongside this linter.
- **Upstream specs:** W3C Internationalization, GNU gettext, ICU MessageFormat 2.0
  — none currently define a standardized security checklist for translated
  strings; this specification is a freely reusable, openly licensed artifact.
