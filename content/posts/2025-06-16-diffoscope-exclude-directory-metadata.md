---
title: "Diffoscope: exclude directory metadata"
date: 2025-06-16T11:58:02+02:00
tags:
  - dev
---

[Previously]({{< ref "2024-08-24-diffoscope-recursive-diffs" >}}),
[previously]({{< ref "2024-08-24-diffoscope-recursive-diffs" >}}).

If you simply run `diffoscope dir1/ dir2/`, a lot of noise could be added to the
output due to metadata such as timestamps:

```
│   --- dir1/foo.yaml
│ ├── +++ dir2/foo.yaml
│ │ ├── stat {}
│ │ │ @@ -1,8 +1,8 @@
│ │ │
│ │ │    Size: 314              Blocks: 8          IO Block: 4096   regular file
│ │ │  Device: 1,17     Links: 1
│ │ │  Access: (0644/-rw-r--r--)  Uid: (  501/thiago.perrotta)   Gid: (   20/   staff)
│ │ │
│ │ │ +Modify: 2025-06-16 09:53:55.107373563 +0000
│ │ │ -Modify: 2025-04-04 14:37:59.032398559 +0000
│ │   --- dir1/bar.yaml
│ ├── +++ dir2/bar.yaml
│ │ ├── stat {}
│ │ │ @@ -1,8 +1,8 @@
│ │ │
│ │ │    Size: 444              Blocks: 8          IO Block: 4096   regular file
│ │ │  Device: 1,17     Links: 1
│ │ │  Access: (0644/-rw-r--r--)  Uid: (  501/thiago.perrotta)   Gid: (   20/   staff)
│ │ │
│ │ │ +Modify: 2025-06-16 09:53:55.107527976 +0000
│ │ │ -Modify: 2025-03-05 13:37:47.461442994 +0000
```

These timestamps are relevant in the context of [reproducible
builds](https://reproducible-builds.org/), however we don't particularly care
about them when we're merely interested in diffing directory and file contents.

Thankfully, `diffoscope` has a flag to ignore these:

```shell
diffoscope dir1/ dir2/ --exclude-directory-metadata=yes
```
