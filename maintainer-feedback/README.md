# Maintainer Feedback

This folder invites **open-source maintainers, triagers, and release managers** to describe **how i18n and localization actually behave** in their projects: what works, what stalls, and what would need to change for language work to be sustainable.

The goal is **shared situational awareness** for foundations, standards bodies, and digital public goods programs—**not** advocacy for a specific vendor stack.

---

## Why maintainer input matters

Public **issues and PRs** show *that* people offer translations; they rarely explain **review load**, **risk tradeoffs**, or **architecture sequencing** in one place. **Short, sourced notes from people who merge or triage** help institutions see **process cost** instead of inferring from star counts or merge rates alone.

**Early evidence suggests** repeated public rationales (bandwidth, architecture readiness, review depth) cluster across unrelated repositories—but **this repo does not substitute for a formal survey**; it aggregates pointers and invites structured anecdotes.

---

## How to contribute

1. Prefer **public links** (issues, PRs, `CONTRIBUTING.md`, governance docs) so readers can verify claims.
2. Open an issue in [`ecogetaway/oss-language-inclusion`](https://github.com/ecogetaway/oss-language-inclusion/issues) or paste the template below into a **gist** and link it from an issue if you need formatting.
3. Label **non-attributable** anecdotes clearly if you cannot name a project; treat them as **hypothesis-generating**, not evidence equal to URLs.

**Optional — copy/paste issue body:**

```text
Project:
Role: (e.g. maintainer / triager / translator coordinator)
Challenge: (1–3 sentences; link to public threads if possible)
What would help: (concrete: tooling, funding, policy, platform feature, etc.)
Public links:
```

**Example (illustrative structure only—not a real submission):**

```text
Project: (example) sample-org/sample-app
Role: maintainer
Challenge: Hindi locale PRs wait weeks; only one reviewer reads Hindi; docs and UI strings drift.
What would help: documented review SLA for i18n; shared glossary format; foundation micro-grant for native review.
Public links: https://github.com/sample-org/sample-app/issues/123
```

---

## Example questions you might answer

- Have you faced **difficulty supporting localization** alongside your release cadence?
- Is **review bandwidth** a binding constraint for languages your core team does not read fluently?
- Are **workflows or tools** insufficient for extraction, glossary management, or UI/docs parity?
- When you **defer or close** i18n-related contributions, what **public-facing reason** best matches internal reality?
- What **one upstream change** (forge, CI template, foundation program, standard) would have helped most?

---

## Early observations

**Hypotheses from desk research**, not survey results:

- **Capacity framing** dominates responsible deferrals in public maintainer text.
- Outcomes **cluster** across merged work, long-open PRs, policy consolidation, and explicit “not yet” decisions—metrics that count only merges **under-count friction**.
- **Cross-surface** i18n (UI + CLI + docs) raises coordination cost compared with **single-file** locale patches—comparisons across projects should account for that.

---

## Credibility with foundations (Linux Foundation, Mozilla, and similar)

Practical upgrades that would strengthen **institution-facing** rigor (none are promises from this repo):

1. **`docs/evidence-policy.md`** — how case studies are sourced, dated, and corrected.
2. **`CODE_OF_CONDUCT`**, contribution expectations, and a **`MAINTAINERS`** note — reduce perceived single-author capture.
3. **Explicit non-goals and conflicts of interest** — what this repo will not do; affiliations/funding of people who merge narrative text.

---

*Repository: [github.com/ecogetaway/oss-language-inclusion](https://github.com/ecogetaway/oss-language-inclusion) · [New issue](https://github.com/ecogetaway/oss-language-inclusion/issues/new)*
