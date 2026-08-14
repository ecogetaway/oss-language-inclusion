# `i18n-signals.yml` — draft specification (v0.1, provisional)

A project may place a file named `i18n-signals.yml` at its repository root so a
contributor can see — before opening a locale PR — whether language work is
likely to be reviewed.

This is **not** a translation platform, a quality score, or a badge. Empty or
modest answers are more useful than optimistic ones. The file is optional.

**Status:** v0.1 draft. Fields may change. There is **no** validator, GitHub
Action, or posture badge yet.

**Volunteer note:** this spec is **not** the on-ramp. First contributions still
start at [issue #6](https://github.com/ecogetaway/oss-language-inclusion/issues/6)
(case study, lint corpus, or signal notes).

Related: research patterns live in [`signals/`](../signals/) (markdown). That
folder is *this* project's observations. `i18n-signals.yml` is a file *other*
projects may adopt. The two share a word; they are not the same artifact.

Security checks for translated strings are a separate spec:
[`translated-string-security-checks.md`](translated-string-security-checks.md).

---

## Why this file (from this repository's evidence)

Public case studies in this repo repeatedly show **demand for locales** while
**review ownership, architecture readiness, and format expectations** stay
unstated:

- Maintainers defer new locales until architecture and bandwidth exist
  ([OpenClaw](../case-studies/openclaw.md),
  [contribution-evidence.md](../case-studies/contribution-evidence.md)).
- Review depth often depends on **who can actually read the language**, not on
  bot checks ([maintainer-signals.md](../signals/maintainer-signals.md)).
- Docs translation is a different decision surface from UI strings
  ([Hermes Agent in contribution-evidence.md](../case-studies/contribution-evidence.md)).
- Projects re-derive intake locally (JSON vs gettext vs a hosted platform).

The draft fields below are meant to make those facts legible in one place.

---

## Proposed v0.1 field set

Every field except `schema_version` and `project` is optional. Prefer an honest
omission to a guess.

| Field | Intent | Suggested values (draft) |
| --- | --- | --- |
| `schema_version` | Pin the draft | `"0.1"` |
| `project` | Name and repo URL | object |
| `review_readiness` | Will someone look at language PRs? | `not_ready` · `accepting_fixes_only` · `accepting_new_locales` |
| `language_expertise` | Languages a reviewer can actually check | list of `{ locale, github_handle? }` — empty list is valid |
| `preferred_format` | How this repo expects translations to land | e.g. `po`, `json`, `xliff`, `fluent`, `weblate`, `docs` |
| `standards_compliance` | Plural / message format bar, if any | e.g. `cldr` · `gettext` · `icu` · `none-declared` |
| `scope` | What kind of language work is in play | list: `ui`, `docs` |
| `last_reviewed` | When a maintainer last stood behind this file | ISO date |

`review_readiness: not_ready` is a first-class, respectable state. It matches
public triage this corpus already documents (waiting states, duplicate closure,
architecture-first).

`scope` is included because UI-string PRs and documentation-locale PRs are not
the same review problem. A project can accept one and decline the other.

---

## Open questions (do not treat as frozen)

1. Is `not_ready` / `accepting_fixes_only` / `accepting_new_locales` the right
   three-way split, or is a free-text `notes` field enough?
2. Should `scope` be required in v0.1, or stay optional?
3. Should the file mention CI tools (`i18n-security-lint`, a future plural
   check)? **Proposal: no** — declaration must not depend on those tools
   existing.
4. Named `github_handle` on `language_expertise`: useful, or too stale too
   fast? An honest empty list may be better than a handle that left the project.

Comment on [issue #8](https://github.com/ecogetaway/oss-language-inclusion/issues/8)
rather than silently rewriting this file.

---

## What this draft is not

- Not a claim that CLDR plural errors are the dominant failure in this corpus
  (they are a *finishable* check; evidence for “most violated” is not in the
  current case studies).
- Not a quality or inclusion score.
- Not ready to extract into its own repository.

---

## Examples

Illustrative files (including this repository's own honest self-file) live in
[`examples/`](examples/).
