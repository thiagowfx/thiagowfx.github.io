---
title: "chrome-fresh: start a fresh instance of Google Chrome"
date: 2024-03-10T21:55:16+01:00
tags:
  - dev
---

I used to have the following handy script to launch a new (fresh!) instance of
Google Chrome when working on [Chrome for Testing]({{< ref
"2024-01-25-chrome-for-testing.md" >}}) in the Browser Automation team at
Google:


```shell
#!/bin/bash
# start chrome with ephemeral settings (every run of Chrome is empty)
# usage: chrome-fresh out/Default/chrome

TMPDIR="$(mktemp -d)"
trap 'rm -rf "${TMPDIR}"' EXIT

CHROME="${1:-google-chrome}"; shift

# https://github.com/GoogleChrome/chrome-launcher/blob/main/docs/chrome-flags-for-tools.md
CHROME_FLAGS="--use-mock-keychain"

if [[ "$(uname -s)" == "Darwin" && "$CHROME" == *.app ]]; then
	open -n "$CHROME" --args "$CHROME_FLAGS" --user-data-dir="$TMPDIR" "$@"
else  # "Linux"
	"$CHROME" "$CHROME_FLAGS" --user-data-dir="$TMPDIR" "$@"
fi
```

The script is self-documenting, it was properly tested on both Linux and macOS.

The typical use case would be to compile a new Google Chrome binary
(`/out/Default/chrome`), and then use the script to launch it with a fresh user
data directory, to ensure the previous launch settings do not interfere with the
current one.
