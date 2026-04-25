# Language inclusion gap in open source

This document gives a **working definition** for use inside this repository. It is **not** a consensus definition of any foundation or standards body.

---

## Definition

The **language inclusion gap in open source** is the **systemic difficulty** of making **linguistic contribution** (translation, localization, multilingual documentation, culturally appropriate UX copy) as **predictable, reviewable, and sustainable** as **code contribution**, **across** projects and platforms.

The gap is visible when **public contribution artifacts** (issues, PRs, maintainer statements) repeatedly show:

- demand for locales or doc translations,
- **while** merge paths, review capacity, or architecture readiness **lag** or **defer** that demand,

**without** implying that any single project “failed” by choosing its own risk and staffing tradeoffs.

---

## Key characteristics (working list)

- **Workflow vacuum:** Few cross-ecosystem defaults for how linguistic changes are opened, reviewed, attributed, and kept current across releases—**early evidence suggests** projects re-derive process locally.
- **Tooling fragmentation:** Extraction, glossaries, translator context, and parity checks between UI and docs are often **non-uniform** or **vendor-coupled**, not a portable commons.
- **Recognition asymmetry:** Credit and trust models for **linguistic** review commonly lag those for **code** review.
- **Bandwidth coupling:** Public maintainer language often ties deferrals to **review time**, **architecture**, and **coordination cost**—not to dismissing non-English users.

---

## Distinction that matters

The gap is **not** primarily a lack of **willing contributors**. Public threads in the linked case studies show offers to translate, review, or scaffold locales.

The gap **is** a lack of **shared systems**—time, tooling, governance, and funding models—that make linguistic work **as legible and mergeable** as code work at ecosystem scale.

---

## Scope boundary

This definition is **descriptive** for investigation. It does **not** claim that a specific technical architecture, hosting platform, or translation management product is required.

**Primary evidence** for how the gap manifests in practice belongs in [`case-studies/`](case-studies/) with URLs to upstream repositories.
