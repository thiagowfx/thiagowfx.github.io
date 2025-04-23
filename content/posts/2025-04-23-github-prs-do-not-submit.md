---
title: "Github PRs: do not submit"
date: 2025-04-23T12:47:20+02:00
tags:
  - dev
---

Sometimes you want to send a pull request for review to your teammates and want
to ensure they do not accidentally prematurely merge it.

One way to do so is to note in the commit message / PR description that it
should not be merged. Nonetheless, humans don't always read instructions, our
attention span is quite limited.

It would be more robust to employ a mechanism to prevent the PR from being
submitted, even if someone attempts to do so.

You could leave the PR as a draft. However, this could have the side effect that
not all CI checks may run. You don't want surprising failures later on, that
could slow you down.

I like the following approach, which is partly inspired by an internal presubmit
check at Google: write "DO NOT SUBMIT" in the PR title, and have a CI check
(github action[^1]) fail in this situation. Mark the action as
[required](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks):

> If status checks are required for a repository, the required status checks
> must pass before you can merge your branch into the protected branch. For more
> information, see About protected branches.

Use the following github action (`.github/workflows/pr-checks.yml`):

```yaml
name: PR Checks

permissions: read-all

on:
  pull_request:
    types: [opened, edited, synchronize]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  pr-checks:
    runs-on: ubuntu-latest
    steps:
      - name: '"DO NOT SUBMIT" check'
        env:
          PR_TITLE: ${{ github.event.pull_request.title }}
        run: |
          echo "Title: $PR_TITLE"

          if [[ "${PR_TITLE,,}" =~ "do not submit" ]]; then
            echo "::error::PR title '$PR_TITLE' must not contain 'DO NOT SUBMIT'"
            exit 1
          fi
```

`${PR_TITLE,,}` converts the PR title to lowercase so that the comparison is
case insensitive.

`=~ "do not submit"` is a regular expression to check if the title includes the
"DO NOT SUBMIT" string.

With the action in place, I can just update my PR title by prepending `DO NOT
SUBMIT:` to it. The prefix doubles down as a documentation of my intent.


[^1]: I don't think I'll ever remember the difference between a github action
    and a github workflow. One is reusable, the other one is not. I always
    forget which one.
