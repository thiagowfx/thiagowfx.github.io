
[Previously]({{< ref "2014-03-29-server-challenge-instance-0" >}}).

I'm installing four distros (Arch, Ubuntu Server, CentOS, openSUSE) with
VirtualBox. We need a testing environment without affecting real systems.

## Virtualization Setup

**Chosen tool**: VirtualBox (open source; QEMU is too advanced)

**Virtual machine specs**:

- 16 GB disk per VM (10-12 GB would be sufficient)
- 512 MB RAM (768 MB for openSUSE since it starts X by default)

## ISO Download Experience

I'll rank distros by download experience:

### Downloads

- **Ubuntu**: Straightforward. Find it at ubuntu.com
- **Arch**: Easy at archlinux.org (single minimal ISO)
- **CentOS**: Harder to find the minimal ISO at centos.org
- **openSUSE**: Confusing at opensuse.org (live vs. network version unclear)

### ISO Sizes

- **Arch**: ~500 MB (minimal, core components only)
- **Ubuntu**: ~650 MB
- **CentOS**: ~4 GB (DVD) or ~400 MB (minimal) — I downloaded the wrong version
- **openSUSE**: ~950 MB (KDE Live) or ~300 MB (network)

*Note: I made errors downloading the wrong CentOS and openSUSE versions. Managing 4 distros plus my own system meant I couldn't afford more time on this.*

## Installation Decisions

- Partitions: `/` and swap (512 MB; 768 MB for openSUSE)
- Filesystem: ext4
- **LVM**: Not just classic MBR for learning

## Installation Reviews

**Ubuntu**: ncurses installer is good but requires getting options right initially. Changing timezone/keyboard after installation is painful — the inconsistency between pre- and post-installation is frustrating. You don't see the commands being run, which hides knowledge.

**CentOS**: I hated it. It's intuitive but forces LVM by default — no choice offered.

**openSUSE**: Best installer I've seen. Incredibly customizable with an intuitive UI. You can easily choose btrfs, LVM, anything. But it uses X (mouse interface) and runs post-installation setup after reboot — only openSUSE does this. Same flaw as Ubuntu: you don't learn what's happening behind the scenes.

**Arch**: No installer by design. This is a feature — you have full control and know exactly what you're entering. If you can set up Arch from scratch with LVM, you understand what you're doing. This is rare. The downside: it takes time if you don't know the process. But the Arch Wiki is excellently documented. Automatic installers save time but reduce knowledge.

## Next Steps

I'll set up LVM on Arch using my desktop system (no duplicate effort). Then
decide: either document LVM setup on Arch, or move forward with LAMP
(Linux-Apache-MySQL-PHP/Python/Perl).

Until the next post!

