---
title: "Alpine Linux: How to install all manpages (idiomatically)"
date: 2024-07-20T16:19:53+02:00
tags:
  - dev
  - linux
---

This post is a reply to
https://tilde.town/~kzimmermann/articles/installing_alpine_manpages.html.

The author describes their experience while attempting to install all man pages
for all the packages in use in their system.

The breakdown progression has some valuable insights on how a typical Unix
sysadmin addresses a problem. I tend to adopt a similar approach when entering
unknown territory.

However, in Alpine Linux, there is a better way.


## Solution

There is a `docs` metapackage:

```shell
% apk info docs
docs-0.2-r6 description:
Meta package for pulling in all documentation

docs-0.2-r6 webpage:
https://alpinelinux.org

docs-0.2-r6 installed size:
4096 B
```

All you have to do is:

```shell
% doas apk add docs
(1/125) Installing mandoc-doc (1.14.6-r13)
(2/125) Installing docs (0.2-r6)
(3/125) Installing libseccomp-doc (2.5.5-r1)
(4/125) Installing busybox-doc (1.36.1-r31)
[...]
```

Likewise, it is trivial to get rid of all man pages:

```shell
% doas apk del docs
```

I would like to give a few other suggestions to the author, if we were to assume
there is no `docs` metapackage:

- **Step 2**: You could also `cat /etc/apk/world`
  ([reference](https://serverfault.com/questions/1032488/alpine-linux-apk-list-out-directly-installed-packages-by-apk-add)).

- **Step 4**: `combine` from [moreutils]({{< ref
  "2022-05-01-tools-you-should-know-about-moreutils.md" >}}) is more
  user-friendly than `comm`. I need to look up how to use `comm` every single
  time, whereas `combine` is much easier to remember.

## Appendix

This was also a typical [xyproblem]({{< ref "2024-06-23-xyproblem" >}}) example:

- What is the attempt? "I want to install, via `apk add`, all `foo-doc` packages
  for every `foo` package on my system".

- What is the end goal? "I want to install all man pages for the installed
  packages on my system".


