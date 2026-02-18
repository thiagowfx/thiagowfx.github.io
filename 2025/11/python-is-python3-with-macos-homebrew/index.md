
I face this annoyance all the time:

```
thiago@thiagoperrotta-MacBook-Pro ~
% python
zsh: command not found: python
127 thiago@thiagoperrotta-MacBook-Pro ~
% python3
Python 3.14.0 (main, Oct  7 2025, 09:34:52) [Clang 17.0.0 (clang-1700.0.13.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `python` executable is not available on macOS natively.

It is not available on homebrew either, even with `brew install python`.

`python3` is there though:

```
% which -a python3
/opt/homebrew/bin/python3
/usr/bin/python3
```

I want to be able to run `python` without having to remember I am running
Python 3. Python 3 is the _de facto standard_ in the 2020s, there should be no
need to remember this explicitly, we take it as gospel already.

There are various ways to resolve this:

```shell
alias python=python3
```

Classic. I hate it. Now you'll have a `python` alias even if `python3` is not
available. This is not elegant at all. You could make it a bit better, sure:

```shell
command -v python3 >/dev/null 2>&1 && alias python=python3
```

Or even a bit more idiomatically if using `zsh`:

```shell
(( $+commands[python3] )) && alias python=python3
```

Still, this is not a problem the shell should own. It just _feels_ wrong. This
is a package management problem. The shell remedy is just a cheap band-aid.
Can we do better than this?

What about a wrapper script in `/usr/local/bin`?

```shell
#!/usr/bin/env bash
exec python3 "$@"
```

This is better. Much better. However, why not make it even simpler?

```shell
% sudo ln -s /usr/bin/python3 /usr/local/bin/python
```

A symlink suffices. You just need to decide whether to point it out to `python3`
in homebrew or in the system.

A symlink is not reproducible[^1] though. If you reinstall your system, or acquire a
new one, now you'll have to remember to re-create it.

Sure, you could script it in your .dotfiles installation script, or add it to
the system installation notes section in your second brain app. Who am I to tell
you what to do?

Here is my favorite way to address the issue: install a package!

For example, there was a time in Debian and Ubuntu that the
[`python-is-python3`](https://packages.debian.org/sid/python-is-python3) package
did exactly that:

> This is a convenience package which ships a symlink to point the
> /usr/bin/python interpreter at the current default python3. It may improve
> compatibility with other modern systems, whilst breaking some obsolete or
> 3rd-party software.

Now you can guess what the source of my inspiration was. I created a homebrew
formula to do the same:

```ruby
class PythonIsPython3 < Formula
  desc "Make python point to python3"
  homepage "https://github.com/thiagowfx/homebrew-taps"
  url "file:///dev/null"
  version "1.0"
  sha256 "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

  depends_on "python"

  def install
    bin.install_symlink Formula["python"].opt_bin/"python3" => "python"
    bin.install_symlink Formula["python"].opt_bin/"pip3" => "pip"
  end
end
```

And now that I have a formula, I need to create a tap to host it somewhere.

Hence https://github.com/thiagowfx/homebrew-taps is born.

To install it:

```shell
brew tap thiagowfx/taps
brew install python-is-python3
```

Enjoy peace!

```shell
% which python
/opt/homebrew/bin/python
```

[^1]: This is a very loose usage of "reproducible". Sorry Nix folks, I meant no
    harm!

