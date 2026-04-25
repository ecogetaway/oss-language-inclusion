Open source has standardized infrastructure for code contribution, but no equivalent infrastructure for language contribution.

This repository explores whether language inclusion is a missing infrastructure layer in open source.

# Open Source Language Inclusion

**Early evidence suggests** a recurring tension: **code** changes benefit from shared norms (review, CI, bots, attribution), while **language** changes (UI, errors, documentation) often depend on **project-local improvisation** and **maintainer bandwidth**. This repository collects **primary-linked case notes** and **maintainer-facing prompts** so foundations, standards bodies, and digital public goods programs can assess the question empirically—not from marketing copy.

**Audience:** maintainers, foundations, standards organizations, DPG implementers. **Mode:** exploratory investigation, not a shipped program.

---

## Why Now

- **Open-source AI tools are becoming global infrastructure** for developers and operators; interfaces and docs remain unevenly localized in ways visible in public issue threads and PR queues.
- **Non-English developer communities are large and well documented** by major forges and industry analyses; this repo does not duplicate those datasets—it points to **where OSS contribution UX still defaults English-first**.
- **Localization demand shows up in public artifacts** (issues, open PRs, policy consolidations) **without** a cross-ecosystem equivalent to mature **code** contribution rails—**early evidence suggests** a **capacity and workflow** gap worth treating as infrastructure, not only as isolated project choices.

---

## What This Is / What This Is Not

| What this is | What this is not |
| -------------- | ------------------ |
| An **exploration** of a **possible** infrastructure gap between code and language contribution | A **translation project**, agency, or paid service |
| A **small, checkable evidence set** (case studies with upstream links) | A **finalized** technical proposal or standard |
| An **invitation** for maintainer experience and corrections | A **vendor** or **tool** endorsement |

---

## What’s Missing Today

Stated as **working observations** from desk research and linked primary sources—not exhaustive:

- **No standardized workflows** for i18n contributions comparable in reach to common code-review conventions.
- **No CI/CD-like shared pipelines** for linguistic quality (glossary, reviewer assignment, staleness across UI vs docs)—projects approximate this locally or not at all.
- **Limited cross-project tooling support**; much extraction and review remains **ad hoc** or **vendor-specific**.
- **Weak contributor recognition** for sustained linguistic review relative to code.
- **Heavy dependence on maintainer bandwidth** for triage, native review, and release alignment—often the explicit constraint in public maintainer statements.

---

## Evidence

- [`case-studies/openclaw.md`](case-studies/openclaw.md) — canonical upstream issue, maintainer-stated bandwidth.
- [`case-studies/contribution-evidence.md`](case-studies/contribution-evidence.md) — cross-project PR/issue states (Hindi-related examples preserved with links).
- [`problem-definition.md`](problem-definition.md) — working definition of the “language inclusion gap.”

---

## Potential Next Step

**Hypotheses only—no commitment from this repo:**

- The work **could** evolve into a **neutral working group** (foundation-hosted or multi-stakeholder) if institutions want shared problem framing.
- It **could** contribute to **documented workflows** (templates, review checklists, metadata conventions) *if* maintainers converge on repeatable patterns.
- It **could** inform **platform-level** discussions (e.g. forge features, grant criteria) **without** implying GitHub or any vendor has endorsed this investigation.

Institutional uptake requires governance, evidence policy, and neutral stewardship—see [`maintainer-feedback/README.md`](maintainer-feedback/README.md).

---

## How to engage

- **Maintainer notes:** [`maintainer-feedback/README.md`](maintainer-feedback/README.md) — optional structured format; [open an issue](https://github.com/ecogetaway/oss-language-inclusion/issues) with public links where possible.
- **Corrections:** preferred with citations to upstream issues/PRs/commits.

---

## Repository structure

```
oss-language-inclusion/
├── README.md
├── problem-definition.md
├── roadmap.md
├── case-studies/
├── maintainer-feedback/
│   └── README.md
└── contributors/
```

---

## Current Status

- **Case studies documented** with upstream URLs (Open WebUI, Kilo-Org/kilocode, Hoppscotch, Hermes Agent, OpenClaw—see `case-studies/`).
- **Seeking maintainer feedback** via issues and `maintainer-feedback/README.md`.
- **Early outreach underway**; no fixed roadmap or funded program embedded in this repository.

---

*https://github.com/ecogetaway/oss-language-inclusion*
