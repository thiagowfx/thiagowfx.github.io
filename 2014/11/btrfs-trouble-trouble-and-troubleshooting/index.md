
The last weekend I lost more than **8 hours** trying to recover from a serious
bug that reached the btrfs filesystem in recent days. This bug was relatively
specific: it would only affect Linux users running a specific kernel version
(3.17.1, if I recall correctly), a specific version of the btrfs-progs package,
**and** systems with read-only snapshots — yeah, I've been using the snapshot
feature of the btrfs filesystem extensively.

## First Symptom

After a `pacman -Syu`, my entire filesystem became read-only. I couldn't save
anything. So I rebooted it.

Then I found myself directly in the initramfs rescue prompt. I've always had
nightmares with this prompt. I wouldn't have access to all my files until I got
rid of it.

A few Google searches alerted me that this was a **severe/critical** bug.
However, fortunately (or unfortunately...), other beta and enthusiastic people
also had it. The Arch Linux bug tracker and its discussion forums contained
mentions about it. They served as an initial "what am I supposed to do now,
besides screaming?".

## The Recovery Process

I had backups, but they were a few weeks old. During this process, I fell in
love with the **grml Linux distribution**. It is amazing for recovery processes
and inspired the creators of Arch (the other inspiration is CRUX, which I still
haven't tried). It's based on Debian/testing.

From grml, I logged into Hexchat (an IRC client) in the #btrfs channel, and
within less than five minutes I got help and orientation from a guy who had the
same problems. He told me what I was supposed to do, and it really worked! Now I
have my system back.

## Why It Took 8+ Hours

It wasn't that straightforward. Mainly because I was downloading several distros
and dd'ing them onto USB Flash Drives from a grml virtual machine inside the
Windows 8 desktop from my parents' house. I did this several times until I
realized (well, the #btrfs guy realized) that I needed a recent Linux kernel to
do the recovery process.

What Linux distribution has a recent kernel? Arch, of course. The actual
recovery process was done inside an Arch live medium.

Grml taught me several things to expect from a recovery distribution designed
for system administrators. Unfortunately, its kernel was relatively old at the
    time (it's based on Debian, so I can't blame it).

## The Takeaway

Although losing several hours, I:

- Discovered a nice Linux distribution
- Was convinced (again) that IRC is still awesome
- Could post on the Arch forums confirming the solution I used
- Had fun in the process **(YES. I love this sysadmin thing.)**

**Moral of the story: BACKUP YOUR SYSTEMS!!!! And sleep well.**

---

I'm now using ext4 on my root partition and btrfs on my home partition. This
means I can hibernate my system now — I missed that for a while.

## References

1. https://bbs.archlinux.org/viewtopic.php?id=188900
2. https://bugs.archlinux.org/task/42563

