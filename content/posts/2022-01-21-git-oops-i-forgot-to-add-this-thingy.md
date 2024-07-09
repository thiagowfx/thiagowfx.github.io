---
title: "Git: Oops I forgot to add this thingy"
date: 2022-01-21T15:58:17-05:00
tags:
  - dev
---

Here's a situation that happens often during development:

Suppose you committed something to `git`. A few commits later, you realized you
forgot to add something to that commit, or possibly missed a link, or even
spotted a typo. How do you go about fixing it?

<!--more-->

## Team

If you're working on a repository with a team, you should just `git commit` and `git push`. Write an [eloquent commit message][commit-message] to refer to the previous commit in which you forgot to include your changes.

## Self

Now, if you're working on a standalone repository, just for yourself[^1], this
creates an opportunity to rewrite your history in a cleaner way. The workflow
is as follows:

1. Make the changes or fixes you had originally forgot to.
2. `git add` them.
3. Identify the commit id in which you originally wanted to make those changes. `git log` or [`tig`][tig] are simple CLI-oriented ways to do so. Hereafter assume this id is `abcdef`.
4. Commit your changes while referencing the original commit and then rewrite history:

```shell
$ git commit --fixup=abcdef

# Then pick one of:
$ git rebase -i --root
$ git rebase -i abcdef~1

# And then save the file as is.
```

5. Double-check everything went as expected with `git log` and/or `git show` and/or `tig`.
6. If you're happy with the current state of your repository, commit the sin: `git push --force`.

{{< figure align="center" src="https://imgs.xkcd.com/comics/git_commit.png" link="https://xkcd.com/1296/" alt="Merge branch 'asdfasjkfdlas/alkdjf' into sdkjfls-final" attr="XKCD Courtesy of Randall Munroe" >}}

## References

- `tig`, in case you don't know:

> [`tig`][tig] is an ncurses-based text-mode interface for git. It functions mainly as
> a Git repository browser, but can also assist in staging changes for commit
> at chunk level and act as a pager for output from various Git commands.

- `git rebase --root`: c.f. [Stack
  Overflow](https://stackoverflow.com/a/23000315/1745064). This is just a lazy
  way to make the rebase include `abcdef`. You could do something like `git
  rebase -i HEAD~10` where 10 is an arbitrary guess, but this will only work if
  `abcdef` is within the most 10 recent commits. Alternatively `git rebase -i
  abcdef~1` also works.


[commit-message]: https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[tig]: https://jonas.github.io/tig/

[^1]: For example: your [dotfiles](https://github.com/thiagowfx/.dotfiles), or your personal blog.
