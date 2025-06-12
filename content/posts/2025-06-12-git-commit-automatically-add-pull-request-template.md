---
title: "git commit: automatically add pull request template"
date: 2025-06-12T21:09:36+02:00
tags:
  - bestof
  - dev
---

GitHub supports [pull request
templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository).
Define a `.github/PULL_REQUEST_TEMPLATE.md` directory in your git repo, and it
will be automatically used when creating PRs via the GitHub web UI and via the
CLI tool ([`gh`](https://cli.github.com/)).

But what about commits created locally, via a plain `git commit`?

As per [git
docs](https://git-scm.com/docs/git-commit/2.49.0#Documentation/git-commit.txt-code--templateltfilegtcode):

> `commit.template`
>
> Specify the pathname of a file to use as the template for new commit messages.

Therefore, the following `~/.gitconfig` works:

```
[commit]
  template = .github/PULL_REQUEST_TEMPLATE.md
```

The file path (pathname) is relative to the git repository root.

However, this will fail in repositories that do not have a template:

```
% git commit
fatal: could not read '.github/PULL_REQUEST_TEMPLATE.md': No such file or directory
```

There's a workaround: use [`includeIf`](https://git-scm.com/docs/git-config#_includes):

```shell
% tail -3 ~/.gitconfig
# Import corp configs if any.
[include]
        path = .gitconfig_corp
```

```shell
% cat ~/.gitconfig_corp
[includeIf "gitdir:~/mycompany/**"]
  path = .gitconfig_mycompany

[includeIf "hasconfig:remote.*.url:git@github.com:mycompany/**"]
  path = .gitconfig_mycompany
```

```shell
% cat ~/.gitconfig_mycompany
[commit]
        template = .github/PULL_REQUEST_TEMPLATE.md
```

This way, the github PR template is only included for git repositories from my
company.
