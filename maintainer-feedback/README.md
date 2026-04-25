# Maintainer Feedback

This folder is a **lightweight invitation** for open-source maintainers, triagers, and release managers to describe **how internationalization (i18n) and localization actually behave** in their projects—what works, what fails quietly, and what would need to change for language work to be sustainable.

Nothing here asks you to endorse a particular tool, vendor, or roadmap. The goal is **shared situational awareness**: when many projects describe similar constraints in their own words, patterns become easier for foundations and upstream platforms to address without guessing.

---

## Why this matters

Maintainers already carry **security, compatibility, and review load**. Localization adds **parallel surface area** (strings, docs, errors, marketing copy, legal text) that can drift from releases, break UX, or sit in queues because no one has **linguistic review bandwidth**.

If those constraints stay implicit, funders and tool builders see only **merged PRs** or **silent absence** of locales—not the **process cost** you already pay. Short, concrete notes from maintainers help close that information gap without turning any single project into a spokesperson for the whole ecosystem.

---

## How you can contribute

Pick whatever fits your time and comfort level:

- **Open an issue** in [ecogetaway/oss-language-inclusion](https://github.com/ecogetaway/oss-language-inclusion/issues) with a neutral title (for example, “Maintainer note: i18n review bandwidth”) and link to **public** artifacts where possible (issues, PRs, policy docs).
- **Comment on an existing issue** if your experience matches a thread; discrete anecdotes are still useful when they reference verifiable links.
- **Point to prior art**—a blog post, conference talk, or foundation report—so readers can trace claims to primary sources.

If you cannot speak on the record, **generic patterns without naming a project** are still welcome, but please label them clearly as **non-attributable** so readers do not over-weight them as hard evidence.

---

## Example questions you might answer

- Have you faced **difficulty supporting localization** (incoming translations, community forks, or vendor proposals) alongside your normal release cadence?
- Is **review bandwidth** a binding constraint—especially for languages your core team does not read fluently?
- Do your **workflows or tools** feel insufficient for extraction, glossary management, translator context, or keeping docs and UI in sync?
- When you **defer or close** i18n-related contributions, what **public-facing reason** most closely matches the internal reality (architecture, legal, staffing, risk)?
- What **one change upstream** (in Git hosting, CI templates, foundation programs, or standards) would have helped your project most?

---

## Early observations

These are **starting hypotheses** from early desk research and public threads linked elsewhere in this repository—they are not survey results.

- **Capacity framing dominates** responsible refusals: maintainers often cite bandwidth, architecture readiness, or review depth rather than dismissing non-English audiences as unimportant.
- **Outcomes cluster** across merged work, long-open PRs, policy consolidation, and explicit “not yet” decisions—so “success” metrics that count only merges will **under-count friction**.
- **Cross-package and cross-surface** i18n (UI + CLI + docs) raises coordination cost in ways that **single-file locale patches** do not, which affects how fair it is to compare projects to one another.

---

## Credibility with foundations (Linux Foundation, Mozilla, and similar)

This repository is young. If the goal is to be taken seriously by **foundation-style** governance and program teams, three practical upgrades would help:

1. **Published editorial and evidence standards** — A short `docs/evidence-policy.md` (or equivalent) stating how case studies are sourced (primary links, date-stated snapshots, corrections policy) mirrors how foundations expect **claims to be checkable**, not only persuasive.

2. **Neutral governance shell** — A visible `CODE_OF_CONDUCT`, contribution/review expectations for this repo, and a simple **MAINTAINERS** or “who edits canonical narrative” note reduce perceived **single-author capture**—a common foundation concern for cross-ecosystem topics.

3. **Explicit non-goals and conflicts of interest** — A plain-language section on what this repo **will not** do (e.g. endorse one commercial TMS) and, where relevant, **affiliations / funding** of people who merge narrative text, aligns with how Mozilla, LF, and peer bodies document **bias risk** in neutral forums.

None of these require a large bureaucracy; they mainly make **intent and process legible** to readers who fund or standardize infrastructure.

---

*Repository root: [github.com/ecogetaway/oss-language-inclusion](https://github.com/ecogetaway/oss-language-inclusion) · Issues: [new issue](https://github.com/ecogetaway/oss-language-inclusion/issues/new)*
