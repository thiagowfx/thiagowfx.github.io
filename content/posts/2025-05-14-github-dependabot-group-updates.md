---
title: "Github: dependabot: group updates"
date: 2025-05-14T15:08:40+02:00
tags:
  - dev
  - security
---

[dependabot](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide)
supports
[grouping](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#groups--)
commits into fewer, targeted pull requests.

A recent example in the repository of this blog:

```diff
% git show
commit 1fa93bed4d0faa9dfcdd6e554201d708baa38dbb (HEAD -> master, origin/master, origin/HEAD)
Author: Thiago Perrotta <{email redacted}>
Date:   Wed May 14 15:08:23 2025 +0200

    group dependabot updates

diff --git .github/dependabot.yml .github/dependabot.yml
index d6ca206c..3a5d1b09 100644
--- .github/dependabot.yml
+++ .github/dependabot.yml
@@ -4,7 +4,15 @@ updates:
     directory: /
     schedule:
       interval: monthly
+    groups:
+      all:
+        patterns:
+          - "*"
   - package-ecosystem: github-actions
     directory: /
     schedule:
       interval: monthly
+    groups:
+      all:
+        patterns:
+          - "*"
```

This is better for my workflow because then I will have less pull requests to
deal with at once, instead of having to review them one by one for each
individual github action or git submodule bump.
