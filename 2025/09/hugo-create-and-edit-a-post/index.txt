
It's interesting to glimpse into how my blogging workflow has been evolving over
time.

[Previously]({{< ref "2022-10-09-do-i-still-remember-how-to-blog" >}}),
[previously]({{< ref "2024-12-13-just" >}}).

It started with `hugo new`, then `just new` + `vim`
([Justfile](https://github.com/casey/just)), and now I am introducing a subtle
change, inspired by [`bneil`](https://bneil.me/notes/zshrc_alias_for_hugo/).
This post:

```shell
% just new "hugo: create and edit a post"
```

It creates this file, and automatically opens it in my `$EDITOR`:

```
---
title: "Hugo create and edit a post"
date: 2025-09-15T12:44:31+02:00
tags:
{list of tags pre-populated}
---
```

The more I can reduce the friction to blogging[^1] the better.

[^1]: Up to a [certain extent]({{< ref "2025-03-18-friction" >}}).

