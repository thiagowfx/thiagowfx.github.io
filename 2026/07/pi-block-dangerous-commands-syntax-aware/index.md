---
title: "pi: block dangerous commands syntax-aware"
url: https://perrotta.dev/2026/07/pi-block-dangerous-commands-syntax-aware/
last_updated: 2026-07-28
---


**Problem statement**: block destructive shell commands issued by
[pi](https://pi.dev/) without resorting to grepping shell source with regular
expressions.

My first guard was a direct port of an older hook in Claude Code:

```typescript
const BLOCKED_COMMANDS: ReadonlyArray<{ pattern: RegExp; reason: string }> = [
  { pattern: /terraform\s+apply/, reason: "terraform apply is blocked - use terraform plan first" },
  { pattern: /terraform\s+destroy/, reason: "terraform destroy is blocked for safety" },
  { pattern: /git\s+reset\s+.*--hard/, reason: "git reset --hard is blocked - discards changes irreversibly" },
];

const blocked = BLOCKED_COMMANDS.find(({ pattern }) => pattern.test(command));
```

This matched harmless strings such as `echo 'terraform destroy'`, while shell
quoting, wrappers, substitutions, and reordered options kept opening holes.
Regexes aren't robust in this context.

Enter ASTs! Shell source could leverage a shell parser.

I switched the extension to the Bash grammar from
[`tree-sitter-bash`](https://github.com/tree-sitter/tree-sitter-bash), loaded
through the WASM Tree-sitter runtime:

```typescript
await Parser.init();
const languagePath = require.resolve("tree-sitter-bash/tree-sitter-bash.wasm");
const language = await Language.load(languagePath);
return new Parser().setLanguage(language);
```

[Tree sitter](https://tree-sitter.github.io/) is an amazing parser.

The policy now works on executable names and arguments:

```typescript
if (executable === "rm") {
  const recursive = staticArguments.some(
    (argument) => argument === "--recursive" || hasShortOption(argument, "r") || hasShortOption(argument, "R"),
  );
  const force = staticArguments.some(
    (argument) => argument === "--force" || hasShortOption(argument, "f"),
  );
  if (recursive && force) return { command, reason: "rm -rf is blocked for safety" };
}
```

The AST walker also follows command substitutions, heredocs, `bash -c`, `eval`,
`find -exec`, `xargs`, and common wrappers. Comments and quoted data remain data.
Malformed syntax and dynamic guarded arguments fail closed.

```text
ℹ tests 48
ℹ suites 0
ℹ pass 48
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
```

Local extensions do not get npm dependencies installed by Pi. I kept `index.ts`
dependency-free: on first load it checks for the parser files, runs a pinned
installation when needed, then imports the real guard.

```typescript
const result = await pi.exec("npm", ["ci", "--ignore-scripts"], {
  cwd: extensionDirectory,
  timeout: 120_000,
});

const { default: dangerousCommandGuard } = await import("./guard.ts");
await dangerousCommandGuard(pi);
```

Finally, testing the real tool call:

```shell
% rm -rf /tmp/foo
rm -rf is blocked for safety
% test -f /tmp/foo/marker && cat /tmp/foo/marker
guard-test
```

The guard blocked the command; `/tmp/foo/marker` survived.

The source lives in my [dotfiles](https://github.com/thiagowfx/.dotfiles/tree/d917c6b98e8107490bea92367c89d1b05e1de89b/pi/.pi/agent/extensions/dangerous-command-guard).

- - -

🤖 *Drafted with `/bloggify`.*

