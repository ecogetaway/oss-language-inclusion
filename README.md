# Open Source Language Inclusion
*From evidence base to shippable i18n infrastructure.*

Open source has standardized infrastructure for code contribution, but no equivalent infrastructure for language contribution. This repository studies that **language inclusion gap** with public case studies, then publishes the smallest reusable pieces the evidence supports.

| Piece | Role | Status |
| --- | --- | --- |
| [`signals/`](signals/) | Synthesized research patterns (markdown) | Active |
| [`spec/`](spec/) | Reusable specs — security checks, and a draft root declaration file | Security spec in use; [`i18n-signals.yml`](spec/i18n-signals.md) is a **v0.1 draft** |
| [`tools/i18n-security-lint`](tools/i18n-security-lint/) | CI scan for defects in translated strings | **Shipping** |
| [`tools/cldr-plural-check`](tools/cldr-plural-check/) | Plural-form completeness vs CLDR | **Planned — not implemented** |

**Provenance.** Part of the **OSS Infrastructure Initiative** (Sanjay C. and Aniruddh Raghavendra) — an evidence-first portfolio applying one method across three under-served open source contribution domains: internationalization, accessibility, and AI contribution. First published April 2026. Full portfolio under [Companion Projects](#companion-projects) below.

_Status: the most developed of the three domains — method published in CACM Blog and DevOps.com, with CI-ready tooling (`i18n-security-lint`). A root `i18n-signals.yml` declaration is a provisional draft under `spec/`. The CLDR plural checker is planned, not shipping._

_Built with AI-assisted drafting and research; every factual claim is independently verified against primary sources before publication._

[![PyPI](https://img.shields.io/pypi/v/i18n-security-lint)](https://pypi.org/project/i18n-security-lint/) [![CI](https://github.com/ecogetaway/oss-language-inclusion/actions/workflows/ci.yml/badge.svg)](https://github.com/ecogetaway/oss-language-inclusion/actions/workflows/ci.yml) [![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

## Quickstart — scan your locale files in 60 seconds

```bash
pip install i18n-security-lint
i18n-security-lint --strict locales/
```

![Demo: i18n-security-lint finds XSS, bidi overrides, and placeholder drift in locale files](docs/images/i18n-security-lint-demo.gif)

Real output (from this repository's test corpus):

```text
FAIL: translated-string security defects found:

== malicious.xlf
   malicious.xlf:7
     [HIGH] XSS_PAYLOAD: Possible XSS payload fragment: <img
   malicious.xlf:11
     [HIGH] BIDI_OVERRIDE: Unicode bidirectional control character U+202E detected
== interpolation.po
   interpolation.po:'Hello {userName}…'
     [MEDIUM] PLACEHOLDER_DRIFT: source=['{count}', '{userName}'] translation=['{count}', '{user_name}']
```

Exit code 1 under `--strict`, so it drops straight into CI. Formats: JSON, gettext `.po`, XLIFF, Fluent. Details: [`tools/i18n-security-lint`](tools/i18n-security-lint/).

### Try this first

| Priority | Action |
| --- | --- |
| **1. Primary** | `pip install i18n-security-lint` and scan your `locales/` (or `locale/`, `i18n/`) directory |
| **2. Secondary** | Drop the check into CI with the GitHub Action below |
| **3. Then** | [Open an issue](https://github.com/ecogetaway/oss-language-inclusion/issues/new/choose) with a false positive, a missed format, or your first real finding — that feedback shapes the next release |

**GitHub Action (copy-paste):**

```yaml
- uses: ecogetaway/oss-language-inclusion/tools/i18n-security-lint@main
  with:
    path: locales/
```

Please do **not** ask people to star the repo. The useful signal is an install, a CI run, or a filed finding.

Code contribution has mature shared workflows; language contribution often still depends on local process and maintainer capacity. The optional locale-file scanner above is one byproduct of that gap — not the whole project. For inclusion and review practice, start with [case studies](case-studies/), [problem-definition.md](problem-definition.md), and [RFC #7](https://github.com/ecogetaway/oss-language-inclusion/issues/7).

## Terminology used in this repo

- **signals** = synthesized research patterns in [`signals/`](signals/) (markdown)
- **`i18n-signals.yml`** = a *draft* root declaration file other projects may adopt; specified under [`spec/`](spec/i18n-signals.md), not the markdown in `signals/`
- **feedback** = raw input
- **contributors** = people

---

## Why Now

- Open-source AI tools are increasingly global.
- Non-English developer communities continue to grow.
- Localization demand appears in public issues and PRs without equivalent shared infrastructure.

---

## What This Is / What This Is Not

| What this is | What this is not |
| --- | --- |
| Early-stage investigation with primary-linked examples | Translation service or localization vendor |
| Structured evidence and signals repository | Final standards proposal |
| Maintainer and contributor input channel | Product pitch |

---
## Security Scope
Translated strings in open source software represent an under-recognized attack surface. Unlike code contributions, which pass through linters, static analysis, and CI pipelines, translated strings typically enter a codebase with no automated or standardized security review.
This repository documents four vulnerability classes introduced through unreviewed translated strings:
Unicode Bidirectional Override Attacks — Right-to-left control characters (U+202A–U+202E, U+2066–U+2069) can cause displayed text to differ from actual file content. In software used in legal, financial, or civic contexts, this creates a meaningful integrity risk.
Cross-Site Scripting (XSS) — HTML tags or JavaScript fragments embedded in translated strings can execute in web contexts where locale content is rendered without sanitization.
Format String Vulnerabilities — Translators may inadvertently add, remove, or rename format specifiers such as %s, {0}, or {{variable}}, causing crashes or undefined behaviour at runtime.
Interpolation Variable Integrity Failures — Variable names renamed or omitted during translation break string interpolation, with consequences ranging from empty UI strings to application crashes.
No existing i18n specification — including W3C, GNU gettext documentation, or ICU MessageFormat 2.0 — currently includes a standardized security checklist for translated strings. A primary deliverable of this project is to produce that checklist as a freely reusable, openly licensed artifact.

## Evidence

- [`case-studies/openclaw.md`](case-studies/openclaw.md)
- [`case-studies/contribution-evidence.md`](case-studies/contribution-evidence.md)
- [`problem-definition.md`](problem-definition.md)
- [RFC: do these OSS language-inclusion patterns match real l10n review practice?](https://github.com/ecogetaway/oss-language-inclusion/issues/7)

---
## Tools

This repository is expanding from an evidence base into runnable infrastructure. Tooling lives under `tools/`. Only `i18n-security-lint` is implemented and installable today.

### `tools/i18n-security-lint` — Translated-String Security Linter

A CLI and CI action that scans locale files (`.json`, `.po`, `.xliff`, Fluent) for the four vulnerability classes documented in [Security Scope](#security-scope):
- Unicode bidirectional override attacks
- Cross-site scripting (XSS) in rendered locale content
- Format-specifier tampering
- Interpolation-variable integrity failures

Status: **shipping** — all four checks implemented, with a test suite and CI (see `.github/workflows/ci.yml`) that runs the scanner against a corpus of malicious locale files on every push. Vulnerability reports: see [SECURITY.md](SECURITY.md).

### `tools/cldr-plural-check` — CLDR Plural-Rule Conformance Checker (planned)

**Planned, not implemented.** Intended to verify that a translation's plural forms match the CLDR rules for its language (e.g., Arabic's six forms, Hindi's zero-inclusive singular). It would pair with the security linter as a combined i18n quality gate. Do not treat this directory as a shipping tool.

Both tools are designed to be extracted into their own repositories later if an organization or adopter requests it.

### Draft spec — `i18n-signals.yml`

A provisional root-file spec so a project can declare whether it is ready to review language work (formats, expertise, readiness). Human write-up and examples: [`spec/i18n-signals.md`](spec/i18n-signals.md). No validator, badge, or GitHub Action yet.

## Signals from the Ecosystem

- [Maintainer Signals](signals/maintainer-signals.md)
- [Contributor Signals](signals/contributor-signals.md)
- [Signals Overview](signals/signals-overview.md)

---

## How to participate

See **[`CONTRIBUTING.md`](CONTRIBUTING.md)** for where to file issues, how to use templates, and how listing in [`contributors/README.md`](contributors/README.md) works (opt-in only).

- **Volunteer on-ramp (pinned):** [issue #6](https://github.com/ecogetaway/oss-language-inclusion/issues/6) — case studies, lint corpus, or signal notes. That issue is the entry point; first tasks are scoped from there.
- **Inclusion RFC:** [issue #7](https://github.com/ecogetaway/oss-language-inclusion/issues/7)
- Raw maintainer input: [`maintainer-feedback/README.md`](maintainer-feedback/README.md) → [open an issue](https://github.com/ecogetaway/oss-language-inclusion/issues/new/choose)
- Contributors index: [`contributors/README.md`](contributors/README.md)

---


## Repository structure

```
oss-language-inclusion/
├── README.md
├── CONTRIBUTING.md
├── problem-definition.md
├── roadmap.md
├── tools/
│   ├── i18n-security-lint/      # shipping
│   └── cldr-plural-check/       # planned
├── spec/
│   ├── translated-string-security-checks.md
│   ├── i18n-signals.md          # draft declaration spec
│   └── examples/
├── case-studies/
├── signals/
├── maintainer-feedback/
├── contributors/
└── .github/
    └── ISSUE_TEMPLATE/
```

## Sharing Community Feedback

If you have observations, experiences, or general comments related to OSS internationalization (i18n), localization workflows, multilingual contribution challenges, or translation tooling, feel free to open an issue using the `community-feedback` label.

Feedback does not need to be tied to a specific pull request or bug report. General contributor and maintainer experiences are also valuable.
Short notes, examples, and ecosystem observations are all welcome.


---

## Companion Projects

Three repositories, one method: document how a contribution domain actually fails in real repositories, then build the smallest machine-readable piece of infrastructure the evidence says is missing. Each domain's adoption compounds the others' credibility.

| Domain | Repository | What it builds | Maturity |
| --- | --- | --- | --- |
| Internationalization | [oss-language-inclusion](https://github.com/ecogetaway/oss-language-inclusion) | Language-inclusion evidence, shipping `i18n-security-lint`, draft `i18n-signals.yml` spec | Most developed; method published in CACM Blog and DevOps.com |
| Accessibility | [oss-accessibility-inclusion](https://github.com/ecogetaway/oss-accessibility-inclusion) | How accessibility PRs are reviewed; review rubric + draft `a11y-signals.yml` | Active |
| AI contribution | [oss-ai-contribution-policy](https://github.com/ecogetaway/oss-ai-contribution-policy) | Machine-readable `ai-contribution-policy.yml` standard (verification over detection) | Early evidence-gathering |

---

## Current Status



Case studies documented with upstream PR/issue links across Open WebUI, Kilocode, Hoppscotch, OpenClaw, and Hermes Agent.
-Signals split into maintainer, contributor, and overview files.
-Maintainer feedback and contributors now separated from signals.
-Article published: "Open Source's Hidden Language Gap," CACM Blog, May 2026.
-Article published: "What Five Localization Pull Requests Revealed About Open Source Governance," DevOps.com, June 2026.
-Project website: ossinfrainitiative.netlify.app
-Licensed under Apache 2.0.
- `i18n-security-lint` is shipping (PyPI + GitHub Action). `cldr-plural-check` remains a planned placeholder, not a shipping tool.
- Draft spec for a root `i18n-signals.yml` declaration lives under [`spec/i18n-signals.md`](spec/i18n-signals.md) (provisional v0.1; no validator yet).
