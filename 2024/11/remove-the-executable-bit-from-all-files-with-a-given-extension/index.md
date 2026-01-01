
To illustrate, consider TypeScript files (`*.ts`).

Run:

```shell
% fd -e .ts -x chmod -x
```

References:

- `fd`: `find` on steroids: https://github.com/sharkdp/fd
- `-x`: execute the given command on all matched files

You could also use classic `find`:

```shell
% find . -type f -name '*.ts' -exec chmod -x {} \;
```

Or:

```shell
% find . -type f -name '*.ts' | xargs chmod -x
```

Or, with more ~~style~~ safety:

```shell
% find . -type f -name '*.ts' -print0 | xargs -0 -n 1 chmod -x
```

