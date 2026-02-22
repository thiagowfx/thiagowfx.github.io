
Once upon a time, my alpine linux VPS was located in Toronto (Canada). For a
while now it's been in Frankfurt (Germany).

Linode makes changing the location of your VPS a breeze.
Recently though I realized I forgot to update the system timezone.

In the `systemd` world, we would do this:

```shell
timedatectl set-timezone Europe/Berlin
```

And verify it with:

```shell
timedatectl show --property=Timezone --value
```

I appreciate the simplicity of `timedatectl`.

However, this is Alpine Linux, wherein we don't say the [`s*`
word](https://nosystemd.org/).

First, identify your desired timezone:

```shell
ls /usr/share/zoneinfo
```

We'll go with `Europe/Berlin`. Symlink `/etc/localtime` to it:

```shell
doas ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime
```

In addition, update `/etc/timezone`:

```shell
echo 'Europe/Berlin' | doas tee /etc/timezone
```

That's all.

For completeness you may want to `reboot` afterwards, but it's not strictly
necessary.

