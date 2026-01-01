
Added a new [just](https://just.systems/)
[recipe](https://just.systems/man/en/the-default-recipe.html) to open the latest
(=most recent) blog post in `$EDITOR`. Very handy to make quick edits!

```
% GIT_PAGER=cat git show HEAD
commit 9fac587c257da57a9abb37e4ea1d7b2502ba51d2 (HEAD -> master, origin/master, origin/HEAD)
Author: Thiago Perrotta <{redacted}>
Date:   Fri Nov 21 14:07:35 2025 -0300

    just: add last

diff --git Justfile Justfile
index a6ba3d0b9..ba6268b98 100755
--- Justfile
+++ Justfile
@@ -51,6 +51,18 @@ code title *args:

 alias coding := code

+# Edit the most recent blog post
+last:
+    #!/usr/bin/env bash
+    set -euo pipefail
+
+    latest=$(ls -t content/posts/*.md 2>/dev/null | head -n 1 || true)
+    if [ -z "$latest" ]; then
+      echo "No posts found in content/posts/"
+      exit 1
+    fi
+    {{ editor }} "$latest"
+
 # Delete hugo build artifacts
 clean:
     rm -rf public/ resources/
```

[`ls -t`](https://man7.org/linux/man-pages/man1/ls.1.html) sorts by time, newest
first.

