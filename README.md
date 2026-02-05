# not just serendipity

`> grep -Erl '\b(push|schedule|workflow_dispatch):$' .github/workflows | xargs -n 1 basename | sort -d | sed 's|^[^/]*$|[![&](https://github.com/thiagowfx/thiagowfx.github.io/actions/workflows/&/badge.svg)](https://github.com/thiagowfx/thiagowfx.github.io/actions/workflows/&)|'`

<!-- BEGIN mdsh -->
[![gh-pages.yml](https://github.com/thiagowfx/thiagowfx.github.io/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/thiagowfx/thiagowfx.github.io/actions/workflows/gh-pages.yml)
[![ls-lint.yml](https://github.com/thiagowfx/thiagowfx.github.io/actions/workflows/ls-lint.yml/badge.svg)](https://github.com/thiagowfx/thiagowfx.github.io/actions/workflows/ls-lint.yml)
[![prek-autoupdate.yml](https://github.com/thiagowfx/thiagowfx.github.io/actions/workflows/prek-autoupdate.yml/badge.svg)](https://github.com/thiagowfx/thiagowfx.github.io/actions/workflows/prek-autoupdate.yml)
[![prek.yml](https://github.com/thiagowfx/thiagowfx.github.io/actions/workflows/prek.yml/badge.svg)](https://github.com/thiagowfx/thiagowfx.github.io/actions/workflows/prek.yml)
<!-- END mdsh -->

This blog is built with [`hugo`][hugo].

## LICENSE

All blog posts located under the `content/` directory have a [CC BY-NC-SA
4.0][cc-by-nc-sa-4.0] license.

All other blog sources are governed by the BSD 3-Clause License, see `LICENSE`.

[cc-by-nc-sa-4.0]: https://creativecommons.org/licenses/by-nc-sa/4.0/
[hugo]: https://gohugo.io/
