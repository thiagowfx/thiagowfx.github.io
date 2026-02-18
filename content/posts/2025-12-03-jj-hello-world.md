---
title: "jj: hello world"
date: 2025-12-03T03:43:01-03:00
tags:
  - dev
  - serenity
---

I am reasonably confident to end up (_fully_) adopting
[`jj`](https://github.com/jj-vcs/jj) in 2026. Baby steps though.

Can I attempt to start to use `jj` to manage this blog?

First, the usual:

```shell
brew install jj
```

Second, a basic config file. `git` requires one too:

```shell
% cat ~/.config/jj/config.toml
[user]
name = "Thiago Perrotta"
email = "{redacted}"

[ui]
default-command = "log"
```

So far so good.

Third, initialize a `jj` repo alongside ("co-located") the existing `git` repo
of this blog:

```shell
% jj git init --colocate
Done importing changes from the underlying Git repo.
ignoring git submodule at "vendor/ai.robots.txt"
Setting the revset alias `trunk()` to `master@origin`
Hint: The following remote bookmarks aren't associated with the existing local bookmarks:
  master@origin
Hint: Run the following command to keep local bookmarks updated on future pulls:
  jj bookmark track master@origin
Initialized repo in "."
Hint: Running `git clean -xdf` will remove `.jj/`!
```

I am fine with the second hint, even though I don't fully comprehend it:

```shell
% jj bookmark track master@origin
```

I got this advice[^1]:

> For jj in a blog repo (especially with colocated Git):

> 1. Use small, focused commits — jj makes this easy; amend frequently with jj
>    amend instead of stashing
> 2. Leverage jj log — understand your repo state before operations
> 3. Work on branches — jj new -b feature-name for feature work, keeps main
>    clean
> 4. Keep commits working — jj can track your working changes automatically
> 5. Use jj sync — pulls and pushes in one command with Git

OK.

I know `jj` does not have the concept of a staging area, thus there's no
`jj add`. I double-checked:

```shell
% jj add
error: unrecognized subcommand 'add'
```

Then what should I do...commit?!

```shell
% jj commit
```

Opens `$EDITOR`:

```
add hello world

JJ: Change ID: vvvzruls
JJ: This commit contains the following changes:
JJ:     A content/posts/2025-12-03-jj-hello-world.md
JJ:
JJ: Lines starting with "JJ:" (like this one) will be removed.
```

Follow-up:

```shell
% jj commit
Working copy  (@) now at: loyssymn 4ba8427d (empty) (no description set)
Parent commit (@-)      : vvvzruls d6c2ee34 add hello world
```

Fancy! Now what? I learned that whenever I am lost, `jj` is your friend. `jj`
(or `jj log`) is akin to `git status` and/or `git log`.

```shell
% jj
@  loyssymn {redacted email} 2025-12-03 04:00:08 9df24e6a
│  (no description set)
○  vvvzruls {redacted email} 2025-12-03 03:59:00 git_head() d6c2ee34
│  add hello world
│ ○  oqwvuopo {redacted email} 2025-12-03 03:36:43 likes 907c5e72
├─╯  git-freeze
◆  oqwnlpuv {redacted email} 2025-12-02 23:12:39 master a9efb058
│  bytebytego: Product Array Without Current Element
~
```

There's also:

```shell
% jj status
Working copy changes:
M content/posts/2025-12-03-jj-hello-world.md
Working copy  (@) : loyssymn 54ba540b (no description set)
Parent commit (@-): vvvzruls d6c2ee34 add hello world
```

Whilst I keep adding text to this file...

```shell
% git st
## HEAD (no branch)
 M content/posts/2025-12-03-jj-hello-world.md
```

Oh, look! Our friend is still around.

```shell
% jj amend
error: unrecognized subcommand 'amend'

For more information, try '--help'.
Hint: You probably want `jj squash`. You can configure `aliases.amend = ["squash"]` if you want `jj amend` to work.
```

Really? Oh.

```shell
thiago@thiagoperrotta-MacBook-Pro ~blog (git)-[jj/keep/d6c2ee34fe38ec5a63644114c4c3b13bb09401f1]
% jj squash
Working copy  (@) now at: kpumvxpm e60fb5b5 (empty) (no description set)
Parent commit (@-)      : vvvzruls bba2f04e add hello world
```

Weird:

```
thiago@thiagoperrotta-MacBook-Pro ~blog (git)-[jj/keep/bba2f04ecd437d8d27e4c8103cb61fc936cd0d89]
% jj
@  kpumvxpm {redacted email} 2025-12-03 04:03:57 41b2cf2f
│  (no description set)
○  vvvzruls {redacted email} 2025-12-03 04:03:21 git_head() bba2f04e
│  add hello world
│ ○  oqwvuopo {redacted email} 2025-12-03 03:36:43 likes 907c5e72
├─╯  git-freeze
◆  oqwnlpuv {redacted email} 2025-12-02 23:12:39 master a9efb058
│  bytebytego: Product Array Without Current Elemen
~
thiago@thiagoperrotta-MacBook-Pro ~blog (git)-[jj/keep/bba2f04ecd437d8d27e4c8103cb61fc936cd0d89]
% jj status
Working copy changes:
M content/posts/2025-12-03-jj-hello-world.md
Working copy  (@) : kpumvxpm 41b2cf2f (no description set)
Parent commit (@-): vvvzruls bba2f04e add hello world
thiago@thiagoperrotta-MacBook-Pro ~blog (git)-[jj/keep/bba2f04ecd437d8d27e4c8103cb61fc936cd0d89]
% git status
## HEAD (no branch)
 M content/posts/2025-12-03-jj-hello-world.md
```

I thought `amend` (or `squash`) would be akin to `git commit --amend`, but
apparently not? I see two nodes.

Remember the advice from a while ago?

```shell
% jj sync
error: unrecognized subcommand 'sync'
```

Lame.

Time for `jj help -k tutorial` (linked to from `jj --help`).

At this point I just want to end the post. I'll try `jj git push`. If I am
cut-off, it means it has worked. And we'll continue this in 2026.

```shell
% jj git push
Warning: No bookmarks found in the default push revset: remote_bookmarks(remote=origin)..@
Nothing changed.
```

Errr.

```shell
% jj checkout master
error: unrecognized subcommand 'checkout'

Usage: jj [OPTIONS] <COMMAND>

For more information, try '--help'.
```

```shell
% jj describe -m "new just: jj hello world"
Working copy  (@) now at: kpumvxpm 516b5d69 new just: jj hello world
Parent commit (@-)      : vvvzruls bba2f04e add hello world
```

This is the moment of the post when I had to bail out to `git`.

Somehow two distinct commits were created. :(

Until next time.

[^1]: From whom? From what? Mystery? I think you know the answer.
