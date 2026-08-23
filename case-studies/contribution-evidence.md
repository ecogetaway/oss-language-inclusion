# Contribution Evidence Across Projects

This note collects **publicly verifiable** examples where **Hindi-related i18n work** (or the project’s i18n capacity) intersects with **contribution mechanics**: merge, review queue, policy, or bandwidth. It is intended for **maintainers and foundations** assessing whether language inclusion behaves like a first-class infrastructure layer—or like an exception path.

Star counts and check states **change over time**; each item links to the canonical GitHub object for inspection.

---

## Summary

| Project | Reference | Status (at documentation time) | Key constraint (from public record) |
| -------- | --------- | -------------------------------- | ------------------------------------ |
| **Open WebUI** | [PR #23745](https://github.com/open-webui/open-webui/pull/23745) | Merged 2026-04-15 to `dev` | Same PR governance as code; locale hygiene still must pass project checks |
| **Kilocode** (`Kilo-Org/kilocode`) | [PR #8377](https://github.com/Kilo-Org/kilocode/pull/8377) | Closed unmerged 2026-06-05; bot check had passed | Target paths were deleted while the PR waited; rework invited |
| **Hoppscotch** | [PR #6025](https://github.com/hoppscotch/hoppscotch/pull/6025) | Open; under maintainer/bot review | Coverage vs `en.json`, review thread length, high-traffic repo (~79k stars when drafted) |
| **Hermes Agent** (`NousResearch/hermes-agent`) | [Issue #4763](https://github.com/NousResearch/hermes-agent/issues/4763) | **Still open**; declared resolved in a comment 2026-06-04 after PR #22914 merged 2026-05-10 | Proposal never routed to a PR; maintainer implemented directly 
| **OpenClaw** | [Issue #3460](https://github.com/openclaw/openclaw/issues/3460) | Closed (not planned), locked | Maintainer-stated **i18n bandwidth** + architecture readiness; consolidation policy |

---

## 1. Open WebUI — [PR #23745](https://github.com/open-webui/open-webui/pull/23745)

**Status:** Merged **2026-04-15** into `dev` (per GitHub merge metadata).

- **Insight:** A **locale-only** change (`hi-IN` string corrections in `translation.json`) can still flow through the same **governance surface** as any other PR (template, CLA, review culture)—showing that i18n *can* be treated like normal code when the pipeline accepts it.
- **Insight:** The PR’s own description frames work as **quality repair** (mis-translation, mixed-language leakage, duplicated phrasing)—i18n is not only “new locale,” it is **ongoing product hygiene**.
- **Insight:** Maintainer acknowledgment and merge occurred **within the same calendar day** as the contribution timeline on the record—useful as a **positive** comparator, not a guarantee other projects can match.

---

## 2. Kilocode — [PR #8377](https://github.com/Kilo-Org/kilocode/pull/8377)

**Repository path:** `Kilo-Org/kilocode` (this is where the PR lives on GitHub.)

**Status:** **Closed without merge** on **2026-06-05** by maintainer `@johnnyeric`. Opened 2026-04-05 (9 files, 4 commits); the **“Kilo Code Review”** bot check had passed. It was **not** closed on quality grounds: during the two months the PR sat open, the paths it targeted (`packages/app`, `packages/desktop-electron`) were **removed from the repository**. The maintainer explicitly invited a reworked PR against current `main`.

- **Insight:** The maintainer stated the gap **on the record** — that the project has no structured workflow for i18n contributions beyond normal PR review, and that language review therefore [“does depend on contributor/maintainer bandwidth right now”](https://github.com/Kilo-Org/kilocode/pull/8377#issuecomment-4631698167). This is a maintainer describing the infrastructure gap in their own words, unprompted by any framing from this repository.
- **Insight:** **Review latency has an architectural cost.** The delay did not merely postpone the contribution — it **invalidated** it. Code moved beneath the PR, and a locale change that was correct in April targeted deleted directories by June. For language contributions specifically, waiting is not neutral: the target drifts.
- **Insight:** Hindi here spanned **multiple packages** in one PR — cross-cutting i18n touches more files and more reviewers’ mental models than a single-locale JSON tweak, which widens the surface exposed to that drift.
- **Insight:** This is **not a rejection**, and “merged vs rejected” has no category for it. The invitation to rework still stands. The accurate state is **expired** — a state invisible to any metric that counts only merges and closures-as-refusals.

**Verification:** Originally recorded 2026-04 as “open; not merged.” Re-checked **2026-08-24** against the GitHub API: `state: closed`, `merged: false`, `closed_at: 2026-06-05`. Section corrected accordingly.

---

## 3. Hoppscotch — [PR #6025](https://github.com/hoppscotch/hoppscotch/pull/6025)

**Status:** **Open**; under **maintainer and automated review** (e.g. third-party review bots on the thread). The repository is **high-visibility** (on the order of **~79k GitHub stars** on the repository page at the time this document was drafted—**70k+** remains directionally correct).

- **Insight:** Large projects attract **bot-assisted review** and **long threads**; for contributors, “open” can mean **substantial unpaid follow-up** (coverage gaps, key parity with `en.json`, style nits) even when intent and effort are serious.
- **Insight:** **Partial locale coverage** is technically tolerable (fallback to English) but **product- and community-visible**; reviewers will rightly treat missing keys as debt.
- **Insight:** Peer review from **other Hindi speakers** in-thread shows community capacity exists; the bottleneck is **coordination and merge**, not proof of interest.

---

## 4. NousResearch / Hermes Agent — [Issue #4763](https://github.com/NousResearch/hermes-agent/issues/4763)

**Status:** **Still open** as of 2026-08-24. The underlying request was satisfied upstream by maintainer [PR #22914](https://github.com/NousResearch/hermes-agent/pull/22914), **merged 2026-05-10**, which added 8 documentation locales including Hindi. A maintainer then commented on **2026-06-04** that the issue was being closed as resolved — but **did not actually close it**, and it remains open. The proposal was never routed through a contributor PR; the maintainer implemented it directly.

- **Insight:** **Docs i18n** is often a **separate decision surface** from app UI strings—maintainers must answer workflow questions (direct PR vs platform, ownership, staleness) **before** the first merge.
- **Insight:** The issue explicitly asked for **maintainer preference on process**. That question was never answered; the maintainer implemented the locales directly instead—so **infrastructure and policy** were settled unilaterally rather than negotiated with the contributor.
- **Insight:** Treating this as an **issue-first** proposal (not only a drive-by PR) reflects respect for maintainer load, but it also means **latency**—and here the latency ended not through alignment with the contributor, but through the maintainer doing the work themselves roughly two months later. Issue-first defers to maintainer capacity; it does not secure a contribution path.

- **Insight:** **Declared closure and actual closure diverged.** A maintainer announced the issue was resolved and closed; the tracker still shows it open nearly three months later. Anyone auditing this project's i18n backlog by issue state would double-count it — a small illustration of why locale-request state is hard to measure across projects, and why contributors cannot reliably tell whether their request is live.

**Verification:** Originally recorded as an open proposal; a 2026-08-17 pass wrongly recorded it as “closed 2026-06-04.” Re-checked against the GitHub API on **2026-08-24**: the issue is `state: open` with `closed_at: null`; PR #22914 merged **2026-05-10**, not 06-04 (that was the date of the maintainer's comment). Both errors corrected.
---

## 5. OpenClaw — [Issue #3460](https://github.com/openclaw/openclaw/issues/3460)

**Status:** **Closed** (GitHub: **not planned**); conversation **locked**. Canonical consolidation point for i18n and per-language requests.

- **Insight:** Maintainers stated **lack of bandwidth** to support multiple languages responsibly and the need for an **i18n architecture** before scaling—**capacity**, not hostility to locales, is on the public record (see also [`openclaw.md`](./openclaw.md) in this folder).
- **Insight:** **Central triage** (“close duplicate language issues / translation PRs until ready”) is rational for one repo and still produces a **cold start** for every would-be locale contributor.
- **Insight:** Closure under **architecture and platform change** illustrates that **language work competes with core engineering narratives** for attention and sequencing.

---

## Cross-Project Pattern

Across these references—**merged**, **open-and-reviewed**, **closed-because-the-target-moved**, **resolved-upstream-without-the-contributor**, and **closed-for-capacity**—a stable pattern appears:

1. **Community intent exists** (fixes, new locale files, doc locale proposals, thread offers).
2. **Project outcomes diverge** based on **reviewer time**, **automation**, **repository policy**,****closed-resolved-upstream** **, and **architectural readiness**—not based on whether Hindi is a “reasonable” language to support.
3. **There is no single shared upstream** that equalizes these outcomes; each project **re-derives** intake, quality bars, and sustainability.

**Categories spanned:** the table above includes **AI-adjacent application UIs** (Open WebUI, OpenClaw), **multi-package developer tooling** (Kilocode), **API / client developer tools** (Hoppscotch), and **documentation sites** (Hermes Agent). **Early evidence suggests** the friction pattern is **not confined to one stack or vertical**—it may be **ecosystem-wide**, even though each project’s risk model and staffing differ.

Stated neutrally: **language contribution is coupled to project-local governance and staffing**, not to a portable, ecosystem-wide layer comparable to mature code-contribution norms.

---

## Conclusion

These cases are not interchangeable—different communities, risk models, and release cadences explain different outcomes. Taken together, they **support a hypothesis worth institutional investigation**: **variance in language inclusion is structured by tooling, policy, and maintainer bandwidth**, not fully explained as isolated incidents or lack of contributor motivation.

This is framed as a **potential infrastructure gap**. It is **not** a statistically proven universal law; confirm or falsify with broader sampling, surveys, and program data before policy or funding decisions.

Where merge happens, it tends to look like **ordinary engineering hygiene**. Where it stalls or is deferred, the public reasons are overwhelmingly **process and capacity**. That gap—between **desire to contribute in language** and **predictable, low-friction pathways**—is the **question** this repository is meant to keep visible.

---

**Disclaimer:** GitHub states (open/merged/locked), checks, and star counts were sampled from the linked URLs and API at documentation time; refresh the links for the current truth.
