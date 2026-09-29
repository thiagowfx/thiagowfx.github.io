---
title: "pi: stop repeated macos keychain prompts for mcp oauth"
date: 2026-09-08T13:09:35+02:00
tags:
  - bloggify
  - dev
  - macos
  - pi
  - security
---

**Problem statement**: why did Pi keep asking for my macOS login keychain
password during MCP OAuth authentication?

`/mcp-auth grafana` opened the same prompt again after I entered the correct
password and selected **Allow**:

> pi wants to use your confidential information stored in
> "pi-mcp-adapter.oauth" in your keychain.

[`pi-mcp-adapter`](https://github.com/nicobailon/pi-mcp-adapter) stores OAuth
credentials in the operating system credential store. Its Grafana record name
is a SHA-256 hash:

```shell
% node -e 'const {createHash}=require("crypto"); console.log("sha256-" + createHash("sha256").update("grafana").digest("hex"))'
sha256-cace491b69555e8d0f77747d47ae54e31ce4cc322fe51a7bdcf64402f3676ebf
```

The Keychain ACL still allowed old Homebrew Node executables:

```shell
% security dump-keychain -a | rg -A18 'sha256-cace491b69555e8d0f77747d47ae54e31ce4cc322fe51a7bdcf64402f3676ebf"'
    entry 1:
        authorizations (6): decrypt derive export_clear export_wrapped mac sign
        don't-require-password
        description: pi-mcp-adapter.oauth
        applications (2):
            0: /opt/homebrew/Cellar/node/26.6.0/bin/node (status -67068)
                requirement: cdhash H"ea8d578543c9d8c21b74e26f7976cc30b60e24a5"
            1: /opt/homebrew/Cellar/node/26.5.0_1/bin/node (status -67068)
                requirement: cdhash H"4947cbedfdb054cda3708de8c0b22946c4fd98f1"
```

Pi now used Homebrew Node 26.8.1 with a different ad-hoc signature:

```shell
% codesign -dv --verbose=4 /opt/homebrew/Cellar/node/26.8.1/bin/node 2>&1 | rg 'Identifier|CDHash|TeamIdentifier'
Identifier=node-55554944b8d19d4157093cf1805ecde9a77d4850
CandidateCDHash sha256=cead962814af248488bb6597ee22a32fc23d00a1
CandidateCDHashFull sha256=cead962814af248488bb6597ee22a32fc23d00a1aac036bb431b750dd5120163
CDHash=cead962814af248488bb6597ee22a32fc23d00a1
TeamIdentifier=not set
```

The password was valid. macOS did not trust this new executable to read the
old item. Selecting **Allow** authorized one access, so the next read prompted
again.

I removed the base record and its two credential chunks, then authenticated
again:

```shell
% service=pi-mcp-adapter.oauth
% base=sha256-cace491b69555e8d0f77747d47ae54e31ce4cc322fe51a7bdcf64402f3676ebf
% security dump-keychain 2>/dev/null \
    | sed -n 's/^[[:space:]]*"acct"<blob>="\([^"]*\)"/\1/p' \
    | rg "^${base}(\.chunk\.[a-f0-9]{16}\.[0-9]+)?$" \
    | while read -r account; do
        security delete-generic-password -s "$service" -a "$account"
      done
password has been deleted.
password has been deleted.
password has been deleted.
```

A future Homebrew Node update would change its code hash again. The official
Node binary installed by Mise has a stable Developer ID requirement instead:

```shell
% codesign -dr - ~/.local/share/mise/installs/node/latest/bin/node 2>&1
designated => identifier node and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = HX7739G8FX
```

Installing Pi through that Node avoids tying Keychain access to one Homebrew
binary hash:

```shell
% npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```
