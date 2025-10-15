---
title: "Alpine Linux: usr-merge"
date: 2025-10-15T11:16:36+02:00
tags:
  - dev
---

[Alpine Linux](https://alpinelinux.org/posts/2025-10-01-usr-merge.html):

> The Alpine Linux Technical Steering Committee (TSC) has decided to change the
> base filesystem hierarchy. In the future, /lib, /bin, and /sbin will be
> symbolic links to their /usr counterparts, and every package shall be
> installed under the /usr paths. For now, /usr/bin and /usr/sbin will continue
> to be independent paths, but that might change if the Filesystem Hierarchy
> Standard (FHS) gets updated.

Just like Arch Linux has been doing [for
ages](https://www.archlinux.org/news/binaries-move-to-usrbin-requiring-update-intervention/)
(2013).

Fedora also did [a similar
move](https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin) this year.

I've been running Alpine Linux since 3.15 (2021), its current version is 3.22.
The migration process has been quite straightforward.

```shell
% doas apk upgrade -aU     # perform a full system upgrade
% doas apk add merge-usr   # install the migration script
% doas merge-usr --dryrun  # exec the migration script in dry-run mode
```

If the dry-run succeeds:

```shell
% doas merge-usr           # exec the migration script
$ doas apk del merge-usr   # clean up
```

Fin.
