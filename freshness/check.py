"""Weekly freshness check for the sources behind the case studies.

Reads freshness/watchlist.yml and reports, per source:
  * activity on watched GitHub pull requests and issues after the `verified` date,
  * commits to watched GitHub / GitLab files after the `verified` date,
  * MediaWiki edits after the `verified` date,
  * anchor phrases that are no longer present on the page,
  * sources that could not be reached.

With --dry-run it prints the report. Otherwise, if anything needs review (or it is
the first run of the month and there are manual sources), it opens an issue
labelled `source-changed`, or comments on the one already open.
"""

import argparse
import datetime as dt
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request

import yaml

UA = "oss-language-inclusion freshness check (+https://github.com/ecogetaway/oss-language-inclusion)"
REPO = os.environ.get("GITHUB_REPOSITORY", "ecogetaway/oss-language-inclusion")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
LABEL = "source-changed"
TITLE = "Case-study sources changed: review needed"


def fetch(url, headers=None, data=None, method=None):
    h = {"User-Agent": UA}
    h.update(headers or {})
    req = urllib.request.Request(url, headers=h, data=data, method=method)
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "replace")


def gh(path, method=None, body=None):
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    data = json.dumps(body).encode() if body is not None else None
    if data:
        headers["Content-Type"] = "application/json"
    return json.loads(fetch(f"https://api.github.com{path}", headers, data, method) or "null")


def since_iso(verified):
    # `verified` means reviewed through the end of that day (UTC).
    d = dt.date.fromisoformat(str(verified)) + dt.timedelta(days=1)
    return f"{d.isoformat()}T00:00:00Z"


def page_text(url):
    raw = fetch(url)
    raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", raw)))


def check_source(src):
    findings, errors = [], []
    since = since_iso(src["verified"])
    for t in src.get("threads", []):
        try:
            item = gh(f"/repos/{t['repo']}/issues/{t['number']}")
        except Exception as e:  # noqa: BLE001
            errors.append(f"{t['repo']}#{t['number']}: {e}")
            continue
        if item["updated_at"] >= since:
            kind = "pull request" if "pull_request" in item else "issue"
            q = urllib.parse.urlencode({"since": since, "per_page": 20})
            new_comments = gh(f"/repos/{t['repo']}/issues/{t['number']}/comments?{q}")
            findings.append(f"activity on {kind} [{t['repo']}#{t['number']}]({item['html_url']}): now `{item['state']}`, updated {item['updated_at'][:10]}; new comments: {len(new_comments)}")
    for f in src.get("github", []):
        q = urllib.parse.urlencode({"path": f["path"], "since": since, "per_page": 20})
        try:
            commits = gh(f"/repos/{f['repo']}/commits?{q}")
        except Exception as e:  # noqa: BLE001
            errors.append(f"{f['repo']}/{f['path']}: {e}")
            continue
        for c in commits:
            msg = c["commit"]["message"].split("\n")[0][:100]
            findings.append(f"commit {c['commit']['committer']['date'][:10]} to `{f['repo']}/{f['path']}`: [{msg}]({c['html_url']})")
    for f in src.get("gitlab", []):
        proj = urllib.parse.quote(f["project"], safe="")
        q = urllib.parse.urlencode({"path": f["path"], "since": since})
        try:
            commits = json.loads(fetch(f"https://{f['host']}/api/v4/projects/{proj}/repository/commits?{q}"))
        except Exception as e:  # noqa: BLE001
            errors.append(f"{f['host']}/{f['project']}/{f['path']}: {e}")
            continue
        for c in commits:
            findings.append(f"commit {c['created_at'][:10]} to `{f['project']}/{f['path']}`: [{c['title'][:100]}]({c.get('web_url', '')})")
    mw = src.get("mediawiki")
    if mw:
        q = urllib.parse.urlencode({"action": "query", "prop": "revisions", "titles": mw["title"], "rvlimit": 5,
                                    "rvprop": "timestamp|comment", "rvend": since, "format": "json"})
        try:
            pages = json.loads(fetch(f"{mw['api']}?{q}"))["query"]["pages"]
            for p in pages.values():
                for r in p.get("revisions", []):
                    if r["timestamp"] >= since:
                        findings.append(f"wiki edit {r['timestamp'][:10]} to `{mw['title']}`: {r.get('comment', '')[:100]}")
        except Exception as e:  # noqa: BLE001
            errors.append(f"{mw['title']}: {e}")
    cache = {}
    for a in src.get("anchors", []):
        try:
            if a["url"] not in cache:
                cache[a["url"]] = page_text(a["url"])
            if a["text"] not in cache[a["url"]]:
                findings.append(f"anchor phrase missing from {a['url']}: “{a['text']}”")
        except Exception as e:  # noqa: BLE001
            errors.append(f"{a['url']}: {e}")
    return findings, errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "watchlist.yml"), encoding="utf-8") as fh:
        sources = yaml.safe_load(fh)["sources"]

    changed, unreachable, manual = [], [], []
    for src in sources:
        if src.get("manual"):
            manual.append(f"- **{src['id']}**: {src['manual']}")
        findings, errors = check_source(src)
        if findings:
            changed.append(f"### {src['id']} (verified {src['verified']})\n" + "\n".join(f"- {x}" for x in findings))
        if errors:
            unreachable.append(f"- **{src['id']}**: " + "; ".join(errors))

    today = dt.date.today()
    monthly = today.day <= 7
    parts = [f"Freshness check run on {today.isoformat()} ({len(sources)} sources)."]
    if changed:
        parts.append("## Changed since last verification\n\nReview each change against the case study (and the language page on the initiative site), log any correction in CORRECTIONS.md, then update `verified` in `freshness/watchlist.yml`.\n\n" + "\n\n".join(changed))
    if unreachable:
        parts.append("## Could not check\n\n" + "\n".join(unreachable))
    if manual and (monthly or changed or unreachable):
        parts.append("## Check by hand\n\n" + "\n".join(manual))
    report = "\n\n".join(parts)
    print(report)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(report + "\n")

    needs_issue = bool(changed or unreachable or (monthly and manual))
    if args.dry_run or not needs_issue:
        return 0
    try:
        gh(f"/repos/{REPO}/labels", "POST", {"name": LABEL, "color": "d4c5f9", "description": "A case-study source changed; review needed"})
    except Exception:  # noqa: BLE001 - label already exists
        pass
    open_issues = gh(f"/repos/{REPO}/issues?labels={LABEL}&state=open&per_page=5")
    if open_issues:
        gh(f"/repos/{REPO}/issues/{open_issues[0]['number']}/comments", "POST", {"body": report})
    else:
        gh(f"/repos/{REPO}/issues", "POST", {"title": TITLE, "body": report, "labels": [LABEL]})
    return 0


if __name__ == "__main__":
    sys.exit(main())
