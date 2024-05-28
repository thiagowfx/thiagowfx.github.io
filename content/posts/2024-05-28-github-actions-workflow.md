---
title: "★ Github actions workflow"
date: 2024-05-28T10:23:22+02:00
tags:
  - bestof
  - dev
  - devops
---

This post exemplifies an efficient workflow to shorten the edit-refresh loop
when dealing with github actions.

<!--more-->

## Assumptions

- You have `git`, `jq` and the [`gh`](https://cli.github.com/) command-line tool
  installed (`brew install gh`)
- You have a github actions file in
  `~/.github/workflows/package-release-dispatch.yml`.
- The action has the following form:

```
on:
  workflow_dispatch:
    inputs:
      ref:
        description: 'Ref to build from. This can either be a SHA or a branch/tag'
        required: true
        type: string
  push:
    branches:
      - master
    paths:
      - '.github/workflows/package-release-dispatch.yml'
      - 'helm/**'
```

The goal is to iterate on the `jobs:` section of the action.

## Workflow

Trigger an action run from the command line:

```shell
gh workflow run package-release-dispatch.yml [--ref master] [-f ref=master]
```

`--ref` should be the git branch you're working on, for example,
`thiagowfx/my-cool-feature`.

`-f` provides an input to the workflow. In this case, there's an input named
`ref`, which is meant to be the branch the action will act upon.

The action takes a little while to trigger, we can `sleep` to give it some time.
I found that `sleep 3` is a sensible value (3 seconds).

How to view the action?

First we need to get its ID. Here's one way to do so:

```shell
gh run list --workflow=package-release-dispatch.yml --json databaseId --jq '.[0].databaseId'
```

### Option 1) Via the command-line

```shell
gh run watch <id>
```

It's analogous to `watch`, continuously refreshing the action progress in the
background, step by step. Example:

```
* master Package release dispatch · 12345678
Triggered via workflow_dispatch about 1 minute ago

JOBS
* build (ID 23456789)
  ✓ Set up job
  ✓ Checkout source code
  ✓ Run azure/setup-helm@v4
  ✓ Install yq
  ✓ Install helm cm-push plugin
  ✓ Set up Helm repos
  * Helm package all charts sans blacklist
  * Publish all helm packages
  * Post Checkout source code
```

### Option 2) Via the web browser

```shell
gh run view <id> -w
```

It will open the system web browser in the right page, pertaining to the action
run.

## Putting everything together

### Option 1)

```shell
gh workflow run package-release-dispatch.yml --ref master -f ref=master && \
  sleep 3 && \
  gh run watch $(gh run list --workflow=package-release-dispatch.yml --json databaseId --jq '.[0].databaseId')
```

### Option 2)

```shell
gh workflow run package-release-dispatch.yml --ref master -f ref=master && \
  sleep 3 && \
  gh run view $(gh run list --workflow=package-release-dispatch.yml --json databaseId --jq '.[0].databaseId') -w
```
