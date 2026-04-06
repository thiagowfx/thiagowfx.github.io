---
title: "flameshot: collating multiple screenshots"
url: https://perrotta.dev/2026/02/flameshot-collating-multiple-screenshots/
last_updated: 2026-02-20
---


[Previously]({{< ref "2025-12-27-flameshot" >}}).

**Flameshot doesn't support collating multiple screenshots together.** This has
been [requested](https://github.com/flameshot-org/flameshot/issues/2763) (which
duplicates [#1130](https://github.com/flameshot-org/flameshot/issues/1130)), but
remains unimplemented.

The amazing ImageMagick (`convert`) comes to the rescue as always:

```shell
# vertical collage
convert screenshot1.png screenshot2.png -append combined.png

# horizontal collage
convert screenshot1.png screenshot2.png +append combined.png
```

