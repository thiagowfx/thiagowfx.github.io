---
title: "★ Alpine Linux: apk command not found hook"
date: 2022-01-04T16:25:51-05:00
tags:
  - linux
  - star
---

In this post we will learn how to define a command-not-found hook to the `apk(8)` package manager in Alpine Linux.

## Sneak peek

Before:

```shell
$ podman
zsh: correct 'podman' to 'pod2man' [nyae]? n
zsh: command not found: podman
```

After:

```shell
$ podman
zsh: correct 'podman' to 'pod2man' [nyae]? n
podman may be found in the following packages:
  <cmd:podman> podman-3.4.4-r1 x86_64 {podman} (Apache-2.0)
```

<!--more-->

## Preamble

Whenever you type a command that is not in your `$PATH`, usually your shell
will yell at you that it wasn't found.

The typical workflow in this scenario is to use the search functionality of your package manager in order to find which package provides the binary you're interested in.

In Alpine Linux, one would do:

```shell
$ apk search podman
podman-doc-3.4.4-r1
podman-remote-3.4.4-r1
podman-docker-3.4.4-r1
openscap-1.3.5-r3
podman-3.4.4-r1
podman-compose-0.1.5-r4
podman-bash-completion-3.4.4-r1
podman-zsh-completion-3.4.4-r1
py3-podman-3.2.1-r1
podman-docker-doc-3.4.4-r1
podman-openrc-3.4.4-r1
podman-fish-completion-3.4.4-r1
```

The output is a bit noisy, but with a bit of experience you could easily figure out the package you're looking for is simply called `podman`, given the output above.

Surely this was an easy example, what if we tried something less obvious?

```shell
$ vidir
zsh: correct 'vidir' to 'vdir' [nyae]? n
zsh: command not found: vidir
```

There's no `vidir` binary, then surely there's a `vidir` package, right?

```shell
$ doas apk add vidir
ERROR: unable to select packages:
  vidir (no such package):
    required by: world[vidir]
```

Er, no. You'll need to use search again:

```shell
$ apk search vidir
moreutils-0.67-r0
```

There it is, `moreutils`. Great piece of software, by the way[^moreutils].

What if we could automate this?

## Automating command-not-found: 1st try

In bash, one can define a `command_not_found_handle` function. In zsh, one can define a `command_not_found_handler` function. I know, why can't it be the same function, right? Just one `r` in the way. Regardless of whichever shell you use, the point is that the function is invoked whenever you run a command that is not in the `$PATH` (or that isn't a shell built-in).

In principle, you could do:

```shell
command_not_found_handle() {
  local cmd="$1"
  apk search "$cmd"
}
```

It's a good first try, and it surely works as expected, but it can be a bit noisy sometimes. Look at the podman output above, it outputs several unrelated packages, none of which provide the `podman` binary other than its homonym.

## Automating command-not-found: 2nd try

In Alpine, we can do slightly better. `apk(8)` has the concept of providers:

```shell
$ apk list -P | awk '{print $1}' | egrep '<\w+:' | cut -f 1 -d ':' | cut -c 2- | sort -u
cmd
dbus
pc
so
```

`-P` above stands for `--providers`. This roughly means one can search for a package that provides a given shared library (`so`), or a package that provides a given binary (`cmd`), and so on. We're interested in the `cmd:` provider.

If we tried it with `podman`, we would get the following output:

```shell
$ apk list -P -- "cmd:podman"
<cmd:podman> podman-3.4.4-r1 x86_64 {podman} (Apache-2.0)
```

Look at how much shorter and direct it is, compared to the 1st approach!

Here's what it looks like if we try it with a binary provided by multiple packages:

```shell
$ apk list -P -- "cmd:docker"
<cmd:docker> docker-cli-20.10.11-r0 x86_64 {docker} (Apache-2.0) [installed]
<cmd:docker> podman-docker-3.4.4-r1 x86_64 {podman} (Apache-2.0)
```

It's very easy to see that both `docker-cli` and `podman-docker` provide `docker`. If you just did a simple search, you'd get a lot of noise:

```shell
$ apk search docker
docker-bash-completion-20.10.11-r0
docker-cli-20.10.11-r0
docker-machine-driver-kvm2-1.24.0-r0
x11docker-6.9.0-r2
docker-volume-local-persist-1.3.0-r5
podman-docker-3.4.4-r1
openvswitch-2.12.3-r4
docker-engine-20.10.11-r0
docker-openrc-20.10.11-r0
dockerize-0.6.1-r9
docker-fish-completion-20.10.11-r0
openscap-1.3.5-r3
docker-py-5.0.3-r1
openvswitch-ovn-2.12.3-r4
docker-registry-openrc-2.7.1-r5
docker-doc-20.10.11-r0
rsyslog-imdocker-8.2108.0-r0
lazydocker-0.12-r2
docker-compose-bash-completion-1.29.2-r2
docker-compose-1.29.2-r2
py3-dockerpty-0.4.1-r4
docker-compose-zsh-completion-1.29.2-r2
docker-registry-2.7.1-r5
docker-credential-ecr-login-0.5.0-r2
dockerpy-creds-0.4.0-r3
docker-cli-compose-2.1.1-r0
docker-credential-ecr-login-doc-0.5.0-r2
podman-docker-doc-3.4.4-r1
docker-20.10.11-r0
docker-compose-fish-completion-1.29.2-r2
flannel-contrib-cni-0.15.1-r0
docker-zsh-completion-20.10.11-r0
docker-volume-local-persist-openrc-1.3.0-r5
docker-cli-buildx-0.7.1-r0
```

## Packaging[^packaging] it all together

I wrote the following scripts, which I source in my respective interactive shells, to achieve this behavior out-of-the-box:

```shell
$ cat apk-command-not-found.bash
#!/bin/bash
# apk(8) from Alpine Linux command not found hook for bash

command_not_found_handle () {
        local cmd="$1" pkgs
        mapfile -t pkgs < <(apk list -P -- "cmd:$cmd" 2>/dev/null)

        if (( ${#pkgs[*]} )); then
                echo "$cmd may be found in the following packages:"
                printf '  %s\n' "${pkgs[@]}"
        else
                echo "bash: command not found: $cmd"
        fi 1>&2

        return 127
}
```

```shell
$ cat apk-command-not-found.zsh
#!/bin/zsh
# apk(8) from Alpine Linux command not found hook for zsh

command_not_found_handler() {
        local cmd="$1"
        local pkgs=(${(f)"$(apk list -P -- "cmd:$cmd" 2>/dev/null)"})

        if [[ -n "$pkgs" ]]; then
                echo "$cmd may be found in the following packages:"
                printf '  %s\n' "${pkgs[@]}"
        else
                echo "zsh: command not found: $cmd"
        fi 1>&2

        return 127
}
```

The snippets above are snapshots intended for this post.
I keep up-to-date versions of these files in my dotfiles repository, [try out this query](https://github.com/thiagowfx/.dotfiles/search?q=filename%3Aapk-command-not-found&type=code) in case I ever move them elsewhere.

[^moreutils]: https://joeyh.name/code/moreutils/: moreutils is a collection of the unix tools that nobody thought to write long ago when unix was young.
[^packaging]: pun intended
