---
title: "git: developer certificate of origin (DCO) sign-off"
date: 2025-07-24T12:37:31+02:00
tags:
  - dev
  - git
---

The [Developer Certificate of Origin](https://developercertificate.org/) (DCO
for short) is often required when sending out PRs upstream.

For example, contributions to the Linux kernel
[mandate](https://wiki.linuxfoundation.org/dco) it.
[Other](https://cert-manager.io/docs/contributing/sign-off/)
[projects](https://gcc.gnu.org/dco.html)
[too](https://docs.pi-hole.net/guides/github/dco/).

It's even possible to enforce it via [Github
Actions](https://github.com/apps/dco).

Suppose that you sent a PR with a single commit but forgot to sign it off. You
can amend it with:

```shell
git rebase HEAD~1 --signoff
git push --force-with-lease origin [branch]
```

Or you can do it proactively, at commit time:

```shell
git commit [-s | --signoff]
```

It is
[often](https://stackoverflow.com/questions/77279077/how-to-sign-off-every-git-commit)
[discouraged](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatsignOff)
to have `git` automatically do it:

> Adding the Signed-off-by trailer to a patch should be a conscious act and means
> that you certify you have the rights to submit this work under the same open
> source license.

In practice, a sign-off is an ordinary [git
footer](https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/git-footers.html):

```
Signed-off-by: John Doe <john@example.com>
```
