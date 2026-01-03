---
title: "git reset --keep"
date: 2024-12-31T18:54:59-03:00
tags:
  - dev
  - git
---

In all these years of `git`, I've only heard about it now: via [Adam
Johnson](https://adamj.eu/tech/2024/09/02/git-avoid-reset-hard-use-keep/):

> Git: avoid reset --hard, use reset --keep instead
>
> But whilst researching for my book on Git, I discovered git reset --keep in
> the documentation. The description there is brief and oblique, but after
> figuring it out, I realized that --keep is way more preferable to --hard!

I have a `git uncommit` alias in my `~/.gitconfig`:

```
uncommit = !git reset --soft HEAD^ && git restore --staged .
```

...which is akin to "undo".

And there's the nuclear `git reset --hard` + `git clean -x -f -d` to "reset
everything".

`git reset --keep` seems like a safer `git reset --hard`. Adam did a good job
describing how it works, so go read it directly there.

This has the same spirit as [`git push --force-with-lease`]({{< ref
"2024-12-20-git-push-force-with-style" >}}).
