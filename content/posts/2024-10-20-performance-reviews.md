---
title: "Performance reviews"
date: 2024-10-20T12:15:14+02:00
tags:
  - dev
---

During performance reviews[^1], it's handy to obtain an overview of your
accomplishments that are stored as artifacts in source control systems.


Usually accomplishments for a software engineer span more than just code: design
documents, documentation, bug triage and fixes, product health initiatives,
tackling of technical debt, processes...the list is endless.

Nonetheless in this post I'll focus only in contributions in the form of code.

99.999% of the time this means `git` commits (and/or pull requests, if you will).

Other than `git`, and the _very very very_ occasional mercurial (`hg`), the only
other VCS I used significantly was Google's Perforce / Piper.

## Piper

Although there are command-line tools to summarize your accomplishments, I
find the easiest way to do so is via Critique.

### Your CL submissions

Use a query like:

```
(author:me OR pair:me) is:submitted since:2024-01-03 to:2024-01-09
```

Update `since` and `to` according to the current PERF / GRAD cycle.

If you are a high-performer and/or send lots of LSCs (large-scale changes), the
output can be noisy. Filter it out with `d:{description}` as needed.

For example, to call out LSC changes in a separate section in your packet, you
may want to exclude them from your overall contributions with `-d:LSC` or
`-d:Rosie` or similar.

`pair` is for crediting pair programming.

**Disclaimer**: There is a possibility the syntax is incorrect, as I am not able
to test it at the moment.

### Your CL reviews

```
r:me is:submitted since:2024-01-03 to:2024-01-09
```

You'll likely want to call out readability reviews separately. Use something
like `-cc:typescript-readability-approvers`.

## `git`

One option is to use the web UI of your forge (GitHub, GitLab, etc).

I strive for a forge-agnostic solution though.

### Your pull requests / commits

[`git shortlog`](https://git-scm.com/docs/git-shortlog) is your friend!

Example for this blog:

```shell
% git shortlog --author="Thiago Perrotta" --since="6 months ago"  # alt: --since="2024-03-01"
Thiago Perrotta (499):
      Initial commit
      add gitignore: go,hugo,vim
      hugo: add config.toml and default archetype
[...]
```

If there are multiple repositories, combine the command with [`myrepos`](https://myrepos.branchable.com/):

```shell
% mr run git shortlog --author="Thiago Perrotta"
```

To filter out irrelevant commits, use `grep -v`. Example:

```shell
% git shortlog --author="Thiago Perrotta" | grep -Ev '^\s*ci|^.*pre-commit'
```

...filters out commits that contain "ci" or "pre-commit" in the message summary.

### Your PR reviews

PR reviews are a concept from forges. From a `git` CLI perspective it would only
be possible to do so when automation adds git tags to commits e.g. `Reviewed-by:
Thiago Perrotta <thiago@example.com>`.

[Gerrit](https://www.gerritcodereview.com/) does that.
[Here](https://chromium-review.googlesource.com/c/chromium/src/+/5012895) is an
example in Chromium. In this case, one could just `grep` for `Reviewed-by` in
`git log`.

Otherwise: on GitHub, use a query such as `is:pr reviewed-by:@me` in the Pull
Request search tab.

[^1]: PERF, GRAD, TPG: there are all sorts of naming schemes for them.
