---
title: "GitHub stale bot considered harmful"
date: 2025-09-16T23:19:17+02:00
tags:
  - bestof
  - dev
  - serenity
---

[Drew DeVault](https://drewdevault.com/2021/10/26/stalebot.html):

> One of GitHub's "recommended" marketplace features is the "stale" bot. The
> purpose of this bot is to automatically close GitHub issues after a period of
> inactivity, 60 days by default. You have probably encountered it yourself in
> the course of your work.
>
> This is a terrible, horrible, no good, very bad idea.
>
> I'm not sure what motivates maintainers to install this on their repository,
> other than the fact that GitHub recommends it to them. Perhaps it's motivated
> by a feeling of shame for having a lot of unanswered issues? If so, this might
> stem from a misunderstanding of the responsibilities a maintainer has to their
> project. You are not obligated to respond to every issue, implement every
> feature request, or fix every bug, or even acknowledge them in any way.

![github-actions stale bot automatically locking an issue](https://redacted.moe/f/e2f0d39c.png)

I second this.

Lately I've been encountering various CNCF projects that employ it (helm,
chart-testing), and it's [simply](https://github.com/helm/helm/issues/13192)
[awful](https://github.com/helm/chart-testing/issues/748).

I do not have anything else to add; Drew pretty much nails it.
