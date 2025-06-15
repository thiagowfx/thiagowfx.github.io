---
title: "Debian: Enable unattended upgrades"
date: 2022-01-16T02:07:00-05:00
tags:
  - dev
  - linux
  - selfhosted
---

Here's how we can enable automatic (unattended) package upgrades in Debian.


## Howto

Install the `unattended-upgrades` package with `apt(8)`:

```shell
% apt install unattended-upgrades
```

The service is then enabled and started automatically:

```shell
$ systemctl status unattended-upgrades
● unattended-upgrades.service - Unattended Upgrades Shutdown
     Loaded: loaded (/lib/systemd/system/unattended-upgrades.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2022-01-16 02:05:42 EST; 35s ago
       Docs: man:unattended-upgrade(8)
   Main PID: 22442 (unattended-upgr)
      Tasks: 2 (limit: 1597)
        CPU: 516ms
     CGroup: /system.slice/unattended-upgrades.serviceGk
             └─22442 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
```

By default, only security updates are enabled. We can enable all updates by uncommenting the applicable lines:

```shell
$ sudoedit /etc/apt/apt.conf.d/50unattended-upgrades
...
Unattended-Upgrade::Origins-Pattern {
        // Codename based matching:
        // This will follow the migration of a release through different
        // archives (e.g. from testing to stable and later oldstable).
        // Software will be the latest available for the named release,
        // but the Debian release itself will not be automatically upgraded.
        // "origin=Debian,codename=${distro_codename}-updates";
        // "origin=Debian,codename=${distro_codename}-proposed-updates";
        // "origin=Debian,codename=${distro_codename},label=Debian";
        "origin=Debian,codename=${distro_codename},label=Debian-Security";
        "origin=Debian,codename=${distro_codename}-security,label=Debian-Security";
...
```

For debugging, one should run:

```shell
$ sudo unattended-upgrade -d
```

We could go beyond and add logging by the means of `etckeeper`, just like how we did for Alpine Linux's [`apk`]({{< ref "2022-01-10-alpine-linux-apk-logs-with-etckeeper" >}})

```shell
% apt install etckeeper
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  etckeeper
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 54.4 kB of archives.
After this operation, 180 kB of additional disk space will be used.
Get:1 http://raspbian.freemirror.org/raspbian bullseye/main armhf etckeeper all 1.18.16-1 [54.4 kB]
Fetched 54.4 kB in 1s (84.3 kB/s)
Preconfiguring packages ...
Selecting previously unselected package etckeeper.
(Reading database ... 44403 files and directories currently installed.)
Preparing to unpack .../etckeeper_1.18.16-1_all.deb ...
Unpacking etckeeper (1.18.16-1) ...
Setting up etckeeper (1.18.16-1) ...
Created symlink /etc/systemd/system/multi-user.target.wants/etckeeper.timer → /lib/systemd/system/etckeeper.timer.
etckeeper.service is a disabled or a static unit, not starting it.
...
```

`etckeeper` is enabled and works out-of-the-box as well:

```
systemctl status etckeeper.timer
● etckeeper.timer - Daily autocommit of changes in /etc directory
     Loaded: loaded (/lib/systemd/system/etckeeper.timer; enabled; vendor preset: enabled)
     Active: active (waiting) since Sun 2022-01-16 02:28:44 EST; 2min 36s ago
    Trigger: Mon 2022-01-17 02:28:44 EST; 23h left
   Triggers: ● etckeeper.service
       Docs: man:etckeeper(8)
```

Here's what a typical log looks like:

```shell
$ (cd /etc/etckeeper && sudo git log)
commit 8f9f5e31d9abb833cf645825c1cbda15336818b7 (HEAD -> master)
Author: root <root@raspberry>
Date:   Sun Jan 16 06:25:28 2022 -0500

    daily autocommit

commit 5a6478711a1a1198535d5062ca309afb5c99c0eb
Author: root <root@raspberry>
Date:   Sun Jan 16 02:29:01 2022 -0500

    Initial commit
```

## References

- https://wiki.debian.org/UnattendedUpgrades
