
[Preliminaries](https://stackoverflow.com/questions/57265785/whats-the-difference-between-git-switch-and-git-checkout-branch#57266005):

> What's the difference between 'git switch' and 'git checkout' <branch>?
>
> Git 2.23 introduces a new command `git switch`. After reading the
> documentation, it seems pretty much the same as `git checkout <branchname>`.
> What is the difference or use case?
>
> `git switch` can now be used to change branches, as git checkout <branchname>
> does
>
> People are confused by these different ways to use git checkout, as you can
> see from the many questions regarding git checkout here on Stack Overflow. Git
> developers seem to have taken this into account.

[`git switch`](https://git-scm.com/docs/git-switch/2.23.0) is the idiomatic way
to switch branches these days. `git checkout` can be ambiguous; not only it
switches branches, it can also revert/reset files and directories.

I unexpectedly hit this ambiguity today.

I have this `git bd` alias:

```
% grep -E '(bd|default\b)' ~/.gitconfig
        bd = !branch="$(git branch --show-current)" && git default && git branch -D "${branch:-$1}"
        default = !git checkout main &>/dev/null || git checkout master
```

...which is short for "branch delete".

**Example**: I am working on branch `thiagowfx/my-branch`, then the commit/PR is
eventually merged. My next action is `git bd`, which a) switches to the default
branch (main or master these days) and b) deletes the previous branch.

This works well most of the time.

Today, when
[bumping](https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/81638)
the `yamlfmt`
[package](https://pkgs.alpinelinux.org/package/edge/testing/x86_64/yamlfmt) for
Alpine Linux, I was in the `yamlfmt` branch and then ran `git bd`.

That didn't do anything. Here's the problem:

```
% tree -L 1
.
├── CODINGSTYLE.md
├── COMMITSTYLE.md
├── README.md
├── community
├── main
├── scripts
└── testing
```

...there's a `main/` directory in the repository root.

Thus `git default`, which calls `git checkout main`, treats `main` as a
directory in this context, instead of a branch.

One solution is to call `git checkout main --` instead, which explicitly denotes
`main` as a branch[^1]. However, that's hard to remember and it's also
confusing. It's easier to simply do `git switch main`.

So here's my updated alias, which works as originally intended:

```
% grep -E '(bd|default\b)' ~/.gitconfig
        bd = !branch="$(git branch --show-current)" && git default && git branch -D "${branch:-$1}"
        default = !git switch main &>/dev/null || git switch master
```

[^1]: To explicitly denote it as a directory / file, call `git checkout -- main`
    instead. I use this variant often to revert file modifications back to the
    original state.

