
Assume you make a huge change to your git repository, that spawns several file
formats – cpp, java, javascript, python, etc.

In the end you want to revert the javascript changes, for the sake of splitting
your commit into self-contained chunks[^1].

I like the following approach[^2]:

```shell
% git checkout -- **/*.js
```

**Caveat**: It does not include hidden files, or files in hidden directories.
Unless...you set the `dotglob` option:

```shell
% shopt -s dotglob
```

Note that `shopt` works in `bash`, alas not in `zsh`.

[^1]: https://sscce.org/
[^2]: In theory, this is a pre-requisite: `shopt -s globstar`. In practice, it
    should be the default behavior.

