---
title: "VSCode: Github Pull Requests plug-in: collapse all comments by default"
date: 2025-05-14T14:40:34+02:00
tags:
  - dev
  - linux
---

**Problem statement**: I am constantly annoyed at opening files in VSCode with
PR comments being automatically expanded by default and occupying precious real
estate. Get rid of these comments!

[Github
issue](https://github.com/Microsoft/vscode-pull-request-github/issues/665):

> From your user settings with `"githubPullRequests.commentExpandState"`

I added the following to my `settings.json`:

```json
{
  "githubPullRequests.commentExpandState": "collapseAll",
}
```
