
## How can we create an empty commit in `git`?

```shell
mkdir repo
cd repo
git init
git commit --allow-empty -n -m "blank commit"
```

```shell
% git log
commit effe4480543051e13838d4fbc127f01f658c07dc (HEAD -> master)
Author: Thiago Perrotta <{redacted-email}>
Date:   Fri Feb 14 13:52:19 2025 +0100

    blank commit
```

## Why is this useful?

1) [dependabot](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide)
[cannot](https://jongleberry.medium.com/accessing-github-actions-secrets-for-dependabot-pull-requests-on-private-repositories-b0dd6995f21b)
access secrets in github actions. There's one workaround: check out the pull
request locally, add a blank commit on top of it, then push it back. _Boom_.
The secrets are suddenly accessible.

2) create a commit _in advance_ of coding it, à la
[TDD](https://en.wikipedia.org/wiki/Test-driven_development). Declaring your
intent first can help with focus and scope. You can always update the commit
message afterwards with `git commit --amend`[^1].

2.1) create a pull request (merge request) _in advance_ of coding it. So that
you can have a PR number that can be shared with your teammates and/or linked to
from your bug tracker software.

## My aliases

```shell
% grep -E '(alias|blank|desc)' ~/.gitconfig
[alias]
        blank = desc -m \"blank commit\"
        desc = commit --allow-empty -n
```

[^1]: Which I alias to `git reword`.

