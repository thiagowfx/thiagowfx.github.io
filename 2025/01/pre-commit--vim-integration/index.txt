
Is it possible to transparently invoke `pre-commit` in the background upon saving in `vim` (`:w`)?

Initially I found this [Stack
Overflow](https://stackoverflow.com/questions/70713450/pre-commit-results-in-vim)
question, but it had no answer.

Digging a bit deeper I realized that I could do it with an `autocmd`:

```vim
autocmd BufWritePost * execute '! if [ -e $(git root)/.pre-commit-config.yaml >/dev/null 2>&1 ]; then pre-commit run; fi'
```

That trashes the screen upon completion. This can be resolved by invoking
`:redraw!` afterwards:

```vim
autocmd BufWritePost * execute '! if [ -e $(git root)/.pre-commit-config.yaml >/dev/null 2>&1 ]; then pre-commit run; fi' | redraw!
```

We can be less intrusive by prepending `silent!` so that, even if the command
fails, it doesn't get in the way:

```vim
autocmd BufWritePost * silent! execute '! if [ -e $(git root)/.pre-commit-config.yaml >/dev/null 2>&1 ]; then pre-commit run; fi' | redraw!
```

And last but not least, ideally `pre-commit` should run only on the file
associated with the current buffer. Pass `--files` to pre-commit with the `%`
argument:

```vim
autocmd BufWritePost * silent! execute '! if [ -e $(git root)/.pre-commit-config.yaml >/dev/null 2>&1 ]; then pre-commit run --files %; fi' | redraw!
```

This approach works as intended.
There's a brief period in which you can see `pre-commit` running in the
background. It's arguable whether that's a feature or a bug.

Ah, and `git root` is simply an alias in my `~/.gitconfig`:

```
root = rev-parse --show-toplevel
```

Whenever there are pre-commit violations (e.g. `end-of-file-fixer`) they are
applied inplace. There's no need to run `:e!`.

This is bare, but I am happy.

Perhaps the only missing piece is to extend it in such a way it's only executed
in the repositories I opt into.

If this turns out to be too intrusive, I am thinking to switch to using a vim
keymap e.g. `<leader>p` instead of an `autocmd`.

