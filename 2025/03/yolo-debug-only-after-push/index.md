
Whenever writing new posts in this blog I rarely preview them in advance,
especially when they are short and simple[^1].

My rushed workflow is roughly:

- open a new terminal tab / window
- `cd ~blog`
- `just new "hello world"`
- `vim content/posts`, hit 'G', hit 'k', hit 'ENTER'
- draft the post
- `:Gwq` ([vim-fugitive](https://github.com/tpope/vim-fugitive), `git`
  integration)
- `git commit -m "new post: hello world"`
- `git push`

_ONLY then_, `just`, open web browser, see if it looks OK.

Does it _NOT_ look OK (grammar errors, markdown issues, typos)? Make a quick
edit, `:Gwq` again, `git amend && git push -f`.

Normally this process happens faster than the CI pipeline takes to build and
subsequently publish the site.

No AI involved™, not even a spellchecker[^2].

[^1]: Which is what I strive for most of the time anyways.

[^2]: Not completely true:
    [`codespell`](https://github.com/codespell-project/codespell) is integrated
    via [pre-commit](https://pre-commit.com/). `vim` has `:set spell`. That's
    all though. There's no "make this sound better" or "rewrite this more
    professionally". What you read is what comes straight off my brain.

