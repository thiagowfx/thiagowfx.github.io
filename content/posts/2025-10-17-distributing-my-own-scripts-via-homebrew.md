---
title: "Distributing my own scripts via homebrew"
date: 2025-10-17T16:38:40+02:00
tags:
  - bestof
  - dev
---

Thanks [Justin
Searls](https://justin.searls.co/posts/how-to-distribute-your-own-scripts-via-homebrew/)
for the idea:

> I use Homebrew all the time. Whenever I see a new CLI that offers an npm or uv
> install path alongside a brew one, I choose brew every single time.

Me too.

> And yet, when it comes time to publish a CLI of my own, I usually just ship it
> as a Ruby gem or an npm package, because I had (and have!) no fucking clue how
> Homebrew works. I'm not enough of a neckbeard to peer behind the curtain as
> soon as root directories like /usr and /opt are involved, so I never bothered
> before today.

I understand how package managers work, and I'm even a package maintainer in
Alpine Linux and Arch Linux, but until now I never bothered to package my own
projects for others to consume.

Previously I talked about my new [pancake]({{< ref "2025-09-25-pancake-potpourri-scripts" >}}) repository. It consists of miscellaneous self-contained executables. As such, it is a great candidate for packaging.

I won't submit it to upstream homebrew because it is overly specific, but that
doesn't prevent me from packaging it in a [standalone
repository](https://docs.brew.sh/Taps).

In order to do so, I simply created a `pancake.rb` [Formula](https://github.com/thiagowfx/pancake/blob/1a58c53e3984b0a0b34b750a73dab793aff5ebe5/Formula/pancake.rb):

```ruby
class Pancake < Formula
  desc "A collection of useful shell scripts"
  homepage "https://github.com/thiagowfx/pancake"
  head "https://github.com/thiagowfx/pancake.git"

  def install
    # keep-sorted start
    bin.install "aws_china_mfa/aws_china_mfa.sh" => "aws_china_mfa"
    bin.install "op_login_all/op_login_all.sh" => "op_login_all"
    bin.install "pritunl_login/pritunl_login.sh" => "pritunl_login"
    bin.install "sd_world/sd_world.sh" => "sd_world"
    # keep-sorted end
  end

  test do
    # Basic test to ensure the scripts are installed and executable.
    # keep-sorted start
    assert_predicate bin/"aws_china_mfa", :executable?
    assert_predicate bin/"aws_china_mfa", :exist?
    assert_predicate bin/"op_login_all", :executable?
    assert_predicate bin/"op_login_all", :exist?
    assert_predicate bin/"pritunl_login", :executable?
    assert_predicate bin/"pritunl_login", :exist?
    assert_predicate bin/"sd_world", :executable?
    assert_predicate bin/"sd_world", :exist?
    # keep-sorted end
  end
end
```

To install it, first tap the repository[^1]:

```shell
% brew tap thiagowfx/pancake https://github.com/thiagowfx/pancake.git
```

Then install it, from `HEAD` because it is not currently versioned:

```shell
% brew install --HEAD pancake
```

List all package contents:

```shell
% brew ls pancake
/opt/homebrew/Cellar/pancake/HEAD-1a58c53/bin/aws_china_mfa
/opt/homebrew/Cellar/pancake/HEAD-1a58c53/bin/op_login_all
/opt/homebrew/Cellar/pancake/HEAD-1a58c53/bin/pritunl_login
/opt/homebrew/Cellar/pancake/HEAD-1a58c53/bin/sd_world
/opt/homebrew/Cellar/pancake/HEAD-1a58c53/sbom.spdx.json
```

There's no need to fiddle with `$PATH`, as this is already handled by homebrew:

```shell
% which aws_china_mfa
/opt/homebrew/bin/aws_china_mfa
% ls -al /opt/homebrew/bin/aws_china_mfa
lrwxr-xr-x@ - thiago.perrotta 13 Oct 14:43 /opt/homebrew/bin/aws_china_mfa -> ../Cellar/pancake/HEAD-1a58c53/bin/aws_china_mfa*
```

[^1]: If this idea sticks, I intend to create a dedicated
    `thiagowfx/homebrew-pancake` repo, so that you can tap it with `brew tap
    thiagowfx/pancake`, without the need of specifying the full repository URL
    as per
    [docs](https://docs.brew.sh/Taps#repository-naming-conventions-and-assumptions).
    For now though, the formula is hosted in the same repository as the
    executables.
