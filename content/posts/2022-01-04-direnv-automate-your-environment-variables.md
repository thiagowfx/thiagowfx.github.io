---
title: "Direnv: Automate your Environment Variables"
date: 2022-01-04T00:34:07-05:00
tags:
  - dev
  - bestof
---

[Direnv][direnv] is a tool to automate your shell to automatically load and unload environment variables on-the-fly, on a per-project (per-directory) basis.


## Preliminaries: Is it worth it?

Questions I like to ask myself before deciding whether to invest my time into learning and potentially **adopting** a foreign tool are the following:

> Is it **popular** _and_ **stable** enough?
> Is it abandonware?

### Popularity

Popularity is relative, it doesn't need to be worthy of the Hacker News frontpage nor Hotness on Reddit, but it needs to be widely available in popular Linux distributions and/or package managers, one install command away from my development environment.

[Repology][repology] is a good proxy for popularity. Looking at [direnv][repology-direnv] therein, it's available for Alpine, Arch, Debian, Fedora, FreeBSD, HomeBrew, Nix, OpenBSD, Ubuntu...that's more than enough, we can safely conclude `direnv` is widely popular.

The main takeaway we want to confirm is whether the project isn't too niche and/or an one-man show. Seeing signs of a small-ish community and/or occasional contributions from external users/developers helps build confidence and give credibility to the project.

### Stability and Abandonware

