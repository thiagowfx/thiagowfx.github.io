---
title: "offboarding: export your own work before the laptop is wiped"
url: https://perrotta.dev/2026/09/offboarding-export-your-own-work-before-the-laptop-is-wiped/
last_updated: 2026-09-30
---


**Problem statement**: what is worth taking home on the last day at work,
without taking the company's code or data?

The line I drew: my work history, my own words, my contacts, my notes. Not
source code, not runbooks, not customer data. Everything else the company keeps.
Metadata about my contributions is mine to remember; the artifacts are theirs.

I pointed an AI harness at the connectors I already had (GitHub, Jira,
Confluence, Gmail, Drive, Calendar, Slack, the HR directory) and asked it to
build an inventory. It landed in one folder:

```shell
% eza -T -L1 ~/Downloads/offboarding
offboarding
├── README.md
├── resume-highlights.md
├── merged-prs.csv
├── jira-done.jsonl
├── jira-epics.md
├── contacts.csv
├── gmail-index.md
├── emails/
├── drive-index.md
├── drive-files/
├── confluence/
├── calendar-summary.md
├── slack-export.md
├── github-insights.md
├── chrome-bookmarks-work-profile.html
└── claude-memory/
```

The GitHub part is pure API, no clone. Merged PRs, paginated once:

```shell
% gh api graphql --paginate -f query='query($c: String) { viewer {
    pullRequests(first: 100, states: MERGED, after: $c) {
      pageInfo { hasNextPage endCursor }
      nodes { mergedAt repository { nameWithOwner } title additions deletions }
    } } }' --jq '.data.viewer.pullRequests.nodes[]' | jq -s . > merged_prs.json
% jq -r '.[].mergedAt[:4]' merged_prs.json | sort | uniq -c
 892 2024
1160 2025
1436 2026
```

Titles, dates, and line counts only. That is enough to write a resume bullet
later; the diffs stay behind. Same idea for Jira (`assignee = currentUser() AND
statusCategory = Done`) and for Confluence (`creator =
currentUser()`).

Two things were clearly mine and would have been lost: the "working with me"
email from week one, and a first-day checklist I mailed to myself. Both went
into `emails/` verbatim. The Slack kudos channel got the same treatment,
because nobody will write a reference from memory two years from now.

The README in the folder lists what was deliberately not exported: source code,
PR descriptions, runbook bodies, performance reviews.

