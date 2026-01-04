
[Previously]({{< ref "2025-12-22-git-stash-untracked" >}}).

If we can stash untracked files (`git stash -u`), should we be able to `git
diff` untracked files?

Naturally, diffing an untracked file would output the entire file contents.
Still, this can be desirable sometimes.

When reviewing multiple files, some of which are modified, and some of which
are brand new, you may want to review the entire list at once.

Let's try it out:

```shell
% cdtmp
/var/folders/yr/6sw3yylx6gjcy5jr38d6j6000000gn/T/thiago.perrotta-2026-01-04-l8Co7f
% git init
Initialized empty Git repository in /private/var/folders/yr/6sw3yylx6gjcy5jr38d6j6000000gn/T/thiago.perrotta-2026-01-04-l8Co7f/.git/
% echo world > hello.md
% git status
## No commits yet on master
?? hello.md
% git diff
% git diff -u
```

Err, no luck. In fact, from [`git-diff(1)`](https://man.archlinux.org/man/git-diff.1):

> -p, -u, --patch
>
> Generate patch (see the section called "GENERATING PATCH TEXT WITH -P").
> This is the default.

Ouch. That's not the `-u` we're looking for!

We can attempt a similar test with `git add -p`:

```shell
% cdtmp
/var/folders/yr/6sw3yylx6gjcy5jr38d6j6000000gn/T/thiago.perrotta-2026-01-04-l8Co7f
% git init
Initialized empty Git repository in /private/var/folders/yr/6sw3yylx6gjcy5jr38d6j6000000gn/T/thiago.perrotta-2026-01-04-l8Co7f/.git/
% echo world > hello.md
% git status
## No commits yet on master
?? hello.md
% git add -p
No changes.
```

No luck either.

Not all hope is lost though.

Enter [`git add -N` (`--intent-to-add`)](https://man.archlinux.org/man/git-add.1#:~:text=ignored%20removed%20files.-,%2DN%2C%20%2D%2Dintent%2Dto%2Dadd,-Record%20only%20the):

```
> -N, --intent-to-add
>
> Record only the fact that the path will be added later. An entry for the
> path is placed in the index with no content. This is useful for, among other
> things, showing the unstaged content of such files with git diff and
> committing them with git commit -a.
```

If we do `git add -N hello.md`, the following happens:

```shell
% git add -N hello.md
% git --no-pager diff
diff --git hello.md hello.md
new file mode 100644
index 0000000..cc628cc
--- /dev/null
+++ hello.md
@@ -0,0 +1 @@
+world
```

Yes! There's our diff. Now `git add -p`:

```shell
% git add -N hello.md
% git add -p
diff --git a/hello.md b/hello.md
new file mode 100644
index 0000000..cc628cc
--- /dev/null
+++ b/hello.md
@@ -0,0 +1 @@
+world
(1/1) Stage addition [y,n,q,a,d,e,p,P,?]?
```

It works too!

In order to make this workflow ergonomic, run `git add -AN` (`-A` = `--all`)
prior to `git diff` or `git add -p`, so that all new files are accounted for.

