
**Problem statement**: `npm test` does not automatically run `npm install`.

```
% npm test
> dns-changer@1.0.0 test
> node --no-warnings --experimental-vm-modules node_modules/.bin/jest

node:internal/modules/cjs/loader:1408
  throw err;
  ^

Error: Cannot find module 'er/aws/lambda/node_modules/.bin/jest'
    at Function._resolveFilename (node:internal/modules/cjs/loader:1405:15)
    at defaultResolveImpl (node:internal/modules/cjs/loader:1061:19)
    at resolveForCJSWithHooks (node:internal/modules/cjs/loader:1066:22)
    at Function._load (node:internal/modules/cjs/loader:1215:37)
    at TracingChannel.traceSync (node:diagnostics_channel:322:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:235:24)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:151:5)
    at node:internal/main/run_main_module:33:47 {
  code: 'MODULE_NOT_FOUND',
  requireStack: []
}

Node.js v23.10.0
```

We could address this with `npm install && npm test`[^1], but these are **two**
commands. We [_should_](https://datatracker.ietf.org/doc/html/rfc2119) be able
to do so with one shot.

Apparently there's [`npm
install-test`](https://docs.npmjs.com/cli/v7/commands/npm-install-test)[^2]. It does
exactly what you would expect. **This is the preferred solution**.

Alternatively (and this was going to be my final solution):

```
% cat package.json
{
  "scripts": {
    "pretest": "npm install",
    "test": "[...]"
  }
}
```

...then `npm test` would invoke `npm install` in advance.

[^1]: Or, even better, `npm ci && npm test`.

[^2]: There's no `npm ci-test`. Sorry to disappoint you.

