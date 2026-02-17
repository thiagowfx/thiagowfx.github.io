---
title: "(Some) SSD benchmarking"
date: 2013-11-16T14:48:31-03:00
tags:
  - dev
  - legacy
---

Last week I moved my Arch installation to my SSD, at the cost of losing the
native Windows caching (actually, losing Windows at all). Here is a summary of
what I did:

**SSD (32 GB):**

- 512 MB for /boot with ext4
- 31 GB for / with ext4

**HDD (500 GB):**

- 13 GB for /var with ext4
- 424 GB for /home with ext4
- 4 GB of swap
- Some gigs for another Linux distro

My /boot partition only eats only 36 MB (kernel 3.12). So 512 MB was clearly an
exaggerated choice (I really like to allocate more space, but 200 or 256 MB
would have been sufficient). My / partition is perfectly fine, I think it was
better (for my uses!) not to separate /usr from it. My /var will continue to
grow as I download more packages, so I feel 13 GB was really a comfortable
choice. I prefer not to clean it, mainly because I'm using Arch (recover/backup
reasons) and because I still have a lot of space available.

Up to today, I was tweaking my SSD by issuing `# fstrim -v /` and `# fstrim -v
/boot` manually. But that is annoying, so I'm looking up to use systemd, cron or
the 'discard' mount option to do that automagically for me.

## Benchmarking

### Psychological benchmarking

I feel very satisfied about my migration. The system boots really fast. I have a
small problem concerning systemd which makes me wait for +10 ~ 12 seconds than
the normal boot time; but, despite that, I think I achieve a little more than 10
seconds of a full boot time (until the login prompt). After entering my login
and password, XFCE 4 boots really fast (I've added a little script issuing
startx to my `~/.zprofile`). I can also tell that Firefox / Chromium / Thunar
(and so on) opens faster (than with the HDD). Eclipse, which takes more time, is
clearly taking less time to start.

### Benchmarking tools

Here is a small list of benchmarking tools, because numbers are not human
intuition. We can see that the SSD targets are usually faster than the HDD ones.

**hdparm -Tt (sda is the SSD):**

```bash
[thiago@thiago-ideapad] - [~] sudo hdparm -Tt /dev/sda

/dev/sda:
 Timing cached reads: 11852 MB in 2.00 seconds = 5930.31 MB/sec
 Timing buffered disk reads: 774 MB in 3.01 seconds = 257.55 MB/sec
```

**hdparm -Tt (sdb is the HDD):**

```bash
[thiago@thiago-ideapad] - [~] sudo hdparm -Tt /dev/sdb

/dev/sdb:
 Timing cached reads: 10982 MB in 2.00 seconds = 5495.10 MB/sec
 Timing buffered disk reads: 322 MB in 3.00 seconds = 107.24 MB/sec
```

We want to look at the **buffered** entries. As you can see, the SSD reads ~2x
faster than the HDD.

### Writing speeds

**SSD:**

```bash
[thiago@thiago-ideapad] - [~] sudo dd if=/dev/zero of=/tempfile bs=1M count=1024 conv=fdatasync,notrunc
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB) copied, 12.5929 s, 85.3 MB/s
```

**HDD:**

```bash
[thiago@thiago-ideapad] - [~] sudo dd if=/dev/zero of=/tempfile bs=1M count=1024 conv=fdatasync,notrunc
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB) copied, 87.2725 s, 12.3 MB/s
```

As you can see, the SSD writes ~7x faster than the HDD! That's the power of SSD.

## Overall

Yeah, SSD is faster (at least for reading). But (even) more important to state
that, is to try to maintain it healthy. I think it should last **at least** 2
years, but I hope to achieve 4 years with my care (even switching hardware until
there). The only thing I haven't done was to tweak the **partition alignment**.
If you want to do your own benchmarking, I recommend reading
[this](https://wiki.archlinux.org/index.php/Partitioning#Partition_alignment).
Also, please consider adding your own results to the wiki if you have time.
