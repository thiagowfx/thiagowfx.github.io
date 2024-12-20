---
title: "git: push --force with style"
date: 2024-12-20T00:38:07-03:00
tags:
  - dev
  - devops
---

TIL:

> `git push --force`: This command forcefully pushes your changes to the remote
> branch, even if it results in overwriting or losing commits. It does not
> consider the current state of the remote branch. If someone else has pushed
> changes to the same branch in the meantime, their changes will be lost.

> `git push --force-with-lease`: This command is a safer alternative to git push
> — force. It will only force push if the remote branch matches your
> expectations. It checks if someone else has pushed changes to the branch in
> the meantime. If the branch on the remote repository has not diverged (i.e.,
> no new commits were pushed by others), your push will be allowed. If someone
> else has pushed changes, the push will be rejected, ensuring you do not
> accidentally overwrite someone else’s work.


[(via)](https://medium.com/@sahilsahilbhatia/git-push-force-with-lease-vs-force-ecae72601e80).

How nice! Why is `--force-with-lease` not the default behavior?

[Stack
Overflow](https://stackoverflow.com/questions/30542491/push-force-with-lease-by-default)
to the rescue...

> I just learned about `git push --force-with-lease`. It's pretty awesome. But,
> of course, I don't use force that often, and so I'm worried that I might
> forget about this nifty feature the next time I need it. Is there a way to
> configure git so git push -f will automatically use `--force-with-lease`
> unless I intentionally override it with `--no-force-with-lease`?

...amen, you read my mind, OP!

The accepted answer, to my despair:

> There currently is no way to configure git to always use force-with-lease
> instead of force. As such the next best available option is, as so often, to
> create an alias which serves this purpose.
