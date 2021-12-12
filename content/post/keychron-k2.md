---
title: "Keychron K2"
date: 2021-12-11T20:59:21-05:00
---

## Review

https://www.keychron.com/products/keychron-k2-wireless-mechanical-keyboard

TODO(thiagowfx): Write review.

## Linux setup

**Note**: This setup was tested on Arch Linux.

### Kernel module

Keychron keyboards are recognized as Apple keyboards on Linux systems.

The corresponding kernel module is `hid_apple`.

```shell
$ lsmod | grep hid_apple
$ modinfo hid_apple
```

### Bluetooth

There are 3 bluetooth slots, corresponding to the `1`, `2` and `3` keys.

To put the keyboard in pairing mode, hold `Fn + <n>` for a few seconds. The key will persistently blink.
From the computer, connect to the device named `Keychron K2`.

Switch slots by pressing `Fn + <n>` once. There is some light feedback to indicate the switch.

Bluetooth works well out-of-the-box, but the keyboard automatically sleeps after 10 minutes of inactivity to save energy.
While it is possible to disable this behavior, I find it welcome. It turns out this creates a hassle though because the bluetooth device refuses to reconnect once the keyboard is awaken. The naive solution is to pair it again from scratch, but a better user experience is to change bluetooth settings:

```shell
$ cat /etc/bluetooth/main.conf
[General]
FastConnectable=true

[Policy]
UserspaceHID=true
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
[Policy]
AutoEnable=true
```

### Function Keys

The default `fnmode` is set to multimedia keys:

```
0 = disabled
1 = normally media keys, switchable to function keys by holding Fn key (Default)
2 = normally function keys, switchable to media keys by holding Fn key
```

I prefer to set it to function keys.

Change it in the current session only:

```shell
% echo 2 >> /sys/module/hid_apple/parameters/fnmode
```

Change it permanently:

```shell
$ cat /etc/modprobe.d/keychron.conf
# Use function keys by default. Press Fn to use multimedia keys.
options hid_apple fnmode=2
```

And then reload the kernel module:

```shell
% modprobe -r hid_apple && modprobe hid_apple
```

### Battery

Check the battery level programatically:

```shell
% pacman -S upower
$ upower --dump | grep -i keyboard -A 7 | grep percentage
    percentage:          71%
```

This only works in bluetooth mode (not in wired mode).

Check the battery level visually, hold `Fn + b`:

- 70%+: green
- 30%~70%: blue
- 30%-: flashing

### Shortcuts summary

- Press `Fn + [1 | 2 | 3]`: Toggle bluetooth slot.
- Hold `Fn + [1 | 2 | 3]` for a few seconds: Put bluetooth slot in pairing mode.
- `Fn + b`: Check battery level visually.
- `Fn + Light`: Toggle keyboard lights on/off.

### References

- https://wiki.archlinux.org/title/Apple_Keyboard
- https://github.com/kurgol/keychron
- https://gist.github.com/andrebrait/961cefe730f4a2c41f57911e6195e444
- https://mikeshade.com/posts/keychron-linux-function-keys/
