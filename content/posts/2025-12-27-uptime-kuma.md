---
title: "UptimeKuma"
date: 2025-12-27T01:53:05-03:00
tags:
  - bestof
  - dev
  - meta
---

This site is now monitored via self-hosted [uptime infrastructure](https://uptime.perrotta.dev/status/serendipity).

How did I do it?

Software: [UptimeKuma](https://github.com/louislam/uptime-kuma). Open-source,
self-hosted, simple & easy, has a docker image for deployment, sensible
defaults, lots of customization possibilities. Modern, solid, well-maintained,
popular (80k+ stars on GitHub). A no-brainer choice, really.

I deployed it via Docker on Alpine Linux.

Install docker and docker-compose:

```shell
% doas apk add docker docker-compose
```

Update the docker storage driver from the `overlay2` default as it was failing
for some reason:

```shell
% doasedit /etc/docker/daemon.json
{
	  "storage-driver": "vfs"
}
```

Start docker, now and on startup:

```shell
% doas service docker start
% doas rc-update add docker
```

...equivalently to `systemctl enable --now docker`.

Create a `docker-compose.yml` file for the service:

```shell
% cat docker/docker-compose.yml
services:
  uptime-kuma:
    image: louislam/uptime-kuma:latest
    container_name: uptime-kuma
    restart: unless-stopped
    ports:
      - "127.0.0.1:3001:3001"
    volumes:
      - /opt/uptime-kuma:/app/data
```

...ensure to bind it to localhost only (`127.0.0.1`).

Start it:

```shell
% docker-compose up -d
```

`-d` to start it in the background.

From here we access the service and configure it (out of scope of this post):

- create an admin user, set a secure password
- enable 2FA (TOTP)
- add the first monitor (`https://perrotta.dev`)

To access the service securely for the first time, there are various
possibilities:

- expose it under a reverse proxy with HTTP basic auth
- employ a VPN (e.g. Tailscale, Wireguard)
- use SSH port forwarding from your VPS to your laptop

...just _do not_ expose the service to `0.0.0.0` without credentials.

Next, expose the service via a user-friendly URL, with the creation of a DNS
record. As you can see, I chose uptime.perrotta.dev.

Configure your reverse proxy ([Caddy]({{< ref "2025-12-24-nginx-caddy" >}}) in
this case):

```
uptime.perrotta.dev {
	log {
		output file /var/log/caddy/uptime.log
	}

	reverse_proxy * {
		to 127.0.0.1:3001
		header_up Host {host}
	}
}
```

Then:

```shell
% doas service caddy reload
```

And now sit back and enjoy free uptime monitoring!