Stability is easier to define than popularity and can often be determined just by taking a quick glance at the github (or whichever other forge it's hosted in) page of the project.

At the time of this writing, the latest release of [direnv][direnv-github] was about a week ago (2.30.2, Dec 28th 2021). It's definitely not abandonware and it's well maintained. A few signs that help corroborate that:

- Several PRs were merged recently
- Its issue tracker is quite active, with a good mix of feature requests and bugs
- I don't like to judge the project based on the number of issues it has, especially if it's popular. Chromium has [60k+][chromium-bugtracker] issues at the time of this writing, yet I wouldn't call it _bleeding edge_. Common sense applies. Since `direnv` has been around for a while and it's relatively popular, 150+ open issue seems acceptable to me.

Now that `direnv` passed the Litmus test for adoption[^foss], let's get our hands dirty.

## Installation

There's nothing special here, as `direnv` is widely packaged. Pick your poison:

```shell
$ sudo pacman -Syu direnv  # Arch Linux
$ doas apk add direnv  # Alpine Linux
$ sudo apt install direnv  # Debian-based distros
```

Is it lightweight?

```shell
$ apk info -L direnv
direnv-2.30.1-r0 contains:
usr/bin/direnv
```

Hell yes! More lightweight than that? Impossible. It's a single binary thanks to Golang. No tons of files or dependencies. I mean:

```shell
$ du -sh /usr/bin/direnv
7.5M    /usr/bin/direnv
```

...it's a 7MB binary, let's not get ahead of ourselves. But that's fine, really, it's just a dev tool, we don't really deploy it to prod.

## Use Cases

Everything is controlled with a `.envrc` file within a repository root. A typical file could look like this:

```
export HOUSE="ATREIDES"
layout python3
```

The [upstream website][direnv] does a great job at summarizing use cases. I am not here to duplicate documentation, so please go ahead and read it. That said, here are some example use cases I found useful:

### Use Case: Python

Python developers often need to create different virtual environments for different projects. For example, I was participating in [Advent of Code](https://adventofcode.com/) last year and wrote my solutions in Python 3: https://github.com/thiagowfx/adventofcode.

Each day[^aoc] I would `cd ~/projects/adventofcode`, and then do `source ~/.venv/bin/activate`. And guess what, that's for the first terminal where I'd run `make`, I'd also spawn a second one with `vim`, thereby needing to activate the virtual environment twice.

And this is assuming the virtual environment already exists. If it didn't - for example, after a vanilla `git clone`, I'd have to do `python -m venv .venv` first.

Quickly all of this became repetitive and annoying. I kinda "cheated" and stopped using the virtualenv for a few days, relying on my Linux distribution package manager instead:

```shell
% apk add py3-{autopep8,pyflakes,numpy,pylint}
```

This way, my

```python
import numpy
```

would correctly work and not yell that `numpy` was nowhere to be found.

It's not very clean, but it worked. However eventually I wanted to become cleaner and leaner and automate my virtual environment setup. I uninstalled the aforementioned packages after a few days:

```
% apk del py3-{autopep8,pyflakes,numpy,pylint}
```

...therefore forcing me to come up with a better setup. I always had direnv in my TODO list, and this was the perfect moment to try it out.

How does `direnv` address this?

1. Add the `direnv` hook to your shell. I actively use two shells[^shells], `bash` and `zsh`, so I did it twice and then added it to my [dotfiles](https://github.com/thiagowfx/.dotfiles):

Bash:

```bash
$ cat ~/.bashrc.d/direnv.bash
#!/bin/bash
# https://direnv.net/
if hash direnv >/dev/null 2>&1; then
        eval "$(direnv hook bash)"
fi
```

Zsh:

```zsh
$ cat ~/.zshrc.d/direnv.zsh
#!/bin/zsh
# https://direnv.net/
if (( $+commands[direnv] )); then
        eval "$(direnv hook zsh)"
fi
```

2. Set up direnv in the AOC repository:

```shell
$ cat ~/projects/adventofcode/.envrc
layout python3
$ direnv allow  # Only needs to be done once
```

That's it: It's a single line of configuration. Now what does it do? All of the above. No magic: whenever you cd into the project directory or any of its subdirectories with one of the configured shells, if the venv doesn't exist:

- it will be automatically created;
- then it will be sourced

Now you may ask yourself: Why go through all this trouble? Why not simply create a shell script to do exactly that for you automatically? That's perfectly fine, it's a matter of taste. But then you'll have to maintain that script. The python ecosystem keeps changing - a few years ago I was using `virtualenvwrapper` to manage virtual environments, these days it doesn't exist anymore, people use either `python -m env` or `pyenv` or `poetry` or...it never ends. [Drew DeVault][drew] wrote a good piece about that.

{{< figure align="center" src="https://imgs.xkcd.com/comics/python_environment.png" link="https://xkcd.com/1987/" alt="The Python environmental protection agency wants to seal it in a cement chamber, with pictorial messages to future civilizations warning them about the danger of using sudo to install random Python packages." attr="XKCD Courtesy of Randall Munroe" >}}

Maintenance is not the only burden, scalability is also one: If you use python in several repositories, you'll now have to include your script in all of them.

Considering that `direnv` is flexible enough in other scenarios, I consider its adoption in this situation a good trade-off to make.

### Use Case: Hugo

This blog is written in Hugo. I have a `Makefile` with a bunch of environment variables to manage its setup:

```shell
$ make dev
```

Whenever I am working in my VPS, for reasons outside of the scope of this post I need to use a different port other than the default one for Hugo (`1313`). Since I am using variables, I could just do:

```shell
$ make PORT=1234 dev
```

However, to make this change permanent ("fire-and-forget"), I could also do:

```shell
$ echo 'export PORT=1234' | tee -a .envrc
$ direnv allow  # Only needs to be done once
$ make dev
```

This way, whenever I run `make` I wouldn't even need to think twice about which port to use.

Of course, a small improvement that should be done in this scenario is to add `direnv` related files to your `.gitignore`:

```
$ git ignore direnv >> .gitignore

# Created by https://www.toptal.com/developers/gitignore/api/direnv
# Edit at https://www.toptal.com/developers/gitignore?templates=direnv

### direnv ###
.direnv
.envrc

# End of https://www.toptal.com/developers/gitignore/api/direnv
```

### Other use cases?

I don't have other real use cases to share because only recently I became familiarized with `direnv`. That said, the [direnv docs](https://direnv.net/man/direnv-stdlib.1.html) are very comprehensive of its full potential usage.

Some use cases that I like:

`dotenv`
: Automatically sources `.env` (note: not to confuse with `.envrc`) files, which are widely common in projects managed with `docker-compose`.

`source_env` + `env_vars_required`
: Alongside `.gitignore`, this is a great way to source secrets (e.g. API keys or tokens) and not accidentally check them into your repository.

`fetchurl`
: `bash | curl` is a cancer[^curlpipesh] that should arguably be stopped due to its inherent security risks. That said, `direnv` provides a safer way to work with it because you can specify a hash to ensure you're downloading the same script - if an attacker or malicious actor modified it, direnv would throw an error.

`path_add`
: If your project outputs to e.g. `build/<...>/bin` or similar (typical in `cmake` projects and AFAIK in Rust ones too), you could add that directory to your `PATH` so that you could easily execute your binaries, without having to write the full subdirectory path each time.

`layout`
: Besides python, `direnv` supports several other programming languages out-of-the-box. Popular examples include `go`, `nix`, `node`, `perl` and `ruby`.

## Downsides?

One could call `direnv` bloated because of all of the aforementioned capabilities. If it doesn't spark joy for your taste, consider using [autoenv](https://github.com/hyperupcall/autoenv) which is basically a leaner version of `direnv`, meant mostly for doing one thing and doing it well: setting and unsetting variables.

Other than that, `direnv` is pretty much a great piece of software.

One thing I didn't cover is how secure it is: You need to run `direnv allow` explicitly in order to tell `direnv` that you trust a given `.envrc` file. If you don't do it, `direnv` will refuse to source it:

```shell
$ touch .envrc
direnv: error ~/projects/foo/.envrc is blocked. Run `direnv allow` to approve its content
```

If you run `direnv allow` but later on the file is modified (for example, after `git pull`, whereby you retrieve a modification from a teammate), `direnv` will once again refuse to operate. You'll need to whitelist it again by re-running `direnv allow`. Direnv will snapshot/hash the file contents of `.envrc` remember it across sessions.

## References

- [Tools You Should Know About: direnv](https://cuddly-octo-palm-tree.com/posts/2021-12-12-tyska-direnv/)

[direnv]: https://direnv.net/
[direnv-github]: https://github.com/direnv/direnv
[repology]: https://repology.org/
[repology-direnv]: https://repology.org/project/direnv/badges
[chromium-bugtracker]: https://bugs.chromium.org/p/chromium/issues/list

[drew]: https://drewdevault.com/2021/11/16/Python-stop-screwing-distros-over.html

[^foss]: Obviously the aforementioned list was non-exhaustive. There are a few other questions that you may want to ask, out of scope of this article, such as: (i) does the project have an OSS or FLOSS license? (ii) does the project depend on Java?
[^aoc]: Advent of code challenges are released one by one, thereby forcing you to wait until the next day in order to get the next challenge.
[^shells]: more on this another day
[^curlpipesh]: c.f. https://curlpipesh.tumblr.com/, https://gnu.moe/wallofshame.md
