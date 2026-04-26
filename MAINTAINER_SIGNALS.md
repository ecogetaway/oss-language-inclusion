# Maintainer Signals

This page documents early signals from open-source maintainers on the challenges of supporting language inclusion contributions (i18n, l10n, translation PRs) in their repositories.

These are not endorsements. They are evidence — gathered from real maintainer interactions across real repositories — that the structural gap documented in this initiative is recognised by those closest to the problem.

---

## Signals from the Ecosystem

### Signal 1 — hermes-webui (Nathan Esquenazi, maintainer)

On reviewing a Chinese (zh-CN) localization PR (#177), the maintainer wrote:

> *"The translations themselves are the hardest part and you've already done that. The infrastructure to make it work safely is the remaining piece."*

**What this reveals:** A willing maintainer, a willing contributor, and no shared infrastructure to connect them safely. The contributor did the hard work. The system was not ready to receive it.

**Source:** [github.com/nesquena/hermes-webui/pull/177](https://github.com/nesquena/hermes-webui/pull/177)

---

### Signal 2 — OpenClaw (vincentkoc, maintainer) — Hindi

Issue #3460: Hindi (hi) internationalization support request.

**Maintainer response:** Closed as *"not planned"* — citing lack of i18n bandwidth.

**What this reveals:** The maintainer did not reject the language. They rejected the burden of supporting it without infrastructure. Language inclusion is willing in principle, unsupported in practice.

**Source:** [github.com/openclaw/openclaw/issues/3460](https://github.com/openclaw/openclaw/issues/3460)

---

### Signal 3 — OpenClaw (vincentkoc, maintainer) — Chinese (Simplified)

Issue #34848: Feature request to add Chinese (Simplified) localization support.

**Maintainer response:** Closed citing architectural changes, with the comment:

> *"We are closing this as we are making architectural changes to the platform and documentation. If we need any localized content we will ask the community to provide."*

**What this reveals:** Language inclusion is treated as reactive and on-demand — "we will ask the community to provide" — rather than a structured contribution pathway. This is the default model across most open-source projects.

**Source:** [github.com/openclaw/openclaw/issues/34848](https://github.com/openclaw/openclaw/issues/34848)

---

### Signal 4 — Open WebUI — Hindi

PR #23745: Corrected erroneous Hindi (hi-IN) translations.

**Outcome:** Merged April 15, 2026 by maintainer Tim Baek.

**What this reveals:** When a structured, high-quality i18n contribution arrives in a form maintainers can handle, it gets merged. The barrier is not willingness — it is the absence of a pathway that makes contributions handleable at scale.

**Source:** [github.com/open-webui/open-webui/pull/23745](https://github.com/open-webui/open-webui/pull/23745)

---

## Pattern Summary

Across these signals, a consistent pattern emerges:

| Signal | Language | Outcome | Root cause |
|---|---|---|---|
| hermes-webui PR #177 | Chinese (zh-CN) | Delayed — infrastructure missing | No i18n scaffold |
| OpenClaw Issue #3460 | Hindi | Closed — no bandwidth | No structured workflow |
| OpenClaw Issue #34848 | Chinese (Simplified) | Closed — architectural | Reactive model |
| Open WebUI PR #23745 | Hindi | Merged | High-quality, structured contribution |

**The conclusion is not that maintainers are unwilling. It is that the open-source ecosystem has not built the infrastructure that would make their willingness actionable.**

---

## Contribute a Signal

If you are a maintainer or contributor who has experienced this pattern — in any language — we would value your perspective.

Open an issue or submit a PR adding your signal to this file. Even a brief description and a link to the relevant issue or PR helps establish the breadth of the pattern.

**What to include:**
- Repository name and link
- Language(s) affected
- What happened (closed, delayed, merged with difficulty)
- The maintainer's or contributor's perspective in their own words (with permission)

---

*This is evidence, not advocacy. The goal is to document the gap accurately so that the right institutions can address it.*

*Last updated: April 2026*
