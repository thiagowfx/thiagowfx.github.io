
I'm not sure if this is well-known, so here's a short anecdotal blog post:

`git` cannot track empty directories.

I wanted to add a `drafts/` folder to my blog repository, alongside a
`.gitignore` containing `drafts/*.md` so that my staging posts wouldn't be
accidentally checked into version control.

If `drafts/` is supposed to be empty, then how can I check it into version
control?

The [answer](https://stackoverflow.com/a/7229996/1745064) is to create a dummy
`.gitkeep` file inside it with `touch drafts/.gitkeep`. This way I can
[push](https://github.com/thiagowfx/thiagowfx.github.io/tree/master/drafts) the
`drafts/` directory to VCS. And it will remain empty (of markdown files)!

