---
title: "(Google) Chrome for Testing: reliable downloads for browser automation"
date: 2024-01-25T18:27:04-03:00
tags:
  - bestof
  - dev
---

Let's discuss the _raison d'etre_ of [Google Chrome for
Testing](https://developer.chrome.com/blog/chrome-for-testing), a project I was
the Tech Lead of during my tenure on the Chrome Tooling / Browser Automation team
at Google.

[Once upon a time, a few (debugging) mistakes
ago](https://www.youtube.com/watch?v=9y4A15WCGdc), web developers would run
(web) integration tests with [WebDriver
Classic](https://www.w3.org/TR/webdriver2/) using Google Chrome (or Chromium)[^1].
This was a [chaotic
era](https://three-body-problem.fandom.com/wiki/Chaotic_Era).

_"Why?"_, you may rightfully ask.

- The web browser and/or its components / extensions / etc could
  **auto-update** in-between successive test runs, yielding different test
  results, i.e. tests were not guaranteed to be hermetic / deterministic due to
  their (potentially) changing environment, yielding test flakiness
- Chrome adds an **info bar** whenever it is controlled in an automated
  fashion, which changes the CSS viewport, resulting in changes compared to a
  production environment. For example: an automated test that takes a
  screenshot would have a slightly smaller height whenever an infobar is
  present.
- There are no versioned Chrome builds for download. There's no **browser
  pinning**. As a developer you always download the latest version. This makes
  it hard to reason about invariants, especially when new browser versions
  introduce breaking changes, even seemingly small ones.
  - **Corollary**: The lack of versioned Chrome builds makes it hard to obtain
    a corresponding (matching)
    [Chromedriver](https://chromedriver.chromium.org/downloads) version for
    Chrome. The mismatch (delta) could provoke testing inconsistencies whenever
    browser APIs diverge[^3].

In order to address these (and other) issues, [Chrome for
Testing](https://goo.gle/chrome-for-testing) (hereafter "CfT") was born. To
clarify, today where are three flavours of Chrom*:

- **Chromium**: the open-source project, https://chromium.org/. The root of all
  derivatives (Microsoft Edge, Brave, etc). It is available in full source
  form, but there are no (official) pre-built binaries for it.
- **Google Chrome**: the proprietary, closed-source version of Chromium developed
  by Google. Think of it as Chromium on steroids. Google distributes pre-built
  Chrome binaries for every platform it supports.
- **Google Chrome for Testing**: think of it as "reproducible (or pinned, or
  frozen) Google Chrome". It is basically a snapshot of Google Chrome in a
  fixed time in the past, plus a few bits of developer-oriented features
  mentioned in this article.

There are other _niceties_ that Chrome for Testing accomplishes as of today:

- The [CDP (Chrome DevTools
  Protocol)](https://chromedevtools.github.io/devtools-protocol/) experiment
  ("Protocol Monitor") is enabled by default, out-of-the-box. This kind of
  experiment, which enriches your debugging toolbox, is exactly the sensible
  state you want during the development cycle.
- Mechanisms such as [self-XSS confirmation
  prompts](https://developer.chrome.com/blog/self-xss) are disabled by default,
  which is the desired behavior for automation. Consider an analogy with
  setting
  [`DEBIAN_FRONTEND=noninteractive`](https://askubuntu.com/questions/972516/debian-frontend-environment-variable)
  when running `apt` in dockerfiles. You don't want prompts (even benign ones)
  to suddenly get in the way of your tests and end up interrupting their
  execution flow.
- Completely agnostic to the concept of "Stable" / "Beta" / "Dev". If you have
  pinned versions, you don't need to care about any of that.
- CfT releases are made available alongside a subset of corresponding Google
  Chrome releases

Something important to note:

> **Warning**: Chrome for Testing has been created purely for browser
> automation and testing purposes, and is not suitable for daily browsing.

The main reason for that is the fact that it does not auto-update. You could
argue that it doesn't matter: Chrome for most linux distributions also does not
auto-update by itself. The updates are normally deferred to the distribution's
package manager (e.g. `apt`, `dnf`, `pacman`, etc). Why should it be different
for Chrome for Testing?

An additional point to consider here is that Chrome for Testing could have new
features in the future that would be optimized for developers, not for end
users. You don't want end users to shoot themselves on the foot, therefore it's
easier, better and safer to do a blanket anti-recommendation of CfT for
non-developers[^2].

Because of that, CfT cannot be made the default system browser.

The easiest way to obtain CfT is via its public API, which is documented here:
https://googlechromelabs.github.io/chrome-for-testing/, or through the official
[CLI utility](https://pptr.dev/browsers-api) that is part of Puppeteer.

Today, for all the reasons above (and more to come!), CfT is the de-facto
recommended solution for browser automation for all things web applications and
web platform testing. If you're currently using either Chromium or Google
Chrome for these purposes, you should switch to it.

## Bonus: How to run Chrome for Testing in CI?

The [chromium-bidi](https://github.com/GoogleChromeLabs/chromium-bidi) repository is an excellent (and simple-ish) example on how to do so[^4].

Given a `.github/workflows/e2e.yml` file:

```yaml
name: E2E tests

jobs:
  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 16
      - run: npm ci

      # This is the exciting part wherein we fetch CfT.
      #
      # Despite the "chromium" name, this is actually CfT.
      #
      # We set a explicit shell to force "set -eo pipefail" so that,
      # if the command fails, then the entire step fails.
      # We do not want "cut" to run if the download fails for some reason.
      #
      # The syntactic sugar of the parsing could be improved in a future
      # version of the CLI tool, but that's how it should be done for now.
      #
      # We store the location of the CfT binary in an environment variable.
      - name: Install Google Chrome for Testing
        shell: bash
        run: |
          cft_binary="$(npx @puppeteer/browsers install chromium@latest | cut -f 2- -d' ')"
          echo "cft_binary=$cft_binary" >> $GITHUB_ENV

      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install -r tests/requirements.txt

      # This is an example on how to run a test suite by explicitly pointing
      # out to CfT, using the environment variable set earlier.
      - name: Run E2E tests
        run: npm run e2e
        env:
          BROWSER_BIN: ${{ env.cft_binary }}
```

You can find the complete version of this example in an [older
commit](https://github.com/GoogleChromeLabs/chromium-bidi/blob/7d0962eb85c014dbb2cace7d471dd29474f11eab/.github/workflows/e2e.yml)
within that repository. The reason I link to an older commit is due to its
direct usage of the [@puppeteer/browsers](https://pptr.dev/browsers-api) CLI
tool, which makes it easier to illustrate how to fetch CfT. Recent commits of
the repository use a JS wrapper to do so, which is more flexible / robust for
the purposes of that particular repository at the expense of decreased
readability for a newcomer. Software Engineering is all about trade-offs after
all.

To fully realize the benefits of reproducibility, you should not use `latest`.
Instead, pin the browser to a specific version.

If using an environment variable (or a command-line flag) is not an option for
some reason, then an alternative would be to create a symlink (`ln -s`) to
`$cft_binary` from a place in the front of your `$PATH`. Or, alternatively,
temporarily update your `$PATH` with the `dirname` of `$cft_binary`.

Also, if you cannot or do not want to install `npm` (`npx`) just for the sake
of fetching CfT[^5], then just fetch it directly (use `curl` or `wget`) from
its [API
endpoint](https://github.com/GoogleChromeLabs/chrome-for-testing#json-api-endpoints), for example:

```shell
% wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/linux64/chrome-linux64.zip
```

Although note that this is not a future-proof way of fetching CfT. It's a
simple shortcut. The better way is to query the JSON metadata file for a
specific platform and browser version:

```shell
% curl https://googlechromelabs.github.io/chrome-for-testing/latest-patch-versions-per-build-with-downloads.json | jq -r '.builds."121.0.6167".downloads.chrome[] | select(.platform == "linux64").url'
```

...so that the download works even if the URL changes in the future [for some
reason](https://github.com/GoogleChromeLabs/chrome-for-testing/pull/102).

## References

- Chrome for Testing Design Document: https://goo.gle/chrome-for-testing
- [How Chrome DevTools helps to defend against self-XSS attacks](https://developer.chrome.com/blog/self-xss#can_you_disable_it_for_test_automation)

[^1]: For simplicity, referred to as just _Chrome_ hereafter.
[^2]: The same way you wouldn't recommend Arch Linux for linux newbies.
[^3]: You can find lots of such reports [here](https://groups.google.com/g/chromedriver-users).
[^4]: **Disclaimer**: I used to work on that repository, thus my self-assessment is clearly biased :-)
[^5]: I know, I know, JS bloat.
