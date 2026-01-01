
When working on Python projects, [`pyenv`](https://github.com/pyenv/pyenv) is a
great python environment / version manager, especially on macOS wherein you
cannot easily control the python system version.

I'd recommend to install it with homebrew (`brew install pyenv`).

The upstream documentation is great. The commands you'll typically use are:

- `pyenv versions`: list all installed versions
- `pyenv global <version>`: set a specific python version for your whole system
- `pyenv local`: set a specific python version only for a specific project
  (directory)

And then it's handy to add the following blurb to your shell rc file to make
`pyenv` work properly out-of-the-box:

```shell
# pyenv: https://github.com/pyenv/pyenv
if hash pyenv >/dev/null 2>&1; then
	export PYENV_ROOT="$HOME/.pyenv"
	path_munge "$PYENV_ROOT/bin"
	eval "$(pyenv init -)"
fi
```

Note that `path_munge` is a custom function, it merely appends the given
argument to the `$PATH`.

