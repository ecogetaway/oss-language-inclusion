# Security Policy

## Reporting a vulnerability

If you find a security issue in this repository — in the `i18n-security-lint` tool, the GitHub Action, or anything else here — please report it privately first:

1. **Preferred:** use GitHub's private vulnerability reporting on this repository ("Security" tab → "Report a vulnerability").
2. **Fallback:** email **ecogetaway@gmail.com** with the subject line `SECURITY: oss-language-inclusion`.

Please include reproduction steps and, if the issue is in the linter, a minimal locale file that triggers it. We aim to acknowledge reports within **7 days**. This is a small, part-time-maintained project — we will be honest about timelines rather than promise turnarounds we can't keep.

Please do not open a public issue for an unpatched vulnerability.

## Scope

In scope:

- `tools/i18n-security-lint/` — the scanner, its CLI, and the Docker-based GitHub Action. Of particular interest: **bypasses** (a locale file containing one of the four documented defect classes that the scanner fails to flag) and **input-handling bugs** (a crafted locale file that crashes the scanner or causes it to misbehave, since the scanner's whole job is to consume untrusted files).
- The workflows in `.github/workflows/`.

Out of scope:

- Vulnerabilities in third-party projects discussed in `case-studies/` — report those to the affected project, not to us.
- The four vulnerability classes in `spec/translated-string-security-checks.md` as *general phenomena* — that's our research subject, not a bug in this repo. Improvements to the spec are welcome as regular issues/PRs.

## Detection limitations, stated plainly

`i18n-security-lint` is a pattern-based scanner at v0.1. It will miss things (it is not a parser-accurate XSS detector, and placeholder comparison is heuristic). A clean scan reduces risk; it is not a security guarantee. Known-limitation reports that don't cross the "bypass" bar are welcome as public issues.

## Security posture of this repository

- No published packages: the tool is installed from source (`pip install -e .`); there is no PyPI artifact yet, so there is no package-registry supply-chain surface.
- The GitHub Action runs from a Dockerfile in this repository; pin a commit SHA rather than `@main` if you consume it in CI.
- CI (`.github/workflows/ci.yml`) runs the linter's test suite and dogfoods the scanner against a corpus of malicious locale files on every push and pull request.
