Open source has standardized infrastructure for code contribution, but no equivalent infrastructure for language contribution.

This repository explores whether language inclusion is a missing infrastructure layer in open source.

# Open Source Language Inclusion

**Early evidence suggests** a recurring pattern: code contribution has mature shared workflows, while language contribution often depends on local process and maintainer capacity.

## Terminology used in this repo

- **signals** = synthesized patterns
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

---

## Signals from the Ecosystem

- [Maintainer Signals](signals/maintainer-signals.md)
- [Contributor Signals](signals/contributor-signals.md)
- [Signals Overview](signals/signals-overview.md)

---

## How to participate

See **[`CONTRIBUTING.md`](CONTRIBUTING.md)** for where to file issues, how to use templates, and how listing in [`contributors/README.md`](contributors/README.md) works (opt-in only).

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
├── case-studies/
├── signals/
├── maintainer-feedback/
├── contributors/
└── .github/ISSUE_TEMPLATE/
```

---
## ## Sharing Community Feedback

If you have observations, experiences, or general comments related to OSS internationalization (i18n), localization workflows, multilingual contribution challenges, or translation tooling, feel free to open an issue using the `community-feedback` label.

Feedback does not need to be tied to a specific pull request or bug report. General contributor and maintainer experiences are also valuable.
Short notes, examples, and ecosystem observations are all welcome.


---

## Current Status



Case studies documented with upstream PR/issue links across Open WebUI, Kilocode, Hoppscotch, OpenClaw, and Hermes Agent.
-Signals split into maintainer, contributor, and overview files.
-Maintainer feedback and contributors now separated from signals.
-Article published: "Open Source's Hidden Language Gap," CACM Blog, May 2026.
-Article published: "What Five Localization Pull Requests Revealed About Open Source Governance," DevOps.com, June 2026.
-Project website: ossinfrainitiative.netlify.app
-Licensed under Apache 2.0.
