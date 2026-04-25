This repository explores whether language inclusion is a missing infrastructure layer in open source.

# Open Source Language Inclusion

**Open source has infrastructure for code, but not for language.**

Most projects invest heavily in contribution workflows, CI, and governance for *software* changes. Comparable norms—reviewable, mergeable, attributable—are inconsistent for *translatable* surfaces (UI, errors, documentation). This repo **documents that asymmetry**, gathers **primary-linked examples**, and invites **maintainer notes**. Audience: maintainers, foundations, and standards bodies. **Exploratory only:** not a product pitch or a committed platform.

---

## Why this matters

- **Access:** Single-language defaults exclude people regardless of technical skill.
- **Equity:** Non-English audiences are majorities in many contexts; language is a hard participation boundary.
- **Quality:** Weak localization affects comprehension, safety-sensitive prompts, and trust.
- **Resilience:** Broader language coverage improves feedback, documentation, and adoption.

---

## Evidence in progress

Worked case notes (each cites upstream issues/PRs):

- [`case-studies/openclaw.md`](case-studies/openclaw.md)
- [`case-studies/contribution-evidence.md`](case-studies/contribution-evidence.md)

---

## The gap

- **Code vs. language:** Pull requests, bots, and review culture are mature for code; translatable content rarely receives the same end-to-end treatment.
- **Fragmented tooling:** Extraction, glossaries, translator context, and merge discipline are often ad hoc or vendor-specific—not a shared commons.
- **Recognition:** Trust and credit for linguistic review still lag those for code.
- **Governance:** Technical programs and specs often center English process; multilingual feedback loops are easy to under-resource.
- **Sustainability:** Locales drift when translation is decoupled from release cadence, funding, and maintainer time.

---

## Where shared infrastructure might help

Working hypotheses—not a roadmap: interoperable formats, clear paths for *linguistic* review (not only string dumps), and coordination across projects to reduce duplicated effort and terminology drift. The point is to **compare notes** and make constraints legible, not to prescribe one stack.

---

## How to engage

- **Maintainer feedback:** [`maintainer-feedback/README.md`](maintainer-feedback/README.md) — neutral prompts; contribute via [issues](https://github.com/ecogetaway/oss-language-inclusion/issues) with public links where you can.
- **Corrections and disagreement** are welcome; cite sources so claims stay checkable.

---

## Repository structure

```
oss-language-inclusion/
├── README.md
├── roadmap.md
├── case-studies/
├── maintainer-feedback/
│   └── README.md
└── contributors/
```

---

## Status

**Early-stage exploration.** No fixed deliverable list; direction follows maintainer and foundation feedback and work already happening elsewhere.

---

*https://github.com/ecogetaway/oss-language-inclusion*
