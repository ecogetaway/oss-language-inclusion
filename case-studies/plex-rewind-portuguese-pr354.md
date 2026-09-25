# Case Study: RaunoT/plex-rewind — Portuguese — PR #354

_Status as of 25 September 2026, verified against the GitHub record. Pull request and issue states change; the linked source is authoritative. Corrections to this case are logged in [CORRECTIONS.md](../CORRECTIONS.md)._

## Repository
[RaunoT/plex-rewind](https://github.com/RaunoT/plex-rewind)

## Contribution Type
Pull Request

## Language
Portuguese (pt)

## What Happened
A contributor added a Portuguese locale file (1 file, +276). The next day the maintainer requested changes: linting was failing, and the language code also needed to be added to `src/utils/constants.ts` "for it to be picked up by the locale switcher". No further commits followed the request. The stale bot marked the pull request inactive and then closed it.

## Timeline
- Opened: 2026-02-26
- Changes requested by the maintainer: 2026-02-27
- Marked stale: 2026-03-30
- Closed: 2026-04-05 (38 days)

## Closing Reason
Closed by the stale bot after no activity on the requested changes.

## Maintainer Response
Yes: a specific change request the day after it opened (fix the lint failure; register the locale code).

## Why This Matters
The maintainer's request names a step that also appears in the Kilo Code case: a translation file alone does not reach users until the locale is registered where the application discovers it. It is a step a project could document for contributors before they begin, so that it is not first learned in review.

## Source
[github.com/RaunoT/plex-rewind/pull/354](https://github.com/RaunoT/plex-rewind/pull/354)
