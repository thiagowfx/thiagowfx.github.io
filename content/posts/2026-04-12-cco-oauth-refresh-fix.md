---
title: "cco: OAuth refresh fix"
date: 2026-04-12T07:35:32+02:00
tags:
  - ai
  - dev
  - security
---

[Previously]({{< ref "2026-03-18-cco-additional-directories" >}}).

**Problem statement**: `cco` is not able to autonomously refresh the OAuth token
used by `claude`.

The manual workaround is to run an one-off unsandboxed `claude`, and then get
back to `cco` afterwards.

Why?

Run `/doctor` within `cco` and compare its output with `/doctor` within an
unsandbox claude code session. The culprit:

```
Warning: macOS Keychain is not writable (security: SecKeychainItemCreateFromContent (<default>): UNIX[Operation not permitted];
  add-generic-password: returned 100001). Console login will fail to save your API key.
  Fix: Run: security unlock-keychain ~/Library/Keychains/login.keychain-db — if that doesn't fix it, your login keychain password may
  be out of sync with your account password: open Keychain Access, select the 'login' keychain, then Edit → Change Password for
  Keychain 'login'.
```

So now I am passing `--add-dir ~/Library/Keychains` to `cco`, and the warning is
finally gone!

```diff
commit 5c111a7caffb4e6b3dc4d678d4fc1bd6c8296ae5
Author: Thiago Perrotta <{redacted}>
Date:   Sun Apr 12 07:34:53 2026 +0200

    cco: add key chain dir, via /doctor

diff --git profile/.profile.d/alias.sh profile/.profile.d/alias.sh
index 0f5018c..80d7b60 100644
--- profile/.profile.d/alias.sh
+++ profile/.profile.d/alias.sh
@@ -51,7 +51,7 @@ fi

 if command -v claude >/dev/null 2>&1; then
 	if command -v cco >/dev/null 2>&1; then
-		alias claudey="cco --allow-oauth-refresh --add-dir ~/.cache --add-dir ~/.aws/cli/cache --add-dir ~/.aws/sso/cache --add-dir ~/.azure --add-dir ~/.terraform.d/plugin-cache --add-dir ~/go"
+		alias claudey="cco --allow-oauth-refresh --add-dir ~/.cache --add-dir ~/.aws/cli/cache --add-dir ~/.aws/sso/cache --add-dir ~/.azure --add-dir ~/.terraform.d/plugin-cache --add-dir ~/go --add-dir ~/Library/Keychains"
 	fi
 	alias claudeyy="claude --allow-dangerously-skip-permissions"
 fi
```
