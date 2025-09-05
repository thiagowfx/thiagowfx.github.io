---
title: "Linux: Remount device with different options"
date: 2022-01-29T23:16:04-05:00
tags:
  - dev
---

A few recipes for remounting linux devices / disks. It mostly boils down to running `mount -o remount` as root.

## Remount as read-write

If `/dev/sdb1` is mounted on `/mnt/data` as read-only (`ro`), it could be remounted as `rw`:

```shell
% mount -o remount,rw /mnt/data
```

or

```shell
% mount -o remount,rw /dev/sdb1
```

## Increase RAM disk size

`/dev/shm` (shared memory) is typically allocated half of the available amount of RAM in the system. For example, in my 8GB Arch Linux system:

```shell
$ df -h | grep /dev/shm
tmpfs                  3.9G  127M  3.8G   4% /dev/shm
```

To increase the amount of space allocated to it:

```shell
% mount -o remount,size=8G /dev/shm
```

The result:

```shell
$ df -h | grep /dev/shm
tmpfs                  8.0G   72M  8.0G   1% /dev/shm
```
