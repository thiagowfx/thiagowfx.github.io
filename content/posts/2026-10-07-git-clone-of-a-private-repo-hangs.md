---
title: "git clone of a private repo hangs"
date: 2026-10-07T20:45:30+01:00
tags:
  - dev
  - git
  - security
---

**Problem statement**: `git clone {repo}` hangs. How to troubleshoot?

Assumption: we're cloning via SSH, not via HTTPS.

First, ensure the proper SSH key is being used:

```shell
% ssh -vT {repo}
```

If that's not the case, you'll need to modify `~/.ssh/config` accordingly (out
of scope of this post).

Next up, run:

```shell
GIT_TRACE=1 git clone -v {repo}
```

It will emit logs during the clone. If there's an error, the answer will be
there.
