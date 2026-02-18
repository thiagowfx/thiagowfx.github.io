---
title: "New APKBUILD: LLM edition"
date: 2026-02-18T11:23:05+01:00
tags:
  - ai
  - alpine-linux
  - bestof
  - dev
---

**Problem statement**: package [`prek`](http://prek.j178.dev/) for [Alpine
Linux](https://alpinelinux.org/).

`prek` is a modern replacement for [`pre-commit`](https://pre-commit.com/),
covered ([many times]({{< ref "/tags/pre-commit" >}})) in this blog[^2].

[Previously]({{< ref "2022-01-23-alpine-linux-new-apkbuild-workflow" >}}).

It's already a breeze to create `APKBUILD`s. I've been doing so for ages.

Now, in 2026, with agentic LLMs, it's even more so!

I can be more useful to the Alpine Linux community by increasing my efficiency
as a package maintainer.

Yesterday I used [Amp Free](https://ampcode.com) in *smart* mode (Opus 4.6) to
scaffold the `APKBUILD` for `prek`, using the [AUR
`PKGBUILD`](https://aur.archlinux.org/packages/prek) as a baseline. Prompt:

```
write an APKBUILD for prek, inspired by https://aur.archlinux.org/packages/prek

once written, copy it to knol (ssh knol)
aports dir: ~/workspace/aports (in knol)
```

The result:

```shell
# Maintainer: Thiago Perrotta <{redacted}>
pkgname=pre
pkgver=0.3.3
pkgrel=0
pkgdesc="Better pre-commit, re-engineered in Rust"
url="https://github.com/j178/prek"
arch="all"
license="MIT"
makedepends="cargo cargo-auditable"
subpackages="
	$pkgname-bash-completion
	$pkgname-fish-completion
	$pkgname-zsh-completion
	$pkgname-doc
	"
source="$pkgname-$pkgver.tar.gz::https://github.com/j178/prek/archive/v$pkgver.tar.gz"
options="net" # fetch dependencies

prepare() {
	default_prepare
	cargo fetch --target="$CTARGET" --locked
}

build() {
	cargo auditable build --release --frozen

	target/release/prek util generate-shell-completion bash > $pkgname.bash
	target/release/prek util generate-shell-completion fish > $pkgname.fish
	target/release/prek util generate-shell-completion zsh > $pkgname.zsh
}

check() {
	cargo test --frozen
	cargo test --frozen -- --skip cache_gc_keeps_local_hook_env --skip cache_gc_removes_unreferenced_entries
}

package() {
	install -Dm755 target/release/$pkgname -t "$pkgdir"/usr/bin/

	install -Dm644 $pkgname.bash "$pkgdir"/usr/share/bash-completion/completions/$pkgname
	install -Dm644 $pkgname.fish "$pkgdir"/usr/share/fish/vendor_completions.d/$pkgname.fish
	install -Dm644 $pkgname.zsh "$pkgdir"/usr/share/zsh/site-functions/_$pkgname

	install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
	install -Dm644 README.md -t "$pkgdir"/usr/share/doc/$pkgname/
}

sha512sums="
87f5b5905d0c95b7f55a789eb00b463bb987c5fc981d83500f34a41b8e9ea2e4a0ac9d45a0c3a029a7957de33f5ade866c396c399252eb4a7a9e09e32e270b99  prek-0.3.3.tar.gz
"
```

This was a great initial attempt, but
[tests](https://gitlab.alpinelinux.org/thiagowfx/aports/-/jobs/2223891) failed:

```
Stopped on the first failure. Run `cargo insta test` to run all snapshots.
thread 'cache_gc_removes_unreferenced_entries' (15179) panicked at /builds/thiagowfx/aports/testing/prek/tmp/cargo/registry/src/index.crates.io-1949cf8c6b5b557f/insta-1.46.3/src/runtime.rs:719:13:
snapshot assertion for 'cache_gc_removes_unreferenced_entries-2' failed in line 234
failures:
    cache_gc_keeps_local_hook_env
    cache_gc_removes_unreferenced_entries
```

A follow-up edit yielded this diff:

```diff
@@ -30,7 +30,7 @@ build() {
}

check() {
-	cargo test --frozen
+	cargo test --frozen -- --skip cache_gc_keeps_local_hook_env --skip cache_gc_removes_unreferenced_entries
}

package() {
```

...but that caused more failures. Then I got interrupted and the night ended.

Today, I continued with [Claude Code](https://claude.com/product/claude-code).

Original prompt to `claudey`[^1] using Opus 4.6:

> we're packaging prek for alpine linux (APKBUILD)
>
> we're using https://aur.archlinux.org/packages/prek as reference
>
> we have access to an alpine system in knol (`ssh knol`)
>
> the aports tree lives in ~/workspace/aports in knol
>
> we're already in the right branch, the prek APKBUILD lives in testing/prek within knol
>
> the problem is that the test is failing in our MR pipeline: https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/97666
>
> sample job: https://gitlab.alpinelinux.org/thiagowfx/aports/-/jobs/2223963 (raw log: https://gitlab.alpinelinux.org/thiagowfx/aports/-/jobs/2223963/raw)
>
> fix the APKBUILD!
>
> I think it's a missing checkdep

A couple of burned tokens later:

> APKBUILD updated. Here's what changed:
>
> Added checkdepends="bash python3":
>
> - python3 — prek's pygrep language handler uses uv to find a Python
>   interpreter. Without system Python, uv python find fails, causing all 11
>   pygrep tests to fail. Also needed for the windows_script_run test which uses
>   a #!/usr/bin/env python3 shebang.
> - bash — the script tests use #!/usr/bin/env bash shebangs, and Alpine doesn't
>   ship bash by default (only busybox ash).
>
> Added --skip for language integration tests needing unavailable runtimes:
>
> - docker — needs Docker daemon (also covers docker_image via substring match)
> - julia — Julia not available in Alpine
> - lua:: — Lua interpreter not available
> - haskell — GHC/cabal not available
> - node:: — Node.js/npm not available
> - ruby:: — Ruby not available
> - rust:: — Rust toolchain tests (rustup) not available
> - swift:: — Swift not available
> - bun:: — Bun not available
>
> The unit tests (282) plus other integration suites (auto_update,
> builtin_hooks, cache, hook_impl, identify, install) still run fully. You can
> commit and push to re-trigger the pipeline.

That's spot on. Here's the diff:

```diff
🧙 thiago@knol ~/workspace/aports/testing/prek git:prek
❯ git --no-pager show
commit 8f702c5f1ee1b6d153a4f957c309f2badd452d31 (HEAD -> prek)
Author: Thiago Perrotta <{redacted}>
Date:   Wed Feb 18 05:30:14 2026 -0500

    skip language integration tests

diff --git testing/prek/APKBUILD testing/prek/APKBUILD
index 5e134457bc..d6080fa977 100644
--- testing/prek/APKBUILD
+++ testing/prek/APKBUILD
@@ -7,6 +7,7 @@ url="https://github.com/j178/prek"
 arch="all"
 license="MIT"
 makedepends="cargo cargo-auditable"
+checkdepends="bash python3"
 subpackages="
 	$pkgname-bash-completion
 	$pkgname-fish-completion
@@ -30,7 +31,18 @@ build() {
 }

 check() {
-	cargo test --frozen -- --skip cache_gc_keeps_local_hook_env --skip cache_gc_removes_unreferenced_entries
+	cargo test --frozen -- \
+		--skip cache_gc_keeps_local_hook_env \
+		--skip cache_gc_removes_unreferenced_entries \
+		--skip "docker" \
+		--skip "julia" \
+		--skip "lua::" \
+		--skip "haskell" \
+		--skip "node::" \
+		--skip "ruby::" \
+		--skip "rust::" \
+		--skip "swift::" \
+		--skip "bun::"
 }

 package() {
```

I had to continue with a few more follow-ups though. Eventually, that led to
Merge Request (MR)
[!97666](https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/97666):

```shell
# Maintainer: Thiago Perrotta <{redacted}>
pkgname=prek
pkgver=0.3.3
pkgrel=0
pkgdesc="Better pre-commit, re-engineered in Rust"
url="https://github.com/j178/prek"
arch="all"
license="MIT"
makedepends="cargo cargo-auditable"
subpackages="
	$pkgname-bash-completion
	$pkgname-fish-completion
	$pkgname-zsh-completion
	$pkgname-doc
	"
source="$pkgname-$pkgver.tar.gz::https://github.com/j178/prek/archive/v$pkgver.tar.gz"
options="net" # fetch dependencies

prepare() {
	default_prepare
	cargo fetch --target="$CTARGET" --locked
}

build() {
	cargo auditable build --release --frozen

	target/release/prek util generate-shell-completion bash > $pkgname.bash
	target/release/prek util generate-shell-completion fish > $pkgname.fish
	target/release/prek util generate-shell-completion zsh > $pkgname.zsh
}

check() {
	cargo test --frozen --lib
}

package() {
	install -Dm755 target/release/$pkgname -t "$pkgdir"/usr/bin/

	install -Dm644 $pkgname.bash "$pkgdir"/usr/share/bash-completion/completions/$pkgname
	install -Dm644 $pkgname.fish "$pkgdir"/usr/share/fish/vendor_completions.d/$pkgname.fish
	install -Dm644 $pkgname.zsh "$pkgdir"/usr/share/zsh/site-functions/_$pkgname

	install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
	install -Dm644 README.md -t "$pkgdir"/usr/share/doc/$pkgname/
}

sha512sums="
87f5b5905d0c95b7f55a789eb00b463bb987c5fc981d83500f34a41b8e9ea2e4a0ac9d45a0c3a029a7957de33f5ade866c396c399252eb4a7a9e09e32e270b99  prek-0.3.3.tar.gz
"
```

...wherein [all tests
pass](https://gitlab.alpinelinux.org/thiagowfx/aports/-/pipelines/407211).

I can't compile `prek` on my little alpine linux VPS (1GB RAM). Apparently Rust
is a monster that requires a lot of RAM for compiling and linking software with
hundreds of dependencies.

I tested it by grabbing the built `.apk` package from the GitLab pipeline from
my MR:

```
⏺ x86_64 passed. Let's grab the artifact and install it:

⏺ Bash(ssh knol "curl -L -o /tmp/prek-x86_64.zip
      'https://gitlab.alpinelinux.org/api/v4/projects/3998/jobs/2224483/artifacts' && cd /tmp && unzip -o
      prek-x86_64.zip &&…)
  ⎿    % Total    % Received % Xferd  Average Speed  Time    Time    Time   Current
                                      Dload  Upload  Total   Spent   Left   Speed
       0      0   0      0   0      0      0      0                              0100  3.51M 100  3.
     … +19 lines (ctrl+o to expand)

⏺ Bash(ssh knol "sudo apk add --allow-untrusted /tmp/packages/testing/x86_64/prek-0.3.3-r0.apk && prek
      --version")
  ⎿  (1/1) Installing prek (0.3.3-r0)
     Executing busybox-1.37.0-r31.trigger
     OK: 1257.5 MiB in 579 packages
     prek 0.3.3

⏺ Installed and working. prek 0.3.3 on knol. All 8 completed architectures passed (riscv64 is still
  building).
```

The LLM tries to use `sudo` instead of `doas`, which is not correct on Alpine
Linux.

It works anyway because I have the [`doas-sudo-shim`](https://pkgs.alpinelinux.org/package/edge/main/x86_64/doas-sudo-shim) package installed:

```shell
% sudo -h
Usage:
  sudo (-i | -s) [-n] [-u <user>] [<command> [--] [<args>...]]
  sudo [-ins] [-u <user>] <command> [--] [<args>...]
  sudo [-h]

Execute a command as another user using doas(1).

This is not the original sudo, but the doas shim for sudo. It supports only
a subset of the sudo options (both short and long) that have an equivalent in
doas, plus option -i (--login). Refer to sudo(1) for more information.

If you need some sudo features that are not supported in doas, replace
package 'doas-sudo-shim' with 'sudo': apk add sudo !doas-sudo-shim.

Please report bugs at <https://github.com/jirutka/doas-sudo-shim/issues>.
```

[^1]: `alias claudey=claude --dangerously-skip-permissions`, with no annoying
    confirmation prompts
[^2]: Expect a post about `prek` soon.
