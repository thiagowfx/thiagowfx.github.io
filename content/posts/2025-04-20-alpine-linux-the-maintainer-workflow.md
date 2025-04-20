---
title: "Alpine Linux: the maintainer workflow"
date: 2025-04-20T15:12:09+02:00
tags:
  - bestof
  - dev
  - linux
  - selfhosted
---

I maintain [a couple of
packages](https://pkgs.alpinelinux.org/packages?name=&branch=edge&repo=&arch=x86_64&origin=&flagged=&maintainer=Thiago+Perrotta)
on Alpine Linux.

Every now and then, a new software version is released, and it's my duty[^1] as an
active package maintainer to update my packages.

The typical workflow looks like the following.

First I get an email notification from "Alpine Package DB":

> Dear Thiago Perrotta
>
> This is an automatic message send from pkgs.alpinelinux.org
> One or more of your aports have been flagged out of date based on
> Anitya monitoring system <https://release-monitoring.org/>
>
> argocd current: 2.14.2-r1 new: 2.14.9
>
> To update the package you can use our helper script:
>
> abump aport-version
>
> If the provided information is incorrect, please let us know on IRC
> or alpine-infra@alpinelinux.org. Thanks!

It's important not to [burn oneself
out](https://opensource.com/business/15/12/avoid-burnout-live-happy).

I treat these notifications as an FYI. They _are not_ prompts to make me
immediately go and update the packages[^2]. For packages with frequent updates,
like `argocd`, I'll let a few patch versions accumulate before I take action.
Other times it is handy to batch package upgrades together so to do them all at
once. I use my personal judgment here. At the very least, this email will
trigger a TODO in my task list, so that it will not be forgotten. _At some
point_ it will be taken care of.

Once I am ready to update the package, I `ssh` to my Alpine Linux server. There
is absolutely no requirement to update alpine linux packages from alpine linux,
but it's the most convenient to do, and I already have an alpine linux system
anyway.

Then `cd aports/`. This is a local git clone of the [aports
tree](https://gitlab.alpinelinux.org/alpine/aports)
([wiki](https://wiki.alpinelinux.org/wiki/Aports_tree)).

`git pull`. I tend to clean up after myself, so the last branch is likely
already `master`. But, if not, then `git reset --hard && git checkout master &&
git pull`. Amen.

Now the real fun starts. And it's surprisingly quick and simple, it feels like
cheating:

```shell
% abump argocd-2.14.9
```

This will update the version and checksums in the corresponding `APKBUILD` and
trigger a package build.

It's sensible to check the package release notes or changelog to find potential
incompatibilities and/or updates to the build process. It's also sensible to
look at the package diffs to inspect for potential malware, which is becoming
increasingly more common these days in open source packages. "Secure your supply
chain", as they say it.

If the build completes successfully, create a new branch (`git nb argocd`),
commit, push it (`git pushm`), then create a merge request (MR) on
[GitLab](https://gitlab.alpinelinux.org/). I normally use the Web UI to do so,
but it's also possible to do it with the CLI. A link to create the MR is printed
to stdout upon pushing the branch, which makes the process even easier.

It could happen that the MR fails CI for some architectures (even if it works
locally on my machine™). These errors need to be dealt with.

The commit message must follow a certain style. I have a pre-commit script set
up that does it for me. It is typically in this form:

```
testing/argocd: upgrade to 2.14.9
```

There's a rule: only one package per merge request.

If there are more packages to upgrade, I run `git bd` ("branch delete") and then
restart this process. It's quite manageable, as I don't maintain a lot of
packages. Perhaps it could be further automated if there were more packages
and/or if the package upgrades were more frequent.

The final MR looks like the following:
[!83026](https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/83026).

Now I sit tight and wait for approval.


[^1]: On a [_best-effort_](https://xkcd.com/2347/) basis.

[^2]: Unless it's a security risk or incident (e.g. whenever there's a CVE
    associated with it).
