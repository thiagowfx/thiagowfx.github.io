---
title: "Advent of Code"
date: 2022-01-28T17:44:00-05:00
tags:
  - programming
showtoc: true
---

Last year I found out about [Advent of Code][aoc].

<!--more-->

## You said what?

**Advent of Code** by [Eric Wastl](http://was.tl/) happens every year since 2015, every December from the 1st to
the 25th. Each day there's a new programming challenge[^1] split into two
parts. The first part tends to be easier than the second one. The second part
usually builds upon the first one, being a follow-up task that requires more
steps and/or with a higher degree of complexity. You can't always reuse the
bits from the first part to solve the second one though.

For those familiar with programming contests like [ACM ICPC][icpc] or [OBI][obi], or online judges like [SPOJ][spoj] or [UVa][uva], advent of code feels like home. The main difference is that there is no time pressure and no need to write spaghetti and unreadable code; in fact, writing readable and elegant solutions is encouraged (_citation needed_...).

For those familiar with FAANG/Tech whiteboard interviews, advent of code feels a lot like a typical interview. I would even go further and say it's a great way to practice for interviews.

It is a great moment to either (i) learn a new exciting programming language or (ii) improve your mastery on programming languages that you already know. I know several people (see below) that used AoC[^2] to learn Rust or Kotlin or whatever else was exciting for them at the time. It's surprising that the official Kotlin Docs even contain a section called [Advent of Code puzzles in idiomatic Kotlin](https://kotlinlang.org/docs/advent-of-code.html).

Some folks go even further and use it to practice their [code golfing](https://codegolf.stackexchange.com/questions/216024/advent-of-code-2020-day-2-part-1)[^3] or even [Google Sheets](https://ryxcommar.com/2021/12/04/advent-of-code-2021-in-google-sheets-first-4-days/) skills. I have a deep amount of respect for them as it's quite a challenge. If you think it stops there, I've also seen solutions in [awk](https://github.com/phillbush/aoc) and [sed](https://twitter.com/_rsc/status/1476683352493207561).

Another positive aspect of AoC is that it has an integrated dashboard that tracks your progress as you go. It's a simple element of gamification that immensely improves motivation and fun. You really feel a big desire to collect all those 50 stars...

## What about me?

As a simpleton my goal for 2021 was relatively less ambitious than that,  I just wanted to improve my Python skills, more specifically Python 3. I learned Python 2 during my first year in university and used it sparingly at work and for personal endeavours, but always had a knowledge gap in Python 3.

I set up a public git repository with [my solutions][myaoc] and aspired to write simple and elegant python, my only [constraint](https://frantic.im/no-constraints-no-fun/) was to limit myself to what is available in the standard library of a vanilla python3 installation in Alpine linux, with the exception of [`numpy`][numpy] which is widespread enough to deserve an entry in my [`requirements.txt`](https://github.com/thiagowfx/adventofcode/blob/master/requirements.txt), and of course devtools like debuggers, linters and auto formatters as needed.

As an additional, non-programming challenge I also limited myself to only use the command line. This basically meant no IDEs[^4]. My programming environment was ultimately `ssh` to an Alpine Linux VPS + `tmux` + `vim`. To make my life easier, one of the first tasks I accomplished was to write a generic [`Makefile`](https://github.com/thiagowfx/adventofcode/blob/master/Makefile) to help me test and run my scripts. A typical invocation would look like:

```shell
$ make DEBUG=1 DAY=3
```

...whereas I could choose between the sample input versus the real one with `DEBUG`, and the puzzle day with `DAY`.

Was the experience worth it? **Definitely yes**! Even though I only completed ~8 puzzles out of the 25 ones due to having my attention split with another project I was working on at the time, the thematic submarine puzzles were hella fun and I learned a lot of python 3 on the way.

A few highlights of what I learned *and used* from my python `2to3` transition were f-strings / string interpolation (`print(f'The sum is {sum}')`), "everything is an iterator now" even `map` and `range`, the standard library is awesome and sometimes you stumble upon useful abstractions like `Counter` and `defaultdict`, `sort` is different now (`key` instead of comparison function), this `pdb` debugger thingy, among other topics I can't remember at the moment. I realized the only concept that was previously familiar was the different syntax of the `print` function (you have to use parentheses now).

In terms of workflow, I also learned that virtual environments are now
supported natively[^5] (`python -m venv`), `direnv` is an amazing tool to
automate/manage environments in git repositories and also happens to have
first-class python integration, `pylint` and `autopep8` are good integrations
with `vim` to help spot basic errors and/or suggest best practices, and `numpy` takes forever to build from source.

## What about the community?

AoC enjoys a lot of popularity and zeitgeist, especially during times of the COVID-19 pandemic, but even before then. There's a large [/r/adventofcode](https://www.reddit.com/r/adventofcode/) subreddit community, lots of people share their solution snippets and impressions on Twitter ([#AdventOfCode](https://twitter.com/search?q=%23adventofcode&src=typed_query)), there's a ton of public git repositories on [GitHub](https://github.com/search?q=adventofcode) where people share their coding solutions, in pretty much any programming language you can think of, and finally there are many screencasts on [YouTube](https://www.youtube.com/results?search_query=advent+of+code). The Internet in the 2020s sparks creativity in every unimaginable corner.

There's so much information that it's impossible to stay on top of everything. Here is a small list of repositories that I followed this year, most of those are acquaintances/friends and/or stumbled upon Twitter:

C++:
- https://github.com/riuri/adventofcode

Python:
- https://github.com/sjvrijn/AdventofCode
- https://github.com/oomenn/AOC

Rust:
- https://github.com/dimo414/advent-2021
- https://github.com/mfs/aoc

I find it's really constructive and useful (and also _fun_) to peek at other people's solutions after I coded my own. I have extensive (albeit kinda rusty these days) experience with C++ so I wanted to follow at least one repository coded with it; since I wrote my solutions in python it was also a natural choice to follow a few python repositories; and, finally, I wanted to peek at some languages I am not familiar with to get a gist of them. This year I watched Rust and a few bits of Clojure and Kotlin on Twitter.

Finally, for some extra inspiration, there are also some _10x programmers_[^6] out there that seem to be fans of AoC as well: [Peter Norvig](https://github.com/norvig/pytudes) and [Russ Cox (_rsc_)](https://twitter.com/_rsc/status/1466089522718986241). There are probably several others I am not aware of.

## Final remarks

I am hoping to participate in AoC this year (2022) as well, and possibly revisit the 2021 puzzles and resolve the rest of the ones I missed as time permits.

Hopefully this post encourages and motivates you to try Advent of Code as well! Happy coding.


[aoc]: https://adventofcode.com/
[icpc]: https://icpc.global/
[myaoc]: https://github.com/thiagowfx/adventofcode
[numpy]: https://numpy.org/
[obi]: https://olimpiada.ic.unicamp.br/
[spoj]: https://www.spoj.com/
[uva]: https://onlinejudge.org/

[^1]: Or puzzle, if you will.
[^2]: Acronym not to be confused with a certain ~~annoying~~^W politician.
[^3]: For those unfamiliar with the concept, code golfing is all about writing a correct solution with the **fewest** amount of characters.
[^4]: For example: PyCharm, and also VSCode, which is getting so big these days I don't even know if it's possible to just call it a simple text editor anymore.
[^5]: Back in the days, `virtualenvwrapper` was all the rage.
[^6]: The _10x programmer_ thing is a well-known joke however in this instance the mentioned characters are indeed superb programmers that I immensely respect.
