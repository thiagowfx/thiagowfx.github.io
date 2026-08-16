---
title: "microSD card: wiping before selling"
date: 2026-08-16T15:20:10+02:00
tags:
  - dev
  - macos
  - privacy
  - security
---

**Problem statement**: I want to sell a 32 GB microSD card, previously used to
boot a Raspberry Pi.

```shell
% diskutil list disk4
/dev/disk4 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *32.0 GB    disk4
   1:             Windows_FAT_32 BOOT                    268.4 MB   disk4s1
   2:                      Linux                         31.7 GB    disk4s2
```

For that, I would like to securely wipe it. `dd` is my preferred tool to do so.

```shell
% diskutil unmountDisk /dev/disk4
Unmount of all volumes on disk4 was successful
% sudo dd if=/dev/zero of=/dev/rdisk4 bs=4m
dd: invalid number: '4m'
```

That is GNU `dd` from coreutils (installed via homebrew) shadowing the BSD one
in `PATH`. BSD `dd` takes `bs=4m`, GNU `dd` takes `4M`. It's hard to standardize
and agree upon something so simple, eh?

`/dev/rdisk4` rather than `/dev/disk4` because the raw node skips the buffer
cache and thus it is several times faster:

```shell
% sudo dd if=/dev/zero of=/dev/rdisk4 bs=4M status=progress
dd: error writing '/dev/rdisk4': Input/output error
7633+0 records in
7632+0 records out
32010928128 bytes (32 GB, 30 GiB) copied, 3550.08 s, 9.0 MB/s
```

The `Input/output error` is the happy ending: `dd` ran off the end of the
device. 32010928128 bytes is precisely what `diskutil info` reported for the
disk size, so every addressable byte got a zero.

The process took ~59min at ~9.0 MB/s.

Then we'll partition it again so that the buyer's camera or laptop will
properly recognize it:

```shell
% diskutil eraseDisk FAT32 SDCARD MBRFormat /dev/disk4
Started erase on disk4
Creating the partition map
Formatting disk4s1 as MS-DOS (FAT32) with name SDCARD
512 bytes per physical sector
/dev/rdisk4s1: 62488736 sectors in 1952773 FAT32 clusters (16384 bytes/cluster)
Finished erase on disk4
% diskutil list disk4
/dev/disk4 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *32.0 GB    disk4
   1:                 DOS_FAT_32 SDCARD                  32.0 GB    disk4s1
```

Now we can finally post it for sale.
