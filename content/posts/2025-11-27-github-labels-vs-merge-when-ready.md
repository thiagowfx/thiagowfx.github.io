---
title: "GitHub labels vs merge when ready"
date: 2025-11-27T16:00:28-03:00
tags:
  - dev
---

GitHub allows marking PRs to be [merged when
ready](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request-with-a-merge-queue).
This means a merge operation will automatically happen in the background once
all PR requirements are satisfied i.e. CI checks pass, teammate approvals, etc.

At Google (Critique, Piper) there's an equivalent setting for internal
CLs, which happens to be named "Auto Submit".

I am a big fan of both mechanisms.

Marking a PR as ready to be auto-merged, or a CL as ready to be auto submitted,
is a signal from my side that I am confident the PR / CL is in its final state,
expecting few to no review comments.

That said: this happens to be an issue whenever I need two or more reviewers to
sign-off on my changes.

As soon as the first reviewer approves the PR / CL, it would be merged, right
away. What if I need to wait for the second reviewer as well?

In Critique one can address this by adding a `WANT_LGTM=all` footer to the CL
description. Now Piper will enforce that the CL is only merged once all
reviewers approve it.

In GitHub there's no straightforward out-of-the-box equivalent. There are ways
to work around the platform limitations, but they all seem hacky to me.

I found an alternative: design a `done`
[label](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels)
to represent that no further changes are planned in the PR.

Now the second (or last, if more than two) reviewer can be confident to trigger
the merge of the PR as soon as they approve it.

Adopting this convention is a team process.
