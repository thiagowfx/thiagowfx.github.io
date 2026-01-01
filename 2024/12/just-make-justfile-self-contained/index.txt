
A commit is worth a thousand words, following up on my previous [just]({{< ref
"2024-12-13-just" >}}) post:

```diff
diff --git Justfile Justfile
old mode 100644
new mode 100755
index 1e1e33c7..cb0cd5e2
--- Justfile
+++ Justfile
@@ -1,10 +1,16 @@
+#!/usr/bin/env just --justfile
 # https://github.com/casey/just

 set dotenv-load

+_default:
+    @just --list
```

- Add a shebang to invoke your `Justfile`
- Make your `Justfile` executable (with `chmod +x`)
- Add a default target that invokes `just --list`. It should be the first one.
  The underscore makes it private, effectively hiding it from the list output.

The diff above is for the `Justfile` used for this blog. The above change
yields:

```shell
% ./Justfile
Available recipes:
    build                                           # Build the blog as in production
    clean                                           # Delete hugo build artifacts
    new post                                        # Create a new post. Usage: `just new "advent of code day 8"`
    ping sitemap="https://perrotta.dev/sitemap.xml" # Ping Google and Bing about changes in the sitemap
    update                                          # Update git submodules
    watch                                           # Start a hugo server in watch mode
```

Realistically though I'd rather invoke the `just` binary directly most of the
time.

