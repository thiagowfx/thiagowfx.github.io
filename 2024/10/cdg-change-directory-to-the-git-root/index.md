
Shell:

```shell
alias cdg='cd "$(git root)"'
```

`~/.gitconfig`:

```
[alias]
  root = rev-parse --show-toplevel
```

Sadly it is not possible to do so with a git alias, c.f. https://stackoverflow.com/questions/19032372/git-alias-for-shell-command-to-cd-into-git-root-not-working-as-expected:

> Your shell is invoking Git, and Git is invoking another shell in which to run
> your cd command. This command is successful, and this changes the working
> directory of the child shell, but it does not change the working directory of
> Git, nor of the parent shell.
>
> In order to do this you need to run the command in your current shell, which
> means that invoking Git will not be able to accomplish this. You will have to
> continue using a shell alias.

Since we cannot change directory with a git alias, then at least we can use one
to print the repository root.

