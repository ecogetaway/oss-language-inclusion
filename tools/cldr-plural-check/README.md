# cldr-plural-check (planned)

**Status: planned, not yet implemented.** This directory is a placeholder.
Do not present this tool as shipping.

Intended scope: verify that a translation's plural forms match the CLDR plural rules for its language — e.g., Arabic's six plural categories, Hindi's zero-inclusive singular — so that a locale file with missing or extra plural forms is caught in CI rather than at runtime.

It will pair with [`../i18n-security-lint`](../i18n-security-lint/) (which is implemented) as a combined "i18n quality gate."

**Before implementation:** collect a small failing corpus of real locale files
(missing or extra plural categories). That fixtures work is a follow-up to the
volunteer on-ramp ([issue #6](https://github.com/ecogetaway/oss-language-inclusion/issues/6)),
not a first task, and is **not** a request to write this checker.
