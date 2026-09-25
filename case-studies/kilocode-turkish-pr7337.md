# Case Study: Kilo-Org/kilocode — Turkish — PR #7337

_Status as of 25 September 2026, verified against the GitHub record. Pull request and issue states change; the linked source is authoritative. Corrections to this case are logged in [CORRECTIONS.md](../CORRECTIONS.md)._

## Repository
[Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode)

## Contribution Type
Pull Request

## Language
Turkish (tr)

## What Happened
A contributor completed the Turkish translation file, restoring earlier work from #7035 and adding 47 keys introduced in a later release (1 file, +1,165). The project's review bot reported one critical issue: Turkish was "not registered as a supported locale … so this new `tr.ts` file is still never selected and Turkish users still fall back to English." (The bot's check itself showed as passed; the finding was in its report.) Another contributor commented "Looks great" the next day. Five weeks later, a repository collaborator asked which of three open Turkish pull requests should be merged, and whether any had been tested. The pull request's Screenshots and "How to Test" sections had been left empty. With no reply to that question, the pull request was closed manually as stale, with an invitation to reopen with a fresh pull request.

## Timeline
- Opened: 2026-03-19
- Review bot report (one critical issue): 2026-03-19
- Collaborator's question about competing pull requests: 2026-04-24
- Closed (manually, not by a bot): 2026-04-30 (42 days)

## Closing Reason
Closed as stale after the question about which of three Turkish pull requests to merge went unanswered.

## Maintainer Response
Yes: a collaborator asked which pull request to merge and whether it had been tested; the closing comment invited a fresh pull request.

## Why This Matters
Three things stood between this translation and its users, and none of them was translation quality: registering the locale so the app would load it, evidence that it worked (screenshots or test steps), and a decision about which of three competing pull requests was authoritative. Each is a review-routing or verification step that a language-contribution workflow could make explicit before a contributor starts.

## Related Cases
Kilo-Org/kilocode#8377 (Hindi, opened by the author of this repository): opened 2026-04-05 and closed 2026-06-05 because the paths it targeted had been removed from the repository. The reviewer invited a reworked pull request against the current i18n files and noted that the project has no structured workflow for i18n contributions beyond normal pull-request review. See [contribution-evidence.md](contribution-evidence.md).

## Source
[github.com/Kilo-Org/kilocode/pull/7337](https://github.com/Kilo-Org/kilocode/pull/7337)
