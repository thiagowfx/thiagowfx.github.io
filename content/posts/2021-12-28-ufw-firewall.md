---
title: 'Ufw: Firewall'
date: 2021-12-28T17:14:55-05:00
tags:
  - linux
  - selfhosted
---

> Ufw stands for Uncomplicated Firewall, and is a program for managing a netfilter firewall. It provides a command line interface and aims to be uncomplicated and easy to use.


The firewall makes justice to its name as it is really uncomplicated, and a pleasure to set up.

## Install

Install and set up `ufw`[^1], which should be packaged for most linux
distributions:

### OpenRC-based (Alpine Linux, Gentoo)

```shell
# Install ufw and ufw-extras
$ doas apk install ufw{,-extras}

# Enable ufw daemon
$ doas rc-update add ufw

# Start ufw daemon
$ doas rc-service ufw start

# Enable firewall
$ doas ufw enable
```

### Systemd-based (Arch Linux, Debian)

```shell
# Install ufw and ufw-extras
$ sudo pacman -Syu ufw{,-extras}

# Enable and start ufw daemon
$ sudo systemctl enable --now ufw

# Enable firewall
$ sudo ufw enable
```

## Add rules

Firewall rules can be added with `ufw allow [port]` or `ufw allow [name]`.
Named profiles (for example: ssh, http) live in `/etc/ufw/applications.d/`, or you can query all of them with `ufw app list`.

```shell
% ufw app list
Available applications:
  AIM
  Bonjour
  CIFS
  DNS
  Deluge
  IMAP
  IMAPS
  IPP
  KTorrent
  Kerberos Admin
  Kerberos Full
  Kerberos KDC
  Kerberos Password
  LDAP
  LDAPS
  LPD
  MSN
  MSN SSL
  Mail submission
  NFS
  POP3
  POP3S
  PeopleNearby
  SMTP
  SSH
  Socks
  Telnet
  Transmission
  Transparent Proxy
  VNC
  WWW
  WWW Cache
  WWW Full
  WWW Secure
  XMPP
  Yahoo
  qBittorrent
  svnserve
```

Ufw also supports `ufw limit [port | name]` which is like `add` but with the
added ability to "deny connections from IP addresses that attempt to initiate
6 or more connections in the last 30 seconds". It's a good measure to mitigate brute-force and/or DDOS attacks.

```shell
# either use named profiles
% ufw allow http-alt
% ufw limit ssh

# or port numbers
% ufw allow 8080/tcp
% ufw limit 22
```

## Remove rules

Firewall rules can be removed by merely adding 'delete' between ufw and the verb.

```shell
% ufw delete allow 8080/tcp
% ufw delete limit ssh
```

## Check status

One status command to rule them all, "verbose" is optional:

```shell
% ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     LIMIT IN    Anywhere
8080                       ALLOW IN    Anywhere
22/tcp (v6)                LIMIT IN    Anywhere (v6)
8080 (v6)                  ALLOW IN    Anywhere (v6)
```

Ufw uses iptables under the hood. Inspect the underlying iptables rules:

```shell
% iptables -S | egrep '\b(22|8080)\b'
-A ufw-user-input -p tcp -m tcp --dport 22 -m conntrack --ctstate NEW -m recent --set --name DEFAULT --mask 255.255.255.255 --rsource
-A ufw-user-input -p tcp -m tcp --dport 22 -m conntrack --ctstate NEW -m recent --update --seconds 30 --hitcount 6 --name DEFAULT --mask 255.255.255.255 --rsource -j ufw-user-limit
-A ufw-user-input -p tcp -m tcp --dport 22 -j ufw-user-limit-accept
-A ufw-user-input -p tcp -m tcp --dport 8080 -j ACCEPT
```

## References

- https://help.ubuntu.com/community/UFW
- https://wiki.archlinux.org/title/Uncomplicated_Firewall


[^1]: [`ufw-extras`](https://github.com/xyproto/ufw-extras) is optional, it contains additional rules (e.g. mosh, tailscale).