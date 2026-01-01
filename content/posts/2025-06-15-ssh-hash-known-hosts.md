---
title: "SSH: hash known hosts"
date: 2025-06-15T12:05:11+02:00
tags:
  - dev
  - privacy
  - security
---

A security / privacy tip: hash ssh hosts, especially in machines you have
access to that are in the cloud.
[`~/.ssh/config`](https://github.com/thiagowfx/.dotfiles/blob/6a5bb6a20eeede82dfcbbc56ef4db91ffe2dd65d/ssh/.ssh/config#L40-L42):

```
Host *
	# Automatically hash new host keys added to ~/.ssh/known_hosts.
	# Manually for pre-existing hosts: ssh-keygen -H
	HashKnownHosts yes
```

The default is not to hash.

As a side effect, `~/.ssh/known_hosts` (sample entry):

```
|1|F1E1KeoE/eEWhi10WpGv4OdiO6Y=|3988QV0VE8wmZL7suNrYQLITLCg= sh-ed25519 [...]
```

Why do this? As per [Security Stack Exchange](https://security.stackexchange.com/questions/56268/ssh-benefits-of-using-hashed-known-hosts):

> The only change is that if a machine is compromised, the idea is to minimize
> how much usable information is given to an attacker.

To retroactively hash existing entries, run:

```shell
% ssh-keygen -H
/Users/tperrotta/.ssh/known_hosts updated.
Original contents retained as /Users/tperrotta/.ssh/known_hosts.old
```
