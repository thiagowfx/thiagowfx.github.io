---
title: "friendly_ping: track your stale GitHub pull requests"
date: 2025-12-04T00:00:00Z
tags:
  - bestof
  - dev
  - serenity
---

I released a new tool:
[**friendly_ping**](https://github.com/thiagowfx/pancake/tree/master/friendly_ping),
a shell script to list all your open GitHub pull requests (still) waiting for
review.

## Problem

When contributing to multiple repositories on GitHub, it's easy to lose track of
which PRs are waiting for reviewer feedback[^1]. You end up doing one of:

- Manually checking GitHub every few days[^2]
- Forgetting about contributions entirely[^3]
- Having no visibility into the review status across various projects

## Solution

`friendly_ping` queries the GitHub API and groups your open PRs by repository:

```bash
$ friendly_ping

helm/helm
  fix(helm-lint): do not validate metadata.name for List resources
  https://github.com/helm/helm/pull/31169
  Reviewers: john, jane

  docs: update helm plugin installation guide
  https://github.com/helm/helm/pull/31204
  Reviewers: jane

loeffel-io/ls-lint
  feat: introduce a json schema file for ls-lint
  https://github.com/loeffel-io/ls-lint/pull/256
```

_(The examples above are semi-fictitious.)_

## Features

**Filtering**:

- Filter by organization: `friendly_ping --org helm` (your company)
- Filter by date range: `friendly_ping --created-after "30 days"` (find old PRs)
- Filter by specific repos: `friendly_ping thiagowfx/.dotfiles thiagowfx/pre-commit-hooks` (or one repo at a time)
- Filter by reviewer/assignee: `friendly_ping --involves alice --detailed`
  (filter by a specific teammate, handy for your 1:1s)

**Grouping**:

- By reviewer: `friendly_ping --group-by reviewer --detailed`
- By assignee: `friendly_ping --group-by assignee --detailed`
- By user (reviewers and assignees combined): `friendly_ping --group-by user --detailed`

The default grouping is per repo.

**Comments**:

- Add "friendly ping" comments to PRs: `friendly_ping --comment`
- Custom messages: `friendly_ping --comment "Please review when you get a
  chance. Deadline is approaching!"`
- Automatically skips PRs wherein you already commented
- Appends context about how long the PR has been waiting ("waiting for 3 days")

**Other modes**:

- JSON output: `friendly_ping --json`
- Quiet mode for scripts: `friendly_ping --quiet && echo "You have open PRs"`

## Prerequisites

- `gh` (GitHub CLI) — preferred method, or `curl` as fallback
- `jq` — for JSON processing
- Git configured with `user.name` (or use `--user` flag)

## Repository

Contributions welcome. This was fully vibe-coded by [Amp
Code](https://ampcode.com/). The CLI design was fully my own.

This could be extended beyond GitHub, naturally.

[^1]: Some people take forever to review PRs / CLs...
[^2]: Or multiple times a day.
[^3]: The non-urgent ones.
