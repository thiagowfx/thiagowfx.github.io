---
title: "pi: update pinned npm packages"
date: 2026-07-27T14:28:59+02:00
tags:
  - ai
  - coding
  - dev
  - security
---

**Problem statement**: pin [pi](https://pi.dev/) npm packages without giving up
convenient updates.

My
[`settings.json`](https://github.com/thiagowfx/.dotfiles/blob/master/pi/.pi/agent/settings.json)
used to leave some package versions unpinned, until now:

```diff
     "npm:@heyhuynhgiabuu/pi-diff@0.7.6",
-    "npm:@tifan/pi-recap",
-    "npm:@tmustier/pi-tab-status",
-    "npm:@tintinweb/pi-subagents"
+    "npm:@tifan/pi-recap@0.4.4",
+    "npm:@tmustier/pi-tab-status@0.1.4",
+    "npm:@tintinweb/pi-subagents@0.14.3"
```

Exact versions make package installation reproducible (& safer), but Pi then
does not automatically pull newer packages.

To tackle that, I added a `just update-pi` recipe that asks npm for each
package's current `latest` version and writes back an exact pin:

```just
[doc('Update pinned Pi npm packages')]
[group('update')]
update-pi:
    #!/usr/bin/env bash
    set -euo pipefail

    settings="pi/.pi/agent/settings.json"
    updates="{}"
    while IFS= read -r spec; do
        if [[ "$spec" =~ ^npm:((@[^/]+/[^@]+)|([^@]+))(@[^@]+)?$ ]]; then
            package="${BASH_REMATCH[1]}"
        else
            echo "Invalid npm package spec: $spec" >&2
            exit 1
        fi

        latest="$(npm view "$package@latest" version)"
        pinned="npm:$package@$latest"
        updates="$(jq -cn \
            --argjson updates "$updates" \
            --arg spec "$spec" \
            --arg pinned "$pinned" \
            '$updates + {($spec): $pinned}')"
        echo "✓ $pinned"
    done < <(jq -r '.packages[] | select(type == "string" and startswith("npm:"))' "$settings")

    updated_settings="$(jq --argjson updates "$updates" \
        '.packages |= map($updates[.] // .)' "$settings")"
    printf '%s\n' "$updated_settings" > "$settings"
```

It handles every `npm:` entry, including scoped packages:

```shell
% just update-pi
✓ npm:@heyhuynhgiabuu/pi-diff@0.7.6
✓ npm:@heyhuynhgiabuu/pi-pretty@0.6.20
✓ npm:@tifan/pi-recap@0.4.4
✓ npm:@tmustier/pi-tab-status@0.1.4
✓ npm:@tintinweb/pi-subagents@0.14.3
```

The aggregate `just update` recipe invokes it alongside submodule, prek hook,
and vendored-file updates.

- - -

🤖 *Drafted with `/bloggify`.*
