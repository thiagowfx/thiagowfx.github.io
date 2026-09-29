---
title: "kargo: quote numeric-looking image tags"
url: https://perrotta.dev/2026/09/kargo-quote-numeric-looking-image-tags/
last_updated: 2026-09-29
---


[Previously]({{< ref "2026-08-21-kargo-notify-when-a-soak-completes" >}}).

**Problem statement**: a Kargo promotion turned a valid all-digit Git SHA into
scientific notation.

The Freight contained an image tag and a Helm chart version:

```text
15abd266dc635e7b9f3fe740441a73cd3cd549e7  937844257  0.5.1
```

`937844257` looked like a build number. It was the first nine characters of a
real commit:

```shell
% git rev-parse 937844257
9378442576c62b45cba4b41d8b4eb09a763da1ad
```

The Stage passed the tag directly to [`yaml-update`](https://docs.kargo.io/user-guide/reference-docs/promotion-steps/yaml-update):

```yaml
- uses: yaml-update
  config:
    path: ./gitrepo/apps/overlays/g02/sessions/patches.yaml
    updates:
      - key: 1.value.image.tag
        value: ${{ imageFrom(vars.imageRepo).Tag }}
```

Kargo [coerces expression results](https://docs.kargo.io/user-guide/reference-docs/expressions/#types)
that look like JSON numbers. The promotion log showed the result:

```text
Updated ./gitrepo/apps/overlays/g02/sessions/patches.yaml

- 1.value.image.tag: 9.37844257e+08
- 3.value: ~0.5.0
```

The generated Git diff therefore pointed at an image tag that did not exist:

```diff
 image:
-  tag: cd3a31000
+  tag: 9.37844257e+08
```

Kargo provides `quote()` for exactly this case:

```diff
-        value: ${{ imageFrom(vars.imageRepo).Tag }}
+        value: ${{ quote(imageFrom(vars.imageRepo).Tag) }}
```

I changed all image-tag writes across the eight rollout Stages and checked
the same condition before and after:

```text
before fix: 20 unsafe image-tag updates
after fix: 0 unsafe image-tag updates
```

```shell
% prek run kargo-promotion-tasks --all-files
Check Kargo PromotionTask references.....................................Passed
```

An [older Kargo bug report](https://github.com/akuity/kargo/issues/876) even
used an all-digit short SHA as its example. Git hashes contain hexadecimal
characters, but none of those characters has to be a letter.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*

