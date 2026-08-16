---
title: "DNS: negative cache behind a local resolver"
date: 2026-07-31T14:02:20+02:00
tags:
  - bloggify
  - dev
  - macos
---

**Problem statement**: a newly created Route 53 record resolved through public DNS,
but ~~Chrome~~ Brave and macOS still returned `DNS_PROBE_POSSIBLE`.

It smells like a DNS caching issue.

Flushing `mDNSResponder` did nothing though.

The system resolver was **Tailscale**'s local DNS
proxy, so I asked that resolver rather than trusting `dig`'s default path:

```shell
% dig +time=3 +tries=1 @100.100.100.100 kargo.tools.example-corp.net A +noall +answer +authority +comments
; <<>> DiG 9.10.6 <<>> +time=3 +tries=1 @100.100.100.100 kargo.tools.example-corp.net A +noall +answer +authority +comments
; (1 server found)
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 13683
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; AUTHORITY SECTION:
tools.example-corp.net. 225 IN SOA ns-1609.awsdns-09.co.uk. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400
```

Route 53's authoritative nameserver and several public resolvers already had it:

```shell
% for resolver in 1.1.1.1 1.1.1.2 8.8.8.8; do
    printf '%-16s ' "$resolver"
    dig +time=2 +tries=1 +short @"$resolver" kargo.tools.example-corp.net A | paste -sd, -
  done
1.1.1.1          192.0.2.11,198.51.100.50,203.0.113.95
1.1.1.2          192.0.2.11,203.0.113.95,198.51.100.50
8.8.8.8          203.0.113.95,198.51.100.50,192.0.2.11

% dig +short @ns-1609.awsdns-09.co.uk kargo.tools.example-corp.net A
192.0.2.11
203.0.113.95
198.51.100.50
```

Tailscale had cached the previous `NXDOMAIN` response for a couple of minutes.
Its cache is not macOS's cache; restarting `mDNSResponder` cannot clear it.
Waiting out that TTL fixed the web browser lookup.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*
