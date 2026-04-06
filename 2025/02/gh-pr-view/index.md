---
title: "gh pr view"
url: https://perrotta.dev/2025/02/gh-pr-view/
last_updated: 2025-06-15
---


When working on a local git branch that has a github PR associated to it, at
some point you'll want to open its pull request page.

If you have the [github CLI](https://cli.github.com/) installed (`gh`), you can do so with `gh pr view
--web`.

If you don't pass `--web`, then it will simply output markdown.

