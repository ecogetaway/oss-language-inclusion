# Contribution Evidence Across Projects

This note collects **publicly verifiable** examples where **Hindi-related i18n work** (or the project’s i18n capacity) intersects with **contribution mechanics**: merge, review queue, policy, or bandwidth. It is intended for **maintainers and foundations** assessing whether language inclusion behaves like a first-class infrastructure layer—or like an exception path.

Star counts and check states **change over time**; each item links to the canonical GitHub object for inspection.

---

## Summary

| Project | Reference | Status (at documentation time) | Key constraint (from public record) |
| -------- | --------- | -------------------------------- | ------------------------------------ |
| **Open WebUI** | [PR #23745](https://github.com/open-webui/open-webui/pull/23745) | Merged 2026-04-15 to `dev` | Same PR governance as code; locale hygiene still must pass project checks |
| **Kilocode** (`Kilo-Org/kilocode`) | [PR #8377](https://github.com/Kilo-Org/kilocode/pull/8377) | Open; automated “Kilo Code Review” check **success**; not merged | Human maintainer merge; cross-package scope |
| **Hoppscotch** | [PR #6025](https://github.com/hoppscotch/hoppscotch/pull/6025) | Open; under maintainer/bot review | Coverage vs `en.json`, review thread length, high-traffic repo (~79k stars when drafted) |
| **Hermes Agent** (`NousResearch/hermes-agent`) | [Issue #4763](https://github.com/NousResearch/hermes-agent/issues/4763) | Open proposal | Maintainer workflow preference (PR vs platform) unset before work lands |
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

**Status:** **Open** at last check; **not merged**. GitHub Actions include a **“Kilo Code Review”** check reported as **success**; other listed checks were **skipped** on the sampled commit. **Human maintainer merge** is therefore still the gating step.

- **Insight:** **Automation can clear a bar** (style/bot review) while **merge authority** remains concentrated on maintainers—fine for risk control, but it lengthens the **wall-clock** for language access unless i18n has dedicated reviewer capacity.
- **Insight:** Hindi here spans **multiple packages** in one PR—cross-cutting i18n touches **more files and more reviewers’ mental models** than a single-locale JSON tweak in one app.
- **Insight:** This sits in the middle of the spectrum: **neither rejected nor shipped**—a common state that is easy to under-count when success is measured only by merged PRs.

---

## 3. Hoppscotch — [PR #6025](https://github.com/hoppscotch/hoppscotch/pull/6025)

**Status:** **Open**; under **maintainer and automated review** (e.g. third-party review bots on the thread). The repository is **high-visibility** (on the order of **~79k GitHub stars** on the repository page at the time this document was drafted—**70k+** remains directionally correct).

- **Insight:** Large projects attract **bot-assisted review** and **long threads**; for contributors, “open” can mean **substantial unpaid follow-up** (coverage gaps, key parity with `en.json`, style nits) even when intent and effort are serious.
- **Insight:** **Partial locale coverage** is technically tolerable (fallback to English) but **product- and community-visible**; reviewers will rightly treat missing keys as debt.
- **Insight:** Peer review from **other Hindi speakers** in-thread shows community capacity exists; the bottleneck is **coordination and merge**, not proof of interest.

---

## 4. NousResearch / Hermes Agent — [Issue #4763](https://github.com/NousResearch/hermes-agent/issues/4763)

**Status:** **Open** (proposal to add Hindi documentation locale via Docusaurus scaffolding and incremental page translation).

- **Insight:** **Docs i18n** is often a **separate decision surface** from app UI strings—maintainers must answer workflow questions (direct PR vs platform, ownership, staleness) **before** the first merge.
- **Insight:** The issue explicitly asks for **maintainer preference on process**—a sign that **infrastructure and policy** precede the first translated paragraph.
- **Insight:** Treating this as an **issue-first** proposal (not only a drive-by PR) reflects respect for maintainer load; it also means **latency** until priorities align.

---

## 5. OpenClaw — [Issue #3460](https://github.com/openclaw/openclaw/issues/3460)

**Status:** **Closed** (GitHub: **not planned**); conversation **locked**. Canonical consolidation point for i18n and per-language requests.

- **Insight:** Maintainers stated **lack of bandwidth** to support multiple languages responsibly and the need for an **i18n architecture** before scaling—**capacity**, not hostility to locales, is on the public record (see also [`openclaw.md`](./openclaw.md) in this folder).
- **Insight:** **Central triage** (“close duplicate language issues / translation PRs until ready”) is rational for one repo and still produces a **cold start** for every would-be locale contributor.
- **Insight:** Closure under **architecture and platform change** illustrates that **language work competes with core engineering narratives** for attention and sequencing.

---

## Cross-Project Pattern

Across these references—**merged**, **open-and-reviewed**, **open-awaiting-merge**, **open-policy-discussion**, and **closed-for-capacity**—a stable pattern appears:

1. **Community intent exists** (fixes, new locale files, doc locale proposals, thread offers).
2. **Project outcomes diverge** based on **reviewer time**, **automation**, **repository policy**, and **architectural readiness**—not based on whether Hindi is a “reasonable” language to support.
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
