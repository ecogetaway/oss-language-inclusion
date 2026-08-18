# Translated-String Security Checks — Specification

This document specifies the checks performed by
[`tools/i18n-security-lint`](../tools/i18n-security-lint/). It is the machine-readable
companion to the parent repository's
[Security Scope](https://github.com/ecogetaway/oss-language-inclusion#security-scope)
and is intended to be referenced by maintainers, auditors, and CI pipelines.

Status: v0.2. All four check families are implemented. Placeholder checks
(CHECK-03, CHECK-04) require a paired source string and therefore run only on
formats that carry one — see [Format coverage](#format-coverage).

**Changed in v0.2 (breaking):** CHECK-01 no longer reports bidi controls on
presence alone, and the single `PLACEHOLDER_DRIFT` rule id has been split in
two. See [Changes from v0.1](#changes-from-v01) before upgrading a pinned CI
configuration.

---

## Scope

Translated strings enter production with no automated security review, unlike
code, which passes through linters, static analysis, and CI. This specification
defines the defect classes a locale-file linter should detect, the detection
method, severity, and remediation guidance.

Supported formats: `.json`, `.po`, `.xliff`/`.xlf`, `.ftl` (Fluent).

---

## CHECK-01 — Bidirectional Control Misuse

Unicode defines two independent families of bidirectional formatting control,
with different terminators and materially different risk. Treating them as one
undifferentiated class produces false positives on the mechanism that Unicode
and W3C actively recommend, so this check classifies by **kind** and by
**balance** rather than by presence.

| Family | Initiators | Terminator |
| --- | --- | --- |
| Embeddings | `U+202A` (LRE), `U+202B` (RLE) | `U+202C` (PDF) |
| Overrides | `U+202D` (LRO), `U+202E` (RLO) | `U+202C` (PDF) |
| Isolates | `U+2066` (LRI), `U+2067` (RLI), `U+2068` (FSI) | `U+2069` (PDI) |

`U+202C` and `U+2069` are **not** interchangeable: PDF pops an embedding or
override, PDI pops an isolate.

W3C's guidance is to prefer isolates: *"in an ideal world you would want to
follow the recommendation of the Unicode Standard to use RLI and LRI, and avoid
using RLE and LRE"*
([Unicode controls vs. markup for bidi support](https://www.w3.org/International/questions/qa-bidi-unicode-controls)).
A balanced isolate is therefore correct usage and **must not** be reported.

### CHECK-01a — Bidirectional Override

- **Rule id:** `BIDI_OVERRIDE`
- **Severity:** high
- **Detection:** any occurrence of `U+202D` or `U+202E`, whether or not it is
  terminated.
- **Rationale:** overrides force character direction regardless of content.
  This is the mechanism behind bidi source-code spoofing (Trojan Source,
  CVE-2021-42574), where displayed text differs from the underlying bytes.
- **Remediation:** remove the override. If the string genuinely needs to carry
  text of a different direction, wrap that run in an isolate
  (`U+2066`/`U+2067`/`U+2068` … `U+2069`) instead.

### CHECK-01b — Unbalanced Bidirectional Control

- **Rule id:** `BIDI_UNBALANCED`
- **Severity:** high
- **Detection:** an initiator left unterminated at end of string, or a
  terminator with no matching initiator, counted separately per family
  (embeddings/overrides against PDF; isolates against PDI).
- **Rationale:** an unterminated control does not stop at the end of the
  translated string. It leaks direction into whatever the application renders
  next, which is what makes surrounding UI text misleading.
- **Remediation:** terminate each initiator with the correct pop character —
  `U+202C` for embeddings and overrides, `U+2069` for isolates.

### CHECK-01c — Deprecated Embedding

- **Rule id:** `BIDI_DEPRECATED_EMBEDDING`
- **Severity:** low (advisory)
- **Detection:** any occurrence of `U+202A` or `U+202B`.
- **Rationale:** embeddings allow spillover effects that isolates were
  introduced to prevent. Balanced embeddings are legal, so this is advisory and
  is not intended to fail a build by itself.
- **Remediation:** migrate to isolates.

### Non-findings

A balanced isolate — `U+2066`/`U+2067`/`U+2068` closed by `U+2069` — produces
**no finding**. This is pinned by regression tests against
[`tests/corpus/bidi-safe.json`](../tools/i18n-security-lint/tests/corpus/bidi-safe.json),
which must scan clean.

### Conformance note

Balance is tracked as two independent counters, not a full implementation of the
Unicode Bidirectional Algorithm ([UAX #9](https://www.unicode.org/reports/tr9/)).
This is sufficient to detect unterminated and stray controls in a single
translated string, which is the unit a locale-file reviewer works with. It does
not model directional-status stack limits or paragraph-level resolution.

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
- **Known limitation:** this is a substring match, not a parser. Locale formats
  whose values legitimately contain markup will produce false positives.
  XLIFF `<target>` inner text is yielded raw during extraction precisely so that
  embedded markup reaches this check instead of being stripped before it runs.

---

## CHECK-03 — Format-Specifier Tampering

- **Rule id:** `FORMAT_SPECIFIER_DRIFT`
- **Severity:** medium
- **Description:** translators may add, remove, or retype printf-family format
  specifiers, causing runtime crashes or undefined behaviour when the
  application substitutes values.
- **Detection:** compare the multiset of format specifiers in the source string
  against the translation. Recognised forms: `%s`, `%d`, `%i`, `%u`, `%f`,
  `%x`, `%X`, positional `%1$d`, and named `%(count)s`.
- **Example (malicious):**
  ```
  source:  "Your balance is %d"
  trans:   "Your balance is %s"   # type changed -> drift
  ```
- **Remediation:** keep the specifier set identical to source. If the target
  language's grammar requires reordering, use positional specifiers (`%1$d`)
  rather than changing the set — reordering alone is not reported as drift.

---

## CHECK-04 — Interpolation-Variable Integrity Failure

- **Rule id:** `INTERPOLATION_DRIFT`
- **Severity:** medium
- **Description:** variable names used in brace- and template-style
  interpolation may be renamed or omitted during translation, producing empty
  UI strings or application crashes.
- **Detection:** multiset comparison over the interpolation family, evaluated
  independently of CHECK-03 so the two failure modes are separately
  actionable. Recognised forms: `{0}`, `{name}`, `{{var}}`, `$t(key)`, `$var`.
- **Example (malicious):**
  ```
  source:  "Welcome {user} to {app}"
  trans:   "Welcome {user} to the app"   # {app} dropped -> broken interpolation
  ```
- **Remediation:** preserve interpolation variable names exactly; only the
  surrounding natural-language text should be translated.

---

## Format coverage

CHECK-03 and CHECK-04 require a source/translation pair. Formats that carry
translation text only are scanned for CHECK-01 and CHECK-02 and are silently
skipped for the placeholder checks.

| Format | Extension | Source pair available | Checks applied |
| --- | --- | --- | --- |
| gettext | `.po` | `msgid` → `msgstr` | 01, 02, 03, 04 |
| JSON | `.json` | no | 01, 02 |
| XLIFF | `.xliff`, `.xlf` | no | 01, 02 |
| Fluent | `.ftl` | no | 01, 02 |

---

## Severity & Exit Semantics

| Severity | Rules | CI default |
| --- | --- | --- |
| high | `BIDI_OVERRIDE`, `BIDI_UNBALANCED`, `XSS_PAYLOAD` | fail build |
| medium | `FORMAT_SPECIFIER_DRIFT`, `INTERPOLATION_DRIFT` | fail build (configurable) |
| low | `BIDI_DEPRECATED_EMBEDDING` | advisory |

With `--strict`, the linter exits `1` on any finding, including advisory ones,
so it drops into CI. Per-severity thresholds are not yet configurable.

---

## Reference Corpus

A corpus of deliberately malformed and deliberately correct translated strings
ships with the tool at
[`tools/i18n-security-lint/tests/corpus/`](../tools/i18n-security-lint/tests/corpus/):

| File | Purpose |
| --- | --- |
| `malicious.json` | overrides, unterminated embeddings, a stray pop, XSS |
| `malicious.po` | format-specifier drift and interpolation drift |
| `bidi-safe.json` | balanced isolates and balanced embeddings — must scan clean |

The safe fixture matters as much as the malicious ones: it is what prevents the
checker from regressing into flagging correct bidi usage. The corpus is intended
as a reusable test fixture for any locale-file security tool.

---

## Changes from v0.1

| v0.1 | v0.2 |
| --- | --- |
| `BIDI_OVERRIDE` on any of `U+202A`–`U+202E`, `U+2066`–`U+2069` | split into `BIDI_OVERRIDE`, `BIDI_UNBALANCED`, `BIDI_DEPRECATED_EMBEDDING`; balanced isolates no longer reported |
| `PLACEHOLDER_DRIFT` for both placeholder families | `FORMAT_SPECIFIER_DRIFT` and `INTERPOLATION_DRIFT` |

Both changes alter emitted rule ids and will affect any CI configuration that
filters on them.

---

## Relationship to Other Work

- **Parent security checklist:** see
  [Security Scope](https://github.com/ecogetaway/oss-language-inclusion#security-scope)
  in the repository README.
- **Companion tool:** `tools/cldr-plural-check/` (CLDR plural-rule conformance)
  is planned and not yet implemented; when it lands it forms a combined "i18n
  quality gate" alongside this linter.
- **Unicode UTS #55 ([Source Code Handling](https://www.unicode.org/reports/tr55/))**
  covers bidirectional ordering spoofs, confusables, and line-break spoofs in
  **source code**, and informs CHECK-01. This specification addresses the
  adjacent and so far unspecified surface: **locale resource files** reviewed as
  translation artifacts rather than as code.
- **UAX #9 ([Unicode Bidirectional Algorithm](https://www.unicode.org/reports/tr9/))**
  defines the control characters and their scoping.
- **W3C Internationalization** publishes authoring guidance on bidi controls
  versus markup, which CHECK-01 follows.
- **Other i18n specifications** (GNU gettext, ICU MessageFormat 2.0, XLIFF)
  define format and message syntax but do not define a security review
  checklist for the translated strings carried in those formats. This
  specification is offered as a freely reusable, openly licensed artifact.
