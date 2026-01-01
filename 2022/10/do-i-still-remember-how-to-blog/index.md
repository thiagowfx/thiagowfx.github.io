
I haven't written a blog post for a couple of months now, which is a good indicator I should probably document my workflow before I forget how to do it...

First, `git clone --recurse https://github.com/thiagowfx/thiagowfx.github.io/`.
I like to store it in `~/Projects/`.

To create a new post, `hugo new content/posts/2022-10-09-title-comes-here.md`.

Use either `vim` or `textmate` to draft the post. Choose one or more tags,
trying to reuse existing ones whenever possible. When using `vim`, use `Q` to
reformat paragraphs.

To preview the post locally, run `make run` and then open http://localhost:1313/.

If everything looks good, `git commit` and `git push`. GitHub CI will then
publish the post to [GitHub Pages](https://pages.github.com/) in a couple of
seconds.

To blog on the go, use https://github.dev/. I documented this setup earlier,
[here]({{< ref "2022-02-18-hugo-compose-or-edit-blog-posts-from-the-web"
>}}).

