
[`fpp`](https://github.com/facebook/PathPicker):

> PathPicker accepts a wide range of input -- output from git commands, grep
> results, searches -- pretty much anything. After parsing the input, PathPicker
> presents you with a nice UI to select which files you're interested in. After
> that you can open them in your favorite editor or execute arbitrary commands.

Think of `fpp` as the result of parsing file-looking paths in `stdout` and
injecting them into [`fzf`](https://github.com/junegunn/fzf).

It's part of my daily tool belt.

Sadly, the project is [somewhat
abandoned](https://github.com/facebook/PathPicker/commits/main/) since 2022.
Nonetheless, it doesn't need any new features: [it does one thing and does it
well](https://en.wikipedia.org/wiki/Unix_philosophy).

Its latest released version is
[0.9.5](https://github.com/facebook/PathPicker/releases/tag/0.9.5). Ironically,
due to a bug, there is a mismatch in `--version`:

```shell
% fpp --version
fpp version 0.9.2
```

A few usage examples:

- `git st | fpp`: modified files in a git repository
- `fd -e ts --type file | fpp`: files with a given extension
- `ack -l {pattern} | fpp`: files that match a given pattern

To continuously edit files in a loop, use `fpp -ko` (`ko` stands for
`--keep-open`).

