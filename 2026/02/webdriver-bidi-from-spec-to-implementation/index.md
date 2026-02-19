
[Previously]({{< ref "2024-01-25-chrome-for-testing" >}}).

**Disclaimer**: Some [LLM magic]({{< ref "/ai" >}}) was used in this blog
post[^2].

[^2]: As it's explicitly noted that I do not use AI to craft blog posts in this
site, and this is one exception, I feel that it must be disclosed upfront.
You're free to skip it if it doesn't suit you. That said, you can tell I edited
the entire post by hand because there are various personal touches all over the
place.

From mid-2022 to late 2023, I was one of the core contributors to
[chromium-bidi](https://github.com/GoogleChromeLabs/chromium-bidi), an
implementation of the [WebDriver BiDi](https://w3c.github.io/webdriver-bidi/)
protocol for Chromium. This was before the agentic LLM days.

Think of it as the next-generation browser automation protocol – the successor
to WebDriver Classic (Selenium-era) and a complement to [CDP (Chrome DevTools
Protocol)](https://chromedevtools.github.io/devtools-protocol/), used by
Puppeteer.

**The key innovation**: bidirectional communication between the test client and
the browser, enabling event-driven automation instead of request-response
polling.

With classic WebDriver, if you wanted to listen for a console log or a network
request, you couldn't – the client sends commands, the server responds, end of
story. You'd need to **poll** for changes. With BiDi, the browser can push
events to the client as they happen: DOM mutations, network interceptions,
script errors, all in real time.

The project is a TypeScript translation layer that sits between BiDi clients and
CDP, running inside a ~~Chrome~~ Chromium tab.
[Our](https://www.linkedin.com/in/sadym/)
[small](https://www.linkedin.com/in/alexrudenko/)
[team](https://www.linkedin.com/in/mathiasbynens/) at Google built it from the
ground up.

## By the numbers

**Disclaimer**: The LLM fetched these numbers, using the [GitHub
CLI](https://cli.github.com/). I am confident they are reasonably correct[^1].

[^1]: Because, initially, it wasn't...by a lot. You _really_ need to
    double-check numbers made up by LLMs.

Over roughly two years, _my_ contributions stood as follows:

- **426 PRs** authored (371 merged)
- **442 PRs** reviewed from teammates
- **29 issues** filed
- **42 PRs** upstream to [web-platform-tests/wpt](https://github.com/web-platform-tests/wpt) (the shared browser test suite)
- **34 PRs** upstream to [w3c/webdriver-bidi](https://github.com/w3c/webdriver-bidi) (the W3C specification itself)

At peak velocity (May--June 2023), I was opening 3--4 PRs per day.

## Infrastructure first

My first contribution
([#221](https://github.com/GoogleChromeLabs/chromium-bidi/pull/221), July 2022)
was adding Terser minification to the mapper, reducing its size by 43%. Not
fancy, but representative of my approach: fix the foundation before building on
it.

The first ~100 PRs were heavily focused on developer experience (#devex):

- Introduced [pre-commit.com](https://pre-commit.com/) with ESLint, Prettier,
  shellcheck, and codespell
  ([#373](https://github.com/GoogleChromeLabs/chromium-bidi/pull/373)). That's
  when I would eventually [fall in love]({{< ref "2024-12-21-pre-commit" >}})
  with it.
- Added macOS E2E tests, headful [WPT](https://web-platform-tests.org/) (Web
  Platform Tests -- the shared test suite across browser vendors) runs in GitHub
  Actions, [Chrome for Testing]({{< ref "2024-01-25-chrome-for-testing" >}}) in
  CI ([#427](https://github.com/GoogleChromeLabs/chromium-bidi/pull/427),
  [#466](https://github.com/GoogleChromeLabs/chromium-bidi/pull/466),
  [#671](https://github.com/GoogleChromeLabs/chromium-bidi/pull/671))
- Integrated [Wireit](https://github.com/nicolo-ribaudo/wireit) build system
  ([#603](https://github.com/GoogleChromeLabs/chromium-bidi/pull/603),
  +751/-337)
- Enforced conventional commits
  ([#900](https://github.com/GoogleChromeLabs/chromium-bidi/pull/900)). From
  that day I started to adopt a light (loose) version of it in my own
  repositories.
- Parallelized WPT test runs
  ([#828](https://github.com/GoogleChromeLabs/chromium-bidi/pull/828))
- Added Codecov integration
  ([#918](https://github.com/GoogleChromeLabs/chromium-bidi/pull/918)). It was
  for free.
- Automated browser version pinning and WPT submodule updates
  ([#941](https://github.com/GoogleChromeLabs/chromium-bidi/pull/941))

There was also a coordinated effort in January 2023 to remove static state from
the codebase -- about 10 PRs converting `EventManager`, `SubscriptionManager`,
`LogManager`, `ScriptEvaluator`, `BrowsingContextStorage`, and `RealmStorage`
from static classes to proper instances. This was the kind of refactoring that
makes everything that comes after easier: better testability, less global
coupling.

## Features

With the infrastructure solid, features came fast(er).

**`browsingContext.print`**
([#526](https://github.com/GoogleChromeLabs/chromium-bidi/pull/526)):
Print-to-PDF, including `shrinkToFit` support and golden image comparison
testing.

**`browsingContext.captureScreenshot`**
([#515](https://github.com/GoogleChromeLabs/chromium-bidi/pull/515)): Full
screenshot implementation including OOPIF (out-of-process iframe) support and
headful mode.

**`script.addPreloadScript`**
([#582](https://github.com/GoogleChromeLabs/chromium-bidi/pull/582)): Preload
scripts that run before page content, with channel and sandbox support added
incrementally over several months.

**Channel mechanism / `script.MessageEvent`**
([#319](https://github.com/GoogleChromeLabs/chromium-bidi/pull/319)): A
prototype for safe page-to-client communication. This one took ~4 months from
first draft to merge -- the longest-lived PR I had.

**`browsingContext.reload`**
([#654](https://github.com/GoogleChromeLabs/chromium-bidi/pull/654)): Including
the `wait` parameter and `ignoreCache` support.

## Network Interception woes

The largest body of work was implementing the full network request interception
subsystem. This was the kind of feature where you feel the weight of the entire
spec behind every line of code. And, again, this was before agentic LLMs.

It started in June 2023 with scaffolding
([#845](https://github.com/GoogleChromeLabs/chromium-bidi/pull/845)) and
stretched through November. The plot arc:

1. Parse URL patterns for `network.addIntercept`
   ([#1186](https://github.com/GoogleChromeLabs/chromium-bidi/pull/1186),
   +461/-526)
2. Handle `Fetch.requestPaused` CDP events
   ([#1304](https://github.com/GoogleChromeLabs/chromium-bidi/pull/1304))
3. Implement `network.failRequest`
   ([#1318](https://github.com/GoogleChromeLabs/chromium-bidi/pull/1318), 20
   review rounds)
4. Implement `network.continueRequest`
   ([#1331](https://github.com/GoogleChromeLabs/chromium-bidi/pull/1331), 28
   review rounds)
5. Unblock event queue when network events are blocked
   ([#1409](https://github.com/GoogleChromeLabs/chromium-bidi/pull/1409)) --
   co-authored with [Maksim Sadym](https://github.com/nicolo-ribaudo), this one
   was tricky
6. Implement `network.continueResponse`
   ([#1443](https://github.com/GoogleChromeLabs/chromium-bidi/pull/1443), 35
   review rounds)
7. Implement `network.provideResponse`
   ([#1457](https://github.com/GoogleChromeLabs/chromium-bidi/pull/1457))
8. Implement `network.continueWithAuth`
   ([#1470](https://github.com/GoogleChromeLabs/chromium-bidi/pull/1470))

My takeaway: networking is _flaky_.

All five BiDi network interception commands, fully implemented. The
`continueResponse` PR alone went through 35 rounds of review. This was
painstaking, detail-oriented work -- matching the spec precisely while dealing
with CDP's quirks underneath.

Again, this was before LLMs (how many times did I already mention that?). It
would have been _soooooo_ much easier, had they existed back then. They are
great at implementing specs and matching patterns, after all.

## Full-stack, spec to tests

What I enjoyed the most about this work was the feedback loop across layers. I
wasn't just writing TypeScript in one repo. The workflow often resembled the
following:

1. Find an ambiguity or bug in the [W3C
   spec](https://github.com/w3c/webdriver-bidi) while implementing a feature
2. Send a fix upstream to the spec (34 PRs)
3. Write the implementation in chromium-bidi
4. Write or fix tests in
   [web-platform-tests](https://github.com/web-platform-tests/wpt) (42 PRs)

This is the kind of work where you see the entire stack — from the standards
document to the test suite shared across browser vendors.

The WPT work was also a first-class concern in CI: I set up auto-committing WPT
expectations, parallelized test runs, and maintained a local bad SSL server for
testing ([#1521](https://github.com/GoogleChromeLabs/chromium-bidi/pull/1521)).

## Test Reorganization

One PR worth calling out:
[#1110](https://github.com/GoogleChromeLabs/chromium-bidi/pull/1110)
(+2586/-2385). This reorganized all E2E tests by domain -- the largest single
diff I landed. Not fancy but necessary. A well-organized test suite is how you
keep a project maintainable as it grows.

## Fin

This was one of the most rewarding projects I worked on at Google. Building a
browser automation protocol from scratch, contributing to W3C specs, and seeing
it all come together in real test infrastructure used by other browser vendors
-- it's the kind of work that makes you appreciate the craft of software
engineering at the standards level.

The project is [still
active](https://github.com/GoogleChromeLabs/chromium-bidi/pulls) and has since
been adopted as the default WebDriver BiDi implementation in Chromium.

