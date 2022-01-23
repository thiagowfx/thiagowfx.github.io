---
title: "Scan local network with nmap"
date: 2022-01-23T13:34:58-05:00
tags:
  - linux
---

Recently I needed to figure out what the IP address of my [pihole][pihole]
instance was in my local network.

<!--more-->

[`nmap`][nmap] to the rescue!

```shell
# nmap -sS 192.168.1.1-255 | tee network.txt | less
```

The relevant snippets to the pihole look like this:

```none
Nmap scan report for pi.hole (192.168.1.XX)
Host is up (0.0052s latency).
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
53/tcp open  domain
80/tcp open  http
MAC Address: AA:AA:AA:AA:AA:AA (Raspberry Pi Foundation)

Nmap scan report for pi.hole (192.168.1.YY)
Host is up (0.0059s latency).
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
53/tcp open  domain
80/tcp open  http
MAC Address: BB:BB:BB:BB:BB:BB (Raspberry Pi Foundation)
```

There are two IP addresses, one for the ethernet interface (`eth0`) and the
other for the wifi (`wlan0`). Later on I would disable the wifi interface.

The 3 open ports are for services you would expect in a pihole:

- `ssh` (port 22) for remote access / debugging / troubleshooting
- DNS server (port 53) for the `dnsmasq` server that pihole uses underneath for adblocking
- HTTP server (port 80) for the http://pi.hole/admin web management UI

[nmap]: https://nmap.org/
[pihole]: https://pi-hole.net/
