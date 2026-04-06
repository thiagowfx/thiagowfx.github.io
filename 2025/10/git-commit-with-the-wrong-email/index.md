---
title: "git: commit with the wrong email"
url: https://perrotta.dev/2025/10/git-commit-with-the-wrong-email/
last_updated: 2026-01-03
---


You are sending a PR upstream.

You accidentally commit it with the wrong email.

First, you prevent this mistake from happening again by updating your
`~/.gitconfig`.

And now you need to fix the most recent commit.

You can easily do so with:

```shell
% git commit --amend --reset-author --no-edit
```

Alternatively, with [my aliases](https://github.com/thiagowfx/.dotfiles):

```shell
git uncommit && git recommit
```

