---
title: "GitHub: review only files owned by you"
date: 2026-04-28T11:01:10+02:00
tags:
  - bestof
  - dev
  - git
---

If you use
[`CODEOWNERS`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
on GitHub, there is a neat[^1] feature to streamline your pull request reviews.

Arguably, in large codebases, you're only interested in reviewing files owned by
you or your team. Wouldn't it be great if you could filter out files that you do
not own?

This [turns
out](https://github.com/microsoft/vscode-pull-request-github/issues/6624) to be
possible.

Workflow:

- go to a given pull request
- click "Files changed" in the top navbar (it's the last tab)
- on the left sidebar, click the filter button
- click "Only files owned by you"

_Boom_. The file noise is gone now!

In case you can't easily spot the filter button, take a look at the screenshot
in the link above.

[^1]: Neat and hard to discover!
