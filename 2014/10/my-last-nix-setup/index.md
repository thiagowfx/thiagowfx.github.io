
I've just completed my objective with this blog. Should I start a new one? After
looping through a BSD distro and dozens of Linux distributions, I've finally
decided to settle down and stay away from new test drives. This time should be
definitive—I really do not intend to replace my system anymore. The point is now
I have a stable configuration and a few preferences that I would like to share
with you.

## The Setup

I don't intend this to take too long, so I'll be brief:

- **Filesystem**: btrfs instead of ext4. Snapshots are awesome, and I also can
  benefit from its SSD and compression performance.
- **Partition scheme**: split your root (/) and home (/home) partitions. Always.
  Unless you're in a hurry, or unless you do not intend to create a non-root
  user. Since I'm using btrfs, I also split my 300-500MB ext4 /boot partition.
  My preferred size for root is (30 ± 15)GB. /home takes up the rest. No LVM.
- **UEFI**: I don't use it now, but I would probably do that the next time I buy
  a new computer. Just take care of your ESP partition and disable secure boot.
- **Bootloader**: syslinux! GRUB2 is way too automatic. Syslinux is simpler and
  faster. If you're in a hurry, stick to GRUB2.
- **Linux Distro**: Arch Linux. Period. If you're in a hurry, use a derivative
  of Arch. If you're even more in a hurry, use a derivative of Debian or Ubuntu.
  Linux Mint is my preferred choice, but Xubuntu or Lubuntu are good lightweight
  options.
- **BSD Distro**: FreeBSD. I love its documentation and traditional Unix
  feeling. But it was the only BSD distro I've tested up to today.
- **Tiling window manager**: i3. KISS, KISS, KISS. And elegant. With i3blocks,
  please.
- **Stacked window manager**: Cinnamon.
- **Full-featured file manager**: dolphin (or nemo, but only if you are using
  Cinnamon).
- **Lightweight file manager**: thunar.
- **Terminal/text editor**: vim.
- **GUI text editor**: emacs.
- **Shell**: zsh. With grml configurations, auto-completion and syntax
  highlighting. It's perfect. Oh-my-zsh is a common alternative.
- **Terminal emulator**: urxvt (rxvt-unicode). With tabs.
- **Monospaced bitmap font**: terminus.
- **Monospaced scalable font**: Source Code Pro (from Adobe).
- **System font**: either Bitter, Cantarell, Ubuntu or Droid Sans.
- **Plug-in manager for emacs**: el-get.
- **Plug-in manager for vim**: pathogen.
- **Display manager**: lightdm.

## Conclusion

This is the best Linux/BSD setup I've ever dreamed of, and I'm really happy. The
original purpose of this blog has been achieved. Through 2 years, what I most
posted here were concerns about Linux. The purpose was to share my own ignorance
and growing maturity towards this awesome subject area.

Now my focus turns to **Programming languages**. Today I feel the same
insecurity towards programming languages that I used to feel two years ago about
Linux. I want to be very good at a few programming languages, and at least know
a couple of them (maybe 5-10). I want to be part of a programming language
community and evangelize programming.

This blog will still exist. I will probably keep posting here with the same rate
I post nowadays, but I will probably talk less about Linux and more about other
things. However, when I get into programming deeply, I might create a new space
for that purpose.

If you are still reading here, thank you. I really appreciate the support of the
people that express interest in this blog. I also hope that others could learn
something during all this time.

