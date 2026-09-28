---
title: "talisman: exempt git commit SHAs"
url: https://perrotta.dev/2026/09/talisman-exempt-git-commit-shas/
last_updated: 2026-09-28
---


**Problem statement**: make [Talisman](https://github.com/thoughtworks/talisman)
stop reporting full Git commit SHAs as hex-encoded secrets (false positives).

A typical false positive 'violation' looks like the following:

```shell
% printf '%s\n' '675adb16677f8d3615f499f43b6ba26e04cfffa4' > talisman-commit-sha-repro.txt
% git add talisman-commit-sha-repro.txt
% prek run talisman-commit --files talisman-commit-sha-repro.txt
talisman.................................................................Failed
- hook id: talisman-commit
- exit code: 1

Talisman Report:
+-------------------------------+------------------------------------------+----------+
|             FILE              |                  ERRORS                  | SEVERITY |
+-------------------------------+------------------------------------------+----------+
| talisman-commit-sha-repro.txt | Expected file to not contain             | high     |
|                               | hex encoded texts such as:               |          |
|                               | 675adb16677f8d3615f499f43b6ba26e04cfffa4 |          |
+-------------------------------+------------------------------------------+----------+
```

To stop it once and for all, add a global [allowed
pattern](https://thoughtworks.github.io/talisman/docs/configuring-talisman/ignoring/)
for full lowercase Git object IDs:

```diff
diff --git .talismanrc .talismanrc
index 68deb2d73c..2e4c8f7b95 100644
--- .talismanrc
+++ .talismanrc
@@ -1,14 +1,15 @@
 # yaml-language-server: $schema=schemas/talismanrc.json

 # Docs: https://thoughtworks.github.io/talisman/docs/configuring-talisman/ignoring/
 threshold: medium
 allowed_patterns:
   # keep-sorted start
+  - "\\b[0-9a-f]{40}\\b"
   - "https://gist\\.github\\.com/\\w+/\\w+"
   - "https://github\\.com/[\\w.-]+/[\\w.-]+/blob/[0-9a-f]{40}"
   - "https://github\\.com/[\\w.-]+/[\\w.-]+/commit/[0-9a-f]{40}"
   - "https://github\\.com/[\\w.-]+/[\\w.-]+/tree/[0-9a-f]{40}"
   - "rev: \\w+ # frozen:"
   # keep-sorted end

 fileignoreconfig:
```

Test it:

```shell
% prek run talisman-commit --files talisman-commit-sha-repro.txt
talisman.................................................................Passed
```

Talisman cannot prove that arbitrary hexadecimal text names a Git object. This
rule deliberately exempts every standalone, lowercase, 40-character hexadecimal
value.

