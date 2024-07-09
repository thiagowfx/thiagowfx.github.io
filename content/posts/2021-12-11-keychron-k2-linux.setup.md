---
title: '★ Keychron K2: Linux Setup'
date: 2021-12-11T20:59:21-05:00
lastmod: "2022-01-03"
tags:
  - hardware
  - linux
  - bestof
---

I recently purchased a [Keychron K2](https://www.keychron.com/products/keychron-k2-wireless-mechanical-keyboard) mechanical keyboard. It is a 75% keyboard that has bluetooth. This article describes some quality-of-life improvements to use it with a Linux system.

<!--more-->

**Note**: Tested on Arch Linux only.

## Kernel Module

Keychron keyboards are recognized out-of-the-box as Apple keyboards on Linux systems.

The corresponding kernel module is `hid_apple`.

```shell
$ modinfo hid_apple
```

Ensure the module is loaded within the initram for setups that use LUKS:

```shell
$ grep MODULES -B 1 /etc/mkinitcpio.conf
# hid_apple for Keychron K2
MODULES=(hid_apple)
```

This works for wired mode but alas it's not possible to use the keyboard wirelessly to type in your LUKS password unless extra steps are taken:

- Install the [`mkinitcpio-bluetooth`](https://aur.archlinux.org/packages/mkinitcpio-bluetooth/) package, currently available in the AUR.
- Add the `bluetooth` hook to your mkinitcpio, ensuring it comes before `encrypt`.

```shell
$ grep HOOKS -B 1 /etc/mkinitcpio.conf
# bluetooth for Keychron K2
HOOKS=(base udev autodetect keyboard bluetooth modconf block encrypt filesystems resume fsck)
```

- Regenerate it: `% mkinitcpio -P`.

## Bluetooth

There are 3 bluetooth slots, corresponding to the `1`, `2` and `3` keys.

To put the keyboard in pairing mode, hold `Fn + <n>` for a few seconds. The key will persistently blink.
From the computer, connect to the device named `Keychron K2`. Trust the keyboard.

Switch slots by pressing `Fn + <n>` once. There is some light feedback to indicate the switch.

Bluetooth works well out-of-the-box, but the keyboard automatically sleeps after 10 minutes of inactivity to save energy.
While it is possible to disable this behavior, I find it welcome. It is a hassle though because the bluetooth device refuses to reconnect once the keyboard is awaken. The naive solution is to pair it again from scratch, but a better user experience is to change bluetooth settings:

```shell
$ cat /etc/bluetooth/main.conf
...
[General]
FastConnectable=true

[Policy]
UserspaceHID=true
...
```

And then restart bluetooth to apply them:

```shell
% systemctl restart bluetooth
```

This way the keyboard always automatically reconnects to the computer.

I also find it convenient to leave bluetooth enabled on startup:

```shell
# Enable the bluetooth daemon.
% systemctl enable bluetooth

# Enable the bluetooth adapter.
$ cat /etc/bluetooth/main.conf
...
[Policy]
AutoEnable=true
...
```

Finally, another tweak is to make the bluetooth adapter stay awake otherwise it may periodically disconnect:

```shell
$ cat /etc/modprobe.d/btusb.conf
# Turn off bluetooth autosuspend.
options btusb enable_autosuspend=0
```

## Function Keys and Multimedia Keys

The default `fnmode` is set to multimedia keys:

```
0 = disabled
1 = normally media keys, switchable to function keys by holding Fn key (Default)
2 = normally function keys, switchable to media keys by holding Fn key
```

I prefer to set it to function keys. One of the reasons for that is to make
switching TTYs (Ctrl+Alt+Fn) possible. For some reason, Fn doesn't seem to work
in TTYs.

Change it in the current session only:

```shell
% echo 2 >> /sys/module/hid_apple/parameters/fnmode
```

If you do not have a root shell, use `sudo` / `doas` + `tee`:

```shell
% echo 2 | sudo tee /sys/module/hid_apple/parameters/fnmode
```

Change it permanently:

```shell
$ cat /etc/modprobe.d/hid_apple.conf
# Use function keys by default. Press Fn to use multimedia keys.
options hid_apple fnmode=2
```

And then reload the kernel module:

```shell
% modprobe -r hid_apple && modprobe hid_apple
```

## Insert Key

By default there is no native `Insert` key. Use `Fn + Del` to trigger `Insert`. For example, `Fn + Shift + Del` works like `Shift + Insert` in X11, yielding paste selection.

## Battery

Check the battery level programmatically:

```shell
% pacman -S upower
$ upower --dump | grep -i keyboard -A 7 | grep percentage
    percentage:          71%
```

This only works in bluetooth mode (not in wired mode).

## Shortcuts

- Hold `Fn + [1 | 2 | 3]` for a few seconds: Put bluetooth slot in pairing mode. The corresponding LED will persistently blink until pairing is complete.
- `Fn + [1 | 2 | 3]`: Toggle bluetooth slot. The corresponding LED will briefly blink.
- `Fn + b`: Check battery level visually. Green is more than 70%, blue is more than 30%, otherwise it will flash.
- `Fn + Light`: Toggle keyboard lights on/off.
- `Fn + [Left | Right]`: Browse keyboard light color schemes.

## References

- https://wiki.archlinux.org/title/Apple_Keyboard
- https://github.com/kurgol/keychron
- https://gist.github.com/andrebrait/961cefe730f4a2c41f57911e6195e444
- https://mikeshade.com/posts/keychron-linux-function-keys/
- https://github.com/kurgol/keychron/blob/master/k2.md
