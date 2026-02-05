
Symptom:

```
❯ pre-commit run -a
[INFO] Installing environment for https://github.com/rbubley/mirrors-prettier.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
An unexpected error has occurred: CalledProcessError: command: ('/Users/thiago.perrotta/.cache/pre-commit/repo78y8p1fk/node_env-system/bin/node', '/opt/homebrew/bin/npm', 'install', '-g', '/Users/thiago.perrotta/.cache/pre-commit/repo78y8p1fk/placeholder_package-0.0.0.tgz', 'prettier@3.8.1')
return code: 1
stdout: (none)
stderr:
    npm error code EBADF
    npm error errno EBADF
    npm error request to https://registry.npmjs.org/prettier failed, reason:
    npm error A complete log of this run can be found in: /Users/thiago.perrotta/.npm/_logs/2026-02-04T12_22_05_104Z-debug-0.log
Check the log at /Users/thiago.perrotta/.cache/pre-commit/pre-commit.log
```

Initially I thought it was an issue with `prettier`. The pre-commit repository
is deprecated after all:

> This is a fork of the (now archived)
> https://github.com/pre-commit/mirrors-prettier with the only difference being
> that it only references release versions of prettier, not e.g. alpha/beta
> versions.

The actual error was [Little
Snitch](https://www.obdev.at/products/littlesnitch/index.html) on macOS blocking
all outgoing connections to the NPM registry.

How to address it?

- Click "Manage Rules..."
- Click "Deny" to list all network blocks
- Delete the NPM registry entry

