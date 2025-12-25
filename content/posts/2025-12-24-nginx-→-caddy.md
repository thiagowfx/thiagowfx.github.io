---
title: "nginx → caddy"
date: 2025-12-24T23:59:02-03:00
tags:
  - bestof
  - dev
---

**Problem statement**: Replace `nginx` with `caddy` for `miniflux` on my Alpine
Linux VPS host.

First, install `caddy`:

```shell
doas apk add caddy
```

Next, migrate the existing nginx config to caddy.

The stock config:

```shell
% cat /etc/caddy/Caddyfile
# Caddy's configuration file
# see: https://caddyserver.com/docs/caddyfile
```

The new config:

```caddyfile
# Caddy's configuration file
# see: https://caddyserver.com/docs/caddyfile
{miniflux_host}.perrotta.dev {
    reverse_proxy * {
        to 127.0.0.1:8080
        header_up Host {host}
        header_up X-Forwarded-For {remote}
        header_up X-Forwarded-Proto {scheme}
    }
}
```

Stop nginx:

```shell
doas service nginx stop
```

Start caddy:

```shell
% doas service caddy start
% doas service caddy status
 * status: started
```

Now I tried to access my server via a web browser, and it worked out-of-the-box
:)

I can see information about the SSL certificate in my web browser:

```
Issued On	Thursday, December 25, 2025 at 1:41:33 AM
Expires On	Wednesday, March 25, 2026 at 1:41:32 AM
```

It was issued just a few seconds ago!

How to view logs?

I expect to find them at `/var/log/caddy` but there's nothing there.

I need to add an explicit directive to enable logging:

```caddy
{miniflux_host}.perrotta.dev {
    log {
        output file /var/log/caddy/miniflux.log
    }
    reverse_proxy * {
        to 127.0.0.1:8080
        header_up Host {host}
        header_up X-Forwarded-For {remote}
        header_up X-Forwarded-Proto {scheme}
    }
}
```

Then reload caddy:

```shell
% doas service caddy reload
~ # service caddy reload
 * Reloading Caddy web server ...
2025/12/25 05:49:04.531	INFO	using config from file	{"file": "/etc/caddy/Caddyfile"}
2025/12/25 05:49:04.532	WARN	caddyfile	Unnecessary header_up X-Forwarded-For: the reverse proxy's default behavior is to pass headers to the upstream
2025/12/25 05:49:04.532	WARN	caddyfile	Unnecessary header_up X-Forwarded-Proto: the reverse proxy's default behavior is to pass headers to the upstream
2025/12/25 05:49:04.532	INFO	adapted config to JSON	{"adapter": "caddyfile"}
2025/12/25 05:49:04.533	WARN	Caddyfile input is not formatted; run 'caddy fmt --overwrite' to fix inconsistencies	{"adapter": "caddyfile", "file": "/etc/caddy/Caddyfile", "line": 4}
Error: sending configuration to instance: caddy responded with error: HTTP 400: {"error":"loading config: loading new config: setting up custom log 'log0': opening log writer using \u0026logging.FileWriter{Filename:\"/var/log/caddy/miniflux.log\", Mode:0x0, Roll:(*bool)(nil), RollSizeMB:0, RollCompress:(*bool)(nil), RollLocalTime:false, RollKeep:0, RollKeepDays:0}: open /var/log/caddy/miniflux.log: permission denied"}
```

Let's address these issues:

```shell
/etc/caddy % doas caddy fmt --overwrite
```

The formatting warning is gone:

```shell
% doas service caddy reload
 * Reloading Caddy web server ...
2025/12/25 05:53:06.079	INFO	using config from file	{"file": "/etc/caddy/Caddyfile"}
2025/12/25 05:53:06.079	WARN	caddyfile	Unnecessary header_up X-Forwarded-For: the reverse proxy's default behavior is to pass headers to the upstream
2025/12/25 05:53:06.079	WARN	caddyfile	Unnecessary header_up X-Forwarded-Proto: the reverse proxy's default behavior is to pass headers to the upstream
2025/12/25 05:53:06.080	INFO	adapted config to JSON	{"adapter": "caddyfile"}
Error: sending configuration to instance: caddy responded with error: HTTP 400: {"error":"loading config: loading new config: setting up custom log 'log0': opening log writer using \u0026logging.FileWriter{Filename:\"/var/log/caddy/miniflux.log\", Mode:0x0, Roll:(*bool)(nil), RollSizeMB:0, RollCompress:(*bool)(nil), RollLocalTime:false, RollKeep:0, RollKeepDays:0}: open /var/log/caddy/miniflux.log: permission denied"}
```

Next, logging:

```shell
% doas mkdir /var/log/caddy
% doas touch /var/log/caddy/miniflux.log
% doas chown -R caddy:caddy /var/log/caddy
```

Now it's much better:

```shell
% doas service caddy reload
 * Reloading Caddy web server ...
2025/12/25 05:56:11.041	INFO	using config from file	{"file": "/etc/caddy/Caddyfile"}
2025/12/25 05:56:11.041	WARN	caddyfile	Unnecessary header_up X-Forwarded-For: the reverse proxy's default behavior is to pass headers to the upstream
2025/12/25 05:56:11.041	WARN	caddyfile	Unnecessary header_up X-Forwarded-Proto: the reverse proxy's default behavior is to pass headers to the upstream
2025/12/25 05:56:11.042	INFO	adapted config to JSON	{"adapter": "caddyfile"}
```

Regarding the two "unnecessary" configs, just remove them from the `Caddyfile`:

```diff
-        header_up X-Forwarded-For {remote}
-        header_up X-Forwarded-Proto {scheme}
```

How did I know which user to `chown` to? `/etc/init.d/caddy` has the following
line:

```conf
command_user=caddy:caddy
```

...though it wouldn't have been difficult to guess it anyways.

I can see some logs at `/var/log/caddy/miniflux.log` already.

Use `tail -f` or `tspin -f` (from tailspin) for live log tailing.

LLM security analysis, for completeness:

```
I reviewed /etc/caddy/Caddyfile. Overall, it's a straightforward reverse proxy for {miniflux_host}.perrotta.dev to 127.0.0.1:8080 with logging to
 /var/log/caddy/miniflux.log. Caddy will automatically manage HTTPS and pass the appropriate headers upstream, and Caddy's defaults already
 set the Host and X-Forwarded-* headers—so explicitly setting them is optional but not harmful.

 Security considerations:
 - Ensure the local Miniflux instance is bound to loopback only (127.0.0.1) so it's not exposed directly.
 - Confirm /var/log/caddy/ and the log file are readable by the Caddy user but not world-readable if the logs might contain sensitive data.
 - If you ever place Caddy behind another proxy (e.g., Cloudflare), configure trusted_proxies in Caddy to ensure X-Forwarded-* is accurate.

 Beyond that, the config is minimal and doesn't expose extra surfaces.
```

Last step: let's make caddy auto start, and disable nginx startup + uninstall
it:

```shell
doas rc-update del nginx
doas rc-update add caddy
doas apk del nginx
```

Out of curiosity: the certificates live here:

```shell
/var/lib/caddy/.local/share/caddy/certificates/acme-v02.api.letsencrypt.org-directory/{miniflux_host}.perrotta.dev/
```

There are three files:

- crt and key: SSL / TLS
- json: configuration / metadata for let's encrypt

And we're done!
