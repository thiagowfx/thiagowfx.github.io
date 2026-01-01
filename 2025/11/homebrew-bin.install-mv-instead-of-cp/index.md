
LLM:

> Unlike `bin.install` in Homebrew (which moves files by default if not given a
> hash), `install` (the Unix command) copies files. It does not consume the
> source file.

Why would you design
[`bin.install`](https://docs.brew.sh/Formula-Cookbook#bininstall-foo) like
this??!

> You'll see stuff like this in some formulae. This moves the file foo into the
> formula's bin directory (/opt/homebrew/Cellar/pkg/0.1/bin) and makes it
> executable (chmod 0555 foo). Variables for the most common directory locations
> are available.

This breaks Unix tradition! `install -> copy`.

