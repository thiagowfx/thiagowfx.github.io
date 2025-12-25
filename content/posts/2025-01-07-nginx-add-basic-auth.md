---
title: "nginx: add basic auth"
date: 2025-01-07T03:28:02-03:00
tags:
  - dev
---

**Problem statement**: You want to expose a HTTPS service from your cloud VPS to
the public Internet. You do not wish to use a VPN (e.g.
[tailscale](https://tailscale.com/)) to do so – which is a great way to address
this, but it's out of scope in this particular instance. How to proceed?

Here's a simple yet effective way: use / configure [nginx](https://nginx.org/)
as a reverse proxy.

Then add [HTTP basic
auth](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) to it:

```shell
% doas htpasswd -c /etc/nginx/.htpasswd myuser
```

The command will prompt for a password.

Once it's set, add two lines to the corresponding `server {}` block in your
nginx config:

```nginxconf
server {
[...]
    auth_basic "Restricted Access";
    auth_basic_user_file /etc/nginx/.htpasswd;
[...]
}
```

And finally: run `nginx -s reload`.

Now, whenever you navigate to that host, you'll be prompted to enter the basic
HTTP auth creds above.

The beauty of this approach is that it works for any HTTPS server, as it is
service agnostic.

The next level would be to integrate an SSO solution such as
[Authentik](https://goauthentik.io/), however it's quite more complex.
