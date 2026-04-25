# Case study: OpenClaw and Hindi (hi-IN) localization

## Project

[OpenClaw](https://github.com/openclaw/openclaw) is a widely used open-source “personal AI assistant”–style project (TypeScript, cross‑platform). It is representative of a class of high-velocity community projects where documentation, UI, and error surfaces are mostly English-first.

## What was proposed

In the canonical [internationalization tracking issue #3460](https://github.com/openclaw/openclaw/issues/3460), a contributor suggested **Hindi (`hi-IN`)** as a high-priority language, citing the size of the developer community in India and reported demand. That request sat alongside many other offers to translate or review specific languages. The issue’s maintainer-facing summary listed several languages in a “requested / tracking” block; **Hindi was not among the languages initially named** in that list, despite explicit community interest.

## Outcome

The project did **not** open a maintained path to land Hindi (or other) UI/docs localization at that time. Maintainers [consolidated](https://github.com/openclaw/openclaw/issues/3460) all i18n and language requests into a single issue, stated that **new translation PRs and per-language issues would be closed** pending a proper i18n setup, and later **closed the issue** while citing **platform and documentation architecture work** and reserving future localized content for when they might explicitly ask the community. The issue was **locked**, ending public continuation of that thread in the same place.

**Stated primary constraint (repeated in the issue body):** the team did not have the **bandwidth to support multiple languages** in an ongoing, reviewable way, including coordination across UI, errors, and docs. Secondary points on the public record include the need for a **deliberate i18n architecture** and **native-speaker review** before scaling translations.

## Why this illustrates a systemic gap

- **Willing contributors are not the bottleneck.** The thread shows numerous native speakers offering concrete help; the limiting factor on the record is **maintainer capacity and a stable translation pipeline**, not lack of interest in Hindi or other languages.
- **“Close duplicate language issues”** is a rational triage move for one repo, but at ecosystem scale it shows how **linguistic access is a second-class workflow**: there is no shared, upstream convention that makes language work as easy to merge and sustain as a typical code change.
- **Global audiences are treated as a backlog item.** Where English-first shipping is the default, communities whose primary language is not English can face **long or indefinite deferral**, even for projects with clear adoption outside English-speaking regions. That is a **structural** problem (resourcing, tooling, and governance for i18n), not a one-off project failure.

*Sources: [openclaw/openclaw#3460](https://github.com/openclaw/openclaw/issues/3460) (issue body, thread, closure comment). Facts here are based on that public record as of the issue’s closed state.*
