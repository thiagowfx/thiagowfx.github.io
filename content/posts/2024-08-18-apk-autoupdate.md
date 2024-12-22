---
title: "apk autoupdate on alpine linux"
date: 2024-08-18T17:32:48+02:00
tags:
  - dev
  - linux
---

**Problem statement**: Upon running `doas apk upgrade` on Alpine Linux, select
packages with binaries backed by system services should be automatically
restarted.


Deb-based systems have
[`checkrestart(8)`](https://manpages.debian.org/bookworm/debian-goodies/checkrestart.8.en.html).

On Alpine, the best available approach as of today is https://github.com/jirutka/apk-autoupdate/:

```shell
doas apk add apk-autoupdate
$EDITOR /etc/apk/autoupdate.conf
```

Then make the two following changes[^1]:

```
# Because the default is '*', which will prevent all services from restarting.
services_blacklist=""

# List of services that should be restarted upon package upgrades.
services_whitelist="miniflux tailscale"
```

From this point on, whenever there are system upgrades for the aforementioned
services (`doas apk upgrade`), they will be automatically restarted. There's no
need for `doas /etc/init.d/miniflux restart`.

[^1]: h/t to @fossdd for replying to my
    https://github.com/jirutka/apk-autoupdate/issues/8 thread.
