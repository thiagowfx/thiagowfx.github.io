---
title: "zsh: glob qualifiers: most recent"
date: 2026-02-15T02:10:49+01:00
tags:
  - dev
---

TIL via [Adam
Johnson](https://adamj.eu/tech/2026/01/27/zsh-om1-glob-qualifiers/):

> Zsh: select generated files with (`om[1]`) glob qualifiers
>
> [...]
>
> In Zsh, we can avoid copying such generated filenames by using glob
> qualifiers, which are extra syntax you can add to filename globs in Zsh.
> Specifically, we want to attach the glob qualifiers `om[1]`, which mean:
>
> — `o`: sort the matches
> — `m`: by modification time, most recent first
> — `[1]`: select only the first match
>
> Attaching these qualifiers to appropriate globs allows commands to pick up a
> generated file without knowing its exact name.

This is akin to `ls -t | head -n 1`. For example, here are both commands in the
repository of this blog:

```shell
% ls -r -t content/posts/* | head -n 1
content/posts/2026-02-15-zsh-glob-qualifiers-most-recent.md
```

`-r` is `--reverse`, so that we get the most recent post instead of the oldest
one.

Now with `zsh` glob qualifiers:

```shell
% ls content/posts/*.md(om[1])
content/posts/2026-02-15-zsh-glob-qualifiers-most-recent.md
```

You could also fetch the two most recent posts:

```shell
% ls content/posts/*.md(om[1,2])
content/posts/2026-02-13-new-blog-post-via-claude-code.md
content/posts/2026-02-15-zsh-glob-qualifiers-most-recent.md
```

Or perhaps only the second most recent post:

```shell
% ls content/posts/*.md(om[2])
content/posts/2026-02-13-new-blog-post-via-claude-code.md
```

Listing files isn't very interesting. Here's a more practical use case: delete
the most recent file:

```shell
% rm *(om[1])
```

Or open the most recent file in `$EDITOR`:

```shell
$EDITOR content/posts/*.md(om[1])
```

`om` operates by time of last modification, but there's also `on` for
alphabetical sorting and `oL` for file size (length) sorting.

Refer to the [zsh
docs](https://zsh.sourceforge.io/Doc/Release/Expansion.html#Glob-Qualifiers) for
more.
