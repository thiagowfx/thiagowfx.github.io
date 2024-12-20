---
title: "Docker on Alpine Linux"
date: 2024-07-30T22:56:58+02:00
tags:
  - dev
---

In this post: how to properly start `docker` on an Alpine Linux server.

<!--more-->

First, install `docker` and friends:

```shell
doas apk add docker docker-cli docker-compose
```

Then start the `docker` service:

```shell
doas service docker start
```

Check if it started successfully:

```shell
service docker status
```

If not, then look at the logs:

```shell
less /var/log/docker.log
```

I got an error:

```
failed to start daemon: error initializing graphdriver: driver not supported
```

The suggestion was to change the driver to `overlay2`:

```shell
% $EDITOR /etc/docker/daemon.json
{
  "storage-driver": "overlay2"
}
```

Then restart `docker`.

I got another error:

```shell
level=error msg="failed to mount overlay: no such device" storage-driver=overlay2
```

The suggestion was to reboot:

```shell
doas reboot
```

Then start `docker` again:

```shell
doas service docker start
```

And now everything works!
