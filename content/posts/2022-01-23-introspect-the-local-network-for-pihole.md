---
title: "Introspect the local network for Pihole"
date: 2022-01-23T13:34:58-05:00
tags:
  - dev
---

Recently I needed to figure out what the IP address of my [pihole][pihole]
instance was in my [Raspberry Pi][raspberry-pi] in my local network.

## Finding the Raspberry Pi

### nmap

[`nmap`][nmap] to the rescue!

```shell
# nmap -sS 192.168.1.1-255 | tee network.txt | less
```

The relevant snippets to the pihole look like this:

```text
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

### ip

Another way is to use the `ip` command. In particular, `ip neigh` lists the
neighbours, one of which should be the pihole.

## Testing the pihole

One effective way to test the pihole is to see if `analytics.google.com` is
blocked. There are several ways to do so:

1. `ping` should return a local address like `127.0.0.1` or `0.0.0.0`.

```shell
$ ping analytics.google.com
PING analytics.google.com (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.023 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.031 ms
^C
--- analytics.google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 0.023/0.027/0.031/0.004 ms
```

2. Ditto for a DNS lookup utility such as `dig`:

```shell
$ dig +short analytics.google.com
0.0.0.0
```

Other ways: `drill`, `host`, `nslookup`, `systemd-resolve`.

https://d3ward.github.io/toolz/adblock.html seems to be a reasonable website to
test whether your adblock blocklists are properly working. Alternatively, just
visit any modern and large news corporation website, it will probably be full
of ads.

## Troubleshooting the pihole

If DNS resolution fails from the pihole itself, run `pihole restartdns`. Then
`ping google.com`. The ping should work, if it doesn't then there's a bigger
problem, out of scope of this post. If the ping works now but stops working
later on once you eventually reboot the Pi, consider triggering this command at
startup via `cron` or a systemd timer.

If DNS resolution works from the pihole but fails from a neighbouring device,
double-check if the device is properly configured: its DNS should be set to the
IP address of the pihole. Check these:

- `/etc/resolv.conf`
- If the system uses `systemd-resolved`, run `resolvectl`.

Another possibility is that the pihole might be configured to only answer
queries from `eth0`. Use the http://pi.hole/admin interface to ensure the
pihole is configured to answer DNS queries from the local network.

## Setting a static IP in the pihole

There are several ways to do so, in order of recommendation:

- Static DHCP lease from your router. If running a modem, this will likely not
  work. Prefer running a DHCP server from the pihole.

- `dhcpcd`: This is typically done as part of the standard pihole setup.

```shell
$ cat /etc/dhcpcd.conf
...
# fallback to static profile on eth0
#interface eth0
#fallback static_eth0
interface eth0
        static ip_address=192.168.1.XX/24
        static routers=192.168.1.1
        static domain_name_servers=
```

Note: Restart `dhcpcd` to apply: `systemctl restart dhcpcd`.

- `/etc/network/interfaces` if running Raspberry Pi OS (debian):

```shell
$ sudoedit /etc/network/interfaces.d/pihole
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
    address 192.168.1.XX
    netmask 255.255.255.0
    gateway 192.168.1.1
```

Note: Reconfigure debian networking to apply: `systemctl restart networking`.

- Static DHCP lease from the pihole itself if it's running a DHCP server. This
  solution is a bit redundant and should only be applied as last resort.

[nmap]: https://nmap.org/
[pihole]: https://pi-hole.net/
[raspberry-pi]: https://www.raspberrypi.org/
