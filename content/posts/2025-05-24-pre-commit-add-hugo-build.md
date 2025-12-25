---
title: "pre-commit: add hugo build"
date: 2025-05-24T17:29:48+02:00
tags:
  - dev
---

Sometimes I make changes to this blog that yield build errors with its static
site generator ([hugo](https://gohugo.io/)).

It's trivial to spot these changes with a simple `hugo build`, but [I don't always
run it]({{< ref "2025-03-14-yolo-debug-only-after-push" >}}).

Here's what a typical error looks like:

```
% hugo build
Start building sites …
hugo v0.147.5+extended+withdeploy darwin/arm64 BuildDate=2025-05-22T11:37:19Z VendorInfo=brew

ERROR [en] REF_NOT_FOUND: Ref "nonexistent/2025-03-24-maccy-pin-items": "/Users/tperrotta/Workspace/perrotta.dev/content/posts/2025-05-16-espanso-hello-world.md:10:14": page not found
Total in 242 ms
Error: error building site: logged 1 error(s)
```

The same happens when invoking [`just`](https://just.systems/man/en/), as you
would expect:

```
% just build
hugo --environment production --gc --minify
Start building sites …
hugo v0.147.5+extended+withdeploy darwin/arm64 BuildDate=2025-05-22T11:37:19Z VendorInfo=brew

ERROR [en] REF_NOT_FOUND: Ref "nonexistent/2025-03-24-maccy-pin-items": "/Users/tperrotta/Workspace/perrotta.dev/content/posts/2025-05-16-espanso-hello-world.md:10:14": page not found
Total in 280 ms
Error: error building site: logged 1 error(s)
error: Recipe `build` failed on line 17 with exit code 1
```

**Problem statement**: catch such build errors at git pre-commit time.

This is trivial with a [pre-commit.com](https://pre-commit.com/) hook:

```diff
Author: Thiago Perrotta <{email redacted}>
Date:   Sat May 24 17:26:59 2025 +0200

    pre-commit: add just build

diff --git .pre-commit-config.yaml .pre-commit-config.yaml
index 60eb2022..623e135d 100644
--- .pre-commit-config.yaml
+++ .pre-commit-config.yaml
@@ -112,5 +112,10 @@ repos:
         language: pygrep
         types:
           - markdown
+      - id: hugo
+        name: Hugo
+        language: system
+        entry: just build
+        pass_filenames: false
```

Here's the end result:

```shell
% git commit -m "test"
Check hooks apply to the repository.............................................(no files to check)Skipped
Check for useless excludes......................................................(no files to check)Skipped
[...]
Forbid usage of UTM analytics / tracking............................................................Passed
Hugo................................................................................................Failed
- hook id: hugo
- exit code: 1

hugo --environment production --gc --minify
Start building sites …
hugo v0.147.5+extended+withdeploy darwin/arm64 BuildDate=2025-05-22T11:37:19Z VendorInfo=brew

ERROR [en] REF_NOT_FOUND: Ref "a/2024-12-23-unbuffer": "/Users/tperrotta/Workspace/perrotta.dev/content/posts/2025-05-24-watch-with-color.md:54:54": page not found
Total in 276 ms
Error: error building site: logged 1 error(s)
error: Recipe `build` failed on line 19 with exit code 1
```
