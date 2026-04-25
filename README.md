# Open Source Language Inclusion

**Open source has infrastructure for code, but not for language.**

This repository explores whether language inclusion is a missing infrastructure layer in open source. Concretely, it documents a systemic gap: projects invest heavily in contribution workflows, CI, and governance for *software* changes, while *localization and translation* often lack comparable tooling, recognition, and pathways for contributors. The result is slower progress toward equitable global access to software and documentation.

This repository is aimed at open-source maintainers, foundations, and standards bodies who set norms and build shared infrastructure. It is not a product pitch; it is a place to name the problem, gather evidence, and shape what *good* could look like at ecosystem scale.

---

## Evidence from real projects

The following are illustrative cases where language-related contribution did not (or could not) match the maturity of code contribution. **Replace the placeholders** with your own links, project names, and short notes as you build this out.

| Project or ecosystem | What happened or what was observed | Source / link |
| -------------------- | --------------------------------- | ------------- |
| *(e.g. large application stack)* | *(e.g. no shared workflow for string updates vs. translation)* | *TBD* |
| *(e.g. documentation-heavy project)* | *(e.g. community translations informal or unmerged)* | *TBD* |
| *(e.g. standards or spec body)* | *(e.g. non-English feedback not captured in the same system as issues)* | *TBD* |

*Additional evidence (blog posts, maintainer threads, research):*

- *TBD — link 1*
- *TBD — link 2*

---

## The gap

- **Asymmetry with code:** Pull requests, reviews, and bots are first-class for code; the same is rarely true end-to-end for translatable content (strings, docs, error messages, UI copy).
- **No shared “language layer” in tooling:** Extraction, glossary, context for translators, and merge discipline are often ad hoc or vendor-specific, not part of a commons.
- **Contributor recognition:** Credit and trust models for i18n work (review, consistency, domain expertise) are weak compared to code, which discourages sustained participation.
- **Foundations and standards:** Technical work is procedurally clear; multilingual participation in feedback and consensus is still an afterthought in many processes.
- **Sustainability:** Translation work burns out when it is decoupled from release cadence, funding, and maintainer time.

---

## Vision: global i18n contributor infrastructure

The long-term goal is **shared infrastructure and norms** so that “language work” is as legible, reviewable, and mergeable as code:

- First-class representation of translatable resources in repository and contribution flows.
- Clear paths for *linguistic* review (not only string dumps) and alignment with product intent.
- Tooling and data formats that are **open, interoperable, and not locked to a single vendor**.
- Recognition and governance that treat localization contributors as first-class participants.
- Coordination across projects where duplication of effort and terminology drift are currently the default.

This repository is a starting point to describe that vision in concrete terms and to connect with others working on the same class of problem.

---

## Call for maintainers and practitioners

If you maintain a project, run a program in a foundation, or shape contribution policy: **this needs your experience.**

- Open an [issue](https://github.com/ecogetaway/oss-language-inclusion/issues) to share constraints (what failed, what almost worked, what you would need from the ecosystem).
- Point to public discussions or documentation that should be in the evidence section.
- Suggest structure for this repository if you believe a different framing would help standards bodies and platform teams.

Constructive disagreement is welcome. The aim is a clearer shared picture, not a single commercial stack.

---

## Repository structure

```
oss-language-inclusion/
├── README.md                 # This document — problem, vision, and calls to action
└── (future)                  # e.g. evidence appendices, templates, or notes — as the project grows
```

*Expand this section as you add files (e.g. `docs/`, `case-studies/`, or contribution guidelines for *this* repo).*

---

## Why this matters

- **Access:** Software that is only fully usable in one language excludes people by default, regardless of their technical skills.
- **Equity:** Non-English users are not a niche audience; they are the majority in many global contexts. Treating language as infrastructure is a prerequisite for fair participation.
- **Quality:** Poor or missing localization undermines security (misunderstood prompts), support load, and trust in the project.
- **Resilience:** Diverse language communities strengthen projects through broader feedback, documentation, and adoption.

---

## Status

**Early-stage exploration.** The GitHub organization is a home for the idea and for collaborative editing of this document and future artifacts. There is no committed roadmap or deliverable list yet. Direction will follow from maintainer and foundation feedback, shared problem framing, and where aligned work already exists in the wild.

---

*Repository: [github.com/ecogetaway/oss-language-inclusion](https://github.com/ecogetaway/oss-language-inclusion)*
