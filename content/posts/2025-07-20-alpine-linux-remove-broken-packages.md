---
title: "Alpine Linux: remove broken packages"
date: 2025-07-20T10:52:11+02:00
tags:
  - alpine-linux
  - dev
---

In a sunny Sunday morning:

```shell
% doas apk upgrade
WARNING: The indexes contain broken packages which might not function properly.
[...]
```

What?! Out of nowhere?

I tried a couple of basic troubleshooting commands:

```shell
% doas apk update --force-refresh
% doas apk fix
% doas apk cache clean
```

...to no avail.

Next idea: search engines. Virtually no results on [Kagi](https://kagi.com/). No
relevant results on Google either[^1].

Next idea: LLMs. Nothing useful either.

This is novel territory! That's what makes it fun to self-host Alpine Linux[^2].

My intuition tells me to start by searching their
[Gitlab](https://gitlab.alpinelinux.org/alpine). Eventually I got linked to
[this](https://sourcegraph.com/github.com/alpinelinux/apk-tools/-/blob/test/solver/error11.test?L3-5):

```
test/solver/error11.test:

@ARGS add invalid
@REPO error.repo
@EXPECT
WARNING: The indexes contain broken packages which are not installable.
ERROR: unable to select packages:
  invalid-1:
    error: uninstallable
    satisfies: world[invalid]
```

From this test file, it seems possible that there's an invalid package in my
`/etc/apk/world`. The error message is not quite the same, but it is similar:

```shell
% wc -l /etc/apk/world
293
```

There are too many packages there to hunt each of them by hand. And I didn't
install any new packages recently.

So I looked into `apk fix --help` and discovered there is a `--verbose` flag. I
did not save its output, but there were five packages there:

```
- busybox-initscripts
- kmod-openrc
- libacl
- py3-pep517
- sensible-utils
```

I ran `doas apk del` to remove all of them. That was a sensible cleanup, but it
still has not resolved the issue.

If I want to dive deeper into this, I'll have to add some debugging logging to
[`src/database.c`](https://sourcegraph.com/github.com/alpinelinux/apk-tools@bffc60041447cadee5b69c291df8c90eb3b8fe82/-/blob/src/database.c?L2090)
in `apk-tools`:

```c
if (db->compat_depversions) {
    apk_warn(out,
        "The indexes contain broken packages which %s.",
        db->compat_notinstallable ? "are not installable" : "might not function properly");
}
```

Then one last thought occurred to me:

```shell
% apk --version
apk-tools 3.0.0_rc5_git20250715-r0, compiled for x86_64.
```

Aha! I am running a release candidate version of `apk`, because I am using
Alpine Linux edge repositories:

```shell
% cat /etc/apk/repositories
http://dl-cdn.alpinelinux.org/alpine/edge/main
http://dl-cdn.alpinelinux.org/alpine/edge/community
http://dl-cdn.alpinelinux.org/alpine/edge/testing
```

From the
[Wiki](https://wiki.alpinelinux.org/wiki/Draft_Release_Notes_for_Alpine_3.23.0):

> After 5 years of development in the master branch of apk-tools, apk v3 is now
> ready for Alpine v3.23.0. This should be a safe and seamless upgrade from apk
> v2, but might has some breaking changes if you use libapk.

No wonder this is bleeding edge territory!

I would say that there's nothing to do here, other than waiting for the next
release of Alpine Linux (3.23) with apk-tools v3, and ignoring the warning in
the meantime.

[^1]: Their AI overview insists on spitting out useless information about
    Ubuntu, which is completely unrelated in this case.

[^2]: It is _fun_. Right? Right?!
