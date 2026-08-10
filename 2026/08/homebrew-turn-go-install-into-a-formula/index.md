---
title: "homebrew: turn go install into a formula"
url: https://perrotta.dev/2026/08/homebrew-turn-go-install-into-a-formula/
last_updated: 2026-08-10
---


[Previously]({{< ref "2025-10-17-distributing-my-own-scripts-via-homebrew" >}}).

**Problem statement**: [meat](https://meat.dev/) only documents a `go install`
command, but I want Homebrew to manage it[^1].

[^1]: In 2026 there's no excuse to ship software with `go install`. It feels
    sloppy, unless it's a prototype or an experimental project. Creating a
    package is trivial, even without LLMs.

The existing installation lived under `$GOPATH`:

```shell
% go install meat.dev/cmd/meat@latest
% which meat
/Users/thiago.perrotta/go/bin/meat
```

There are no tags or releases. `@latest` currently resolves to a Go
pseudo-version:

```shell
% go list -m -json meat.dev@latest
{
        "Path": "meat.dev",
        "Version": "v0.0.0-20260803201634-f39f41dfe7b5",
        "Query": "latest",
        "Time": "2026-08-03T20:16:34Z",
        "Dir": "/Users/thiago.perrotta/go/pkg/mod/meat.dev@v0.0.0-20260803201634-f39f41dfe7b5",
        "GoMod": "/Users/thiago.perrotta/go/pkg/mod/cache/download/meat.dev/@v/v0.0.0-20260803201634-f39f41dfe7b5.mod",
        "GoVersion": "1.24.13"
}
```

The pseudo-version gives us commit `f39f41dfe7b5`; the module's vanity import
page points at `github.com/boldsoftware/meat`. Hash its source archive:

```shell
% curl -LfsS https://github.com/boldsoftware/meat/archive/f39f41dfe7b5.tar.gz -o /tmp/meat.tar.gz
% shasum -a 256 /tmp/meat.tar.gz
faf4831aa3fa866168191b21414698f407f1d473c1572e4cc3942e2c595db6bd  /tmp/meat.tar.gz
```

We can do better. Let's create a homebrew package for it. [`Formula/meat.rb`](https://github.com/thiagowfx/homebrew-taps/blob/master/Formula/meat.rb):

```ruby
class Meat < Formula
  desc "Abridge code diffs into reading diffs"
  homepage "https://meat.dev"
  url "https://github.com/boldsoftware/meat/archive/f39f41dfe7b5b37a12b35fdfbaecc7e779855bd3.tar.gz"
  version "0.0.0-20260803201634-f39f41dfe7b5"
  sha256 "faf4831aa3fa866168191b21414698f407f1d473c1572e4cc3942e2c595db6bd"
  license "Apache-2.0"
  head "https://github.com/boldsoftware/meat.git", branch: "main"

  depends_on "go" => :build

  def install
    system "go", "build", *std_go_args, "./cmd/meat"
  end

  test do
    assert_match "abridge a diff", shell_output("#{bin}/meat --help 2>&1")
  end
end
```

[`std_go_args`](https://docs.brew.sh/Formula-Cookbook#standard-arguments) builds the requested package into Homebrew's `bin` directory. No
manual `GOBIN` or linker flags needed.

Replace the old binary and let Homebrew take over:

```shell
% rm ~/go/bin/meat
% brew install thiagowfx/taps/meat
==> Installing meat from thiagowfx/taps
==> go build ./cmd/meat
🍺  /opt/homebrew/Cellar/meat/0.0.0-20260803201634-f39f41dfe7b5: 6 files, 6.6MB, built in 2 seconds

% which meat
/opt/homebrew/bin/meat
% brew list --versions meat
meat 0.0.0-20260803201634-f39f41dfe7b5
```

Same binary, now owned by the package manager.

We can trivially uninstall it on-demand:

```shell
brew uninstall meat
```

