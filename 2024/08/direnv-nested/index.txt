
I covered [`direnv`]({{< ref "2022-01-04-direnv-automate-your-environment-variables" >}}) before.

**New scenario**: Given a directory structure with two nested `.envrc`s:

```
% tree -a top
top
├── .envrc
└── inner
    └── .envrc
```

It turns out that, surprisingly, `cd top/inner` will load _only_
`top/inner/.envrc`. The top-level `top/.envrc` will _not_ be automatically
loaded.

This is intentional, meant for security reasons.

In order to source the parent `.envrc`, add `source_up` to the inner one.

Alternatively, `source_env ..` also works. I prefer `source_up`.

There's also `source_up_if_exists`, which works gracefully even if there's
no env file to source upwards.

The full list of built-in functions is available here:
https://direnv.net/man/direnv-stdlib.1.html

**Reference**: https://github.com/direnv/direnv/issues/757

**Use Case**: Add top-level environment variables to `top/.envrc`. Add `layout`
to `top/inner/.envrc`. For example, perhaps `inner` is a custom `git` repository
/ project.

