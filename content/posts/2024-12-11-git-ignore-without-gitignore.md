---
title: ".gitignore without .gitignore"
date: 2024-12-11T11:44:12-03:00
tags:
  - bestof★
  - dev
---

`.gitignore` is the canonical way to exclude files from your git repository.

In some situations, however, you may want to exclude files without adding them
to `.gitignore`, because they are only relevant to you, as opposed to your
teammates.

Common examples:

- `.ackrc`: exclude file patterns from search with `ack` – not everyone in your
  team may use `ack` at all
- `.envrc`: `direnv` integration to automatically run a couple of commands
  whenever `cd`'ing to within the repository – not everyone in your team may use
  `direnv` at all

...and so on.


Is there a way to have a "personal" `.gitignore` file? Yes, in fact, many ways!

## 1) Per repository

Use the `.git/info/exclude` file instead of `.gitignore`. Edits in this file are
not tracked by version control. The documentation says:

```
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~
.ackrc
.envrc
```

For example, I could add `.ackrc` to it.

## 2) `git update-index`

```shell
% git update-index --assume-unchanged .ackrc .envrc
```

If you make a mistake, it can be reversed with `--no-assume-unchanged`.

## 3) Globally

This approach takes effect in _all_ repositories.

Set [`core.excludesFile`](https://git-scm.com/docs/gitignore#_configuration) in
your `~/.gitconfig`:

```shell
git config --global core.excludesFile '~/.gitignore'
```

Now populate it as you normally would your repo `.gitignore`.

## References

- https://stackoverflow.com/questions/653454/how-do-you-make-git-ignore-files-without-using-gitignore
- https://gist.github.com/subfuzion/db7f57fff2fb6998a16c
