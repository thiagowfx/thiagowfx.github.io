
I am currently evaluating [Nix](https://nixos.org/download.html) as a
replacement for [Homebrew](https://brew.sh) CLI apps in macOS[^1].
[Others](https://wickedchicken.github.io/post/macos-nix-setup/)
[have](https://ianthehenry.com/posts/how-to-learn-nix/switching-from-homebrew-to-nix/)
[previously](https://ghedam.at/15490/so-tell-me-about-nix) written about this.

My goal is to keep a sane learning curve and learn things on-the-fly, only as
needed. Nix is a massive ecosystem and has so many batteries included and
components (NixOS, NixPkgs, NixOps, Nix programming language, nix-shell,
nix-env, nix-darwin, home-manager, ...). The good news is that those components
are for the most part modular, there's no need to adopt them all in order to
reap the benefits that Nix provides.

For now, I am only adopting `nix-env` and `nix-shell`, with no `*.nix` config
files. This post covers `nix-env`.

For simplicity, think of `nix-env` as a package manager, akin to `apk`,
`pacman`, `brew`, `apt`, `pkg`, etc.

## Install a package

```shell
$ nix-env -i moreutils
installing 'moreutils-0.67'
building '/nix/store/jsp0l5ny3kx8p9lx9w9r0x159i9jjnn6-user-environment.drv'...
```

I see some guides using `nix-env -iA` but `-i` seems to suffice. We could
optionally specify the `nixpkgs.` prefix:

```shell
$ nix-env -i nixpkgs.moreutils
error: selector 'nixpkgs.moreutils' matches no derivations
```

Oh no! Maybe that's what the `-A` is for?

```shell
$ nix-env -iA nixpkgs.moreutils
replacing old 'moreutils-0.67'
installing 'moreutils-0.67'
```

Indeed! Apparently that `-A` thing stands for attribute. The only thing I know
is that there are both `nixpkgs.*` and `nixos.*`. But I don't care about NixOS
at this point. I'll just ignore `-A` from now on, for the time being.

## List installed packages

```shell
$ nix-env -q
moreutils-0.67
```

Easy! This actually gets displayed in my `less` pager.

## Upgrade installed packages

```shell
$ nix-env -u
```

Easy! At this point, I am not super confident whether that works as intended
though. We will find out in a few days when there's some update to one of my
installed CLI applications. I've heard there's something called nix channel to
control that. Leaving it for another day though.

**Update(2022-02-18)**: I learned that `nix-env -u` is akin to `apt upgrade` or
`apk upgrade`. It upgrades installed packages to newer versions but only if it
is aware there are newer versions. To actually refresh the repositories à la
`apt update` or `apk update`, use `nix-channel --update`.

**Note**: On macOS this needs to be `sudo -i nix-channel --update`. See
[issue](https://github.com/NixOS/nix/issues/3595).

## Uninstall a package

```shell
$ nix-env --uninstall moreutils
uninstalling 'moreutils-0.67'
building '/nix/store/5k8rsf4cxg4iz7cqnqirpww6r97bwnqr-user-environment.drv'...
```

Easy!

## Search for packages

```shell
$ nix-env -qaP '.*moreutils.*'
```

The `.*` seems to be needed. It works if I omit them, but only if I write the exact package name (apparently called 'derivation' in Nix):

```shell
$ nix-env -qaP moreutils
nixpkgs.moreutils  moreutils-0.67
```

If I write the wrong package name, the following happens:

```shell
$ nix-env -qaP moreutil
error: selector 'moreutil' matches no derivations, maybe you meant:
       moreutils
```

It was helpful in this case, but I wouldn't always count on that. It is a bit
annoying that there's no `nix search moreutils` command, but it seems that
`nix-env` is very heavily tailored to use short flags, just like `pacman` in
Arch Linux. I got used to `pacman`, hopefully I can get used to the `nix-env`
short flags at some point.

Actually I tried it out and there is a `nix search` command!

```shell
$ nix search moreutils
error: experimental Nix feature 'nix-command' is disabled; use '--extra-experimental-features nix-command' to override
```

This isn't very promising though. How come searching is experimental?! Anyway, I can live with the `nix-env` form for now.

These are the 5 basic package management operations that I needed to bootstrap
my dev environment. Without putting much effort on it, my initial list of package
looks like this:

```shell
$ nix-env -q
atool-0.39.0
bash-interactive-5.1-p12
coreutils-9.0
exa-0.10.1
fpp-0.9.2
fzf-0.29.0
git-2.34.1
htop-3.1.2
hugo-0.92.0
jq-1.6
less-600
moreutils-0.67
ncdu-1.16
perl5.34.0-ack-3.5.0
ranger-1.9.3
stow-2.3.1
tmux-3.2a
tree-1.8.0
vim-8.2.4186
watch-procps-3.3.16
wget-1.21.2
zoxide-0.8.0
```

Those were very intuitive to find, with the exception of `ack` and `bash-interactive`:

- `bash` is a bit odd because Nix splits it into two packages:
  a non-interactive version and an interactive version. I have no idea why. My
  `~/.bashrc` wrecked havoc with the non-interactive version.
- `ack` is very oddly named. Really. Also: `nix-env -i ack` doesn't work, but
  `nix-env -iA nixpkgs.ack` does. I suspect it will be hard to ignore `-A` in
  the future.

[^1]: Strictly speaking there's nothing special about macOS in this context.
  The same setup can also be used in Linux distributions, for example, [Debian
  or Ubuntu](https://ariya.io/2020/05/nix-package-manager-on-ubuntu-or-debian).
  In fact, this is what I did at $DAYJOB, because relying solely on Debian for
  package management is a very big limitation. I find that Nix complements the
  Debian repositories very well, the same way that it does for macOS.

