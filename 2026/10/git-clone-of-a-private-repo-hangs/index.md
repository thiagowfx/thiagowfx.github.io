---
title: "git clone of a private repo hangs"
url: https://perrotta.dev/2026/10/git-clone-of-a-private-repo-hangs/
last_updated: 2026-10-07
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

