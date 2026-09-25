# Case study: OpenClaw and Hindi (`hi-IN`)

**Source:** [openclaw/openclaw#3460](https://github.com/openclaw/openclaw/issues/3460) (issue body, discussion, closure). All factual claims below trace to that thread.

---

## Overview

[OpenClaw](https://github.com/openclaw/openclaw) is an open-source, cross-platform TypeScript project positioned as a personal AI assistant. Default surfaces (documentation, UI, errors) are largely English-first. **Hindi (`hi-IN`)** was advocated in the project’s **single canonical i18n thread**, [#3460](https://github.com/openclaw/openclaw/issues/3460), alongside many other locale offers.

---

## What was attempted

Contributors used #3460 to register translation and review interest. A contributor **proposed Hindi (`hi-IN`) as a high-priority language**, citing India’s developer community size and demand.

The issue description’s initial “languages requested (tracking)” checklist named several locales (e.g. Chinese, Portuguese, Korean, Japanese, European languages, Vietnamese, Filipino). **Hindi did not appear in that initial checklist**, even after the public comment advocating for it—an example of how **formal tracking can lag expressed demand** unless maintainers adopt it.

---

## Outcome

Maintainers **did not** open a sustained, merge-friendly path for Hindi (or other) localization during the life of that thread. On the public record, policy was to **close new translation PRs** and **close separate language requests as duplicates** of #3460 until a deliberate i18n approach existed. The issue was later **closed** (GitHub: **not planned**) and **locked**, with closure framed around **platform and documentation architecture** and maintainers **soliciting localized content when the project explicitly chooses to**.

The limiting factors described publicly were **operational** (capacity, architecture, coordination)—not a claim that Hindi lacked value.
---
## Community Demand 
---
## Key Maintainer Signals (verbatim)

> "we don't currently have the bandwidth to properly support multiple languages"

> "We need to establish a proper i18n architecture first"

> "Maintaining translations requires ongoing effort as the product evolves"

> "If we need any localized content we will ask the community to provide"
---
## Interpretation of Maintainer Constraints

**Lack of i18n bandwidth** is stated directly in the issue body (quoted from [#3460](https://github.com/openclaw/openclaw/issues/3460)):

> However, we don't currently have the bandwidth to properly support multiple languages.

Supporting reasons on the record are **engineering and process constraints**:

- Translation must track a fast-evolving product.
- An **i18n architecture** should exist before scaling languages.
- **Native-speaker review** is required for quality.
- **UI, errors, and documentation** must stay coordinated.

The **April 2026** closure comment (public record) states **architectural changes** to platform and documentation; localized content will be requested from the community **when the project needs it**.
----
## Supporting Evidence from Linked PRs

### PR #42089 — Multilingual Mobile Localization Attempt

_Status as of 25 September 2026, verified against the GitHub record; corrections are logged in [CORRECTIONS.md](../CORRECTIONS.md)._

A contributor proposed Japanese and Chinese (Simplified and Traditional) localization for the iOS and Android apps, including a localization pass over the iOS settings screen (11 files, +967/−686).

**Outcome:**
Closed without merge on 2026-04-26 by the project's automation, as superseded by the canonical i18n issue (#3460).

**Signals on the record:**

- Automated reviewers flagged problems before merge. Greptile rated it 2/5: "Not safe to merge as-is — two logic bugs and a missing locale declaration." Codex flagged the same regressions (a changed status message and a removed spinner), the missing `zh-Hant` declaration, and unrelated `.secrets.baseline` changes. One CI job failed.
- The automated closing comment cited #3460's maintainer policy:

> "translation PRs are being consolidated/closed until the i18n architecture is ready"

  It also noted "unresolved review findings and unrelated `.secrets.baseline` churn", and said future native localization "should wait for a maintainer-requested i18n path".

**Insight:**
The pull request was blocked on two counts: the project's policy of consolidating translation work until its i18n architecture is ready, and unresolved technical findings. It is not an example of a technically complete contribution refused on policy alone. What it does show is that when a project pauses translation intake, the pause is stated in a canonical issue and applied by automation. That is clear, but a contributor may learn of it only after doing the work.
----

## Key insight

**Lack of infrastructure and maintainer capacity—not lack of contributor intent—dominates the thread.** Many speakers offered concrete help; maintainers described blockers as **time, architecture, and review depth**. Hindi is one instance of a **multi-locale** pattern in the same issue.

---

## Broader implication

When each project must **invent** translation intake, triage, and sustainability—and when **i18n bandwidth** is finite—**language access varies with team load** more than with a shared ecosystem layer. Consolidation and closure were **reasonable repo-level** responses that still highlight an **upstream question**: how to make **language contribution** as **legible and sustainable** as **code contribution** without overloading individual maintainers.

---

**Canonical link:** [openclaw/openclaw#3460 — Internationalization (i18n) & Localization Support](https://github.com/openclaw/openclaw/issues/3460)
