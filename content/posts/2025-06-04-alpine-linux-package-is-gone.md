---
title: "Alpine Linux: package is gone?!"
date: 2025-06-04T11:43:05+02:00
tags:
  - dev
  - linux
---

Upon upgrading one of our Dockerfiles from Alpine Linux 3.21 to 3.22, we noticed
that the `ruby-json` package no longer exists:

```shell
% docker build -t myproject -f Dockerfile .
[...]
 > [ 2/10] RUN apk add --update --no-cache ruby-json=~"3.4" [...]
[...]
2.371 ERROR: unable to select packages:
2.371   ruby-json (no such package):
2.371     required by: world[ruby-json~3.4]
```

Why??

First, look into [Alpine Linux Packages](https://pkgs.alpinelinux.org/packages):
[query](https://pkgs.alpinelinux.org/packages?name=ruby-json&branch=v3.22&repo=&arch=&origin=&flagged=&maintainer=).
Ensure to set branch to v3.22 and architecture to All. And it's indeed not
there anymore:

> No matching packages found...

Next, do a bit of digging in the
[aports](https://gitlab.alpinelinux.org/alpine/aports) repository on the [Alpine
Linux GitLab](https://gitlab.alpinelinux.org/):
[query](https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/?sort=created_date&state=all&search=ruby-json&first_page_size=20).
Search for `ruby-json` in "All" Merge requests.

That leads to
[`!80599`](https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/80599):

> community/ruby-json: remove
>
> `ruby-json` is already bundled with `main/ruby`. The `community/ruby-json`
> could never be installed due to conflicts.

Aha, then there's nothing to do here. Installing the base `ruby` package should
be enough from now on.

[#16938](https://gitlab.alpinelinux.org/alpine/aports/-/issues/16938):

> I think it's safe to say community/ruby-json does literally nothing, has never been installed, and does not work.

Oh well.
