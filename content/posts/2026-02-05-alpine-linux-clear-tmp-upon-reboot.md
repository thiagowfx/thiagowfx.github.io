---
title: "Alpine Linux: clear /tmp upon reboot"
date: 2026-02-05T18:02:12+01:00
tags:
  - alpine-linux
  - dev
---

[Clear /tmp at reboot on Alpine Linux](https://chromic.org/blog/alpinelinux-clear-tmp-on-reboot/) via Chimo:

> By default, Alpine Linux doesn't (completely) clear the /tmp directory on
> reboot (unless you mount it as tmpfs). If you would like to enable this
> feature, change "wipe_tmp" to "YES"
>
> [...]

My current config:

```
❯ cat /etc/conf.d/bootmisc

# List of /tmp directories we should clean up
clean_tmp_dirs="/tmp"

# Should we wipe the tmp paths completely or just selectively remove known
# locks / files / etc... ?
wipe_tmp="NO"

# Write the initial dmesg log into /var/log/dmesg after boot
# This may be useful if you need the kernel boot log afterwards
log_dmesg="YES"

# Save the previous dmesg log to dmesg.old
# This may be useful if you need to compare the current boot to the
# previous one.
#previous_dmesg=no

```

I find that to be a sensible change indeed:

```shell
% doasedit /etc/conf.d/bootmisc
# [...]
# update from NO:
# wipe_tmp="YES"
```

I left my config like this:

```shell
% cat /etc/conf.d/bootmisc
[...]
# Should we wipe the tmp paths completely or just selectively remove known
# locks / files / etc... ?
# wipe_tmp="NO"
wipe_tmp="YES"
[...]
```

I like to leave the previous / default value commented out, it is a good paper
trail[^1] for my future self.

[^1]: _tombstone_, in software engineering parlance
