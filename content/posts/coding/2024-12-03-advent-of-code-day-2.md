---
title: "Advent of Code 2024: Day 2"
date: 2024-12-03T01:15:00+01:00
tags:
  - dev
categories:
  - coding
---

Refer to the [previous post]({{< ref "2022-01-28-advent-of-code" >}}) about AoC,
and to the [git repository](https://github.com/thiagowfx/adventofcode) with my
solutions in Python 3.

Link to [Day #2](https://adventofcode.com/2024/day/2) puzzle.

The first part is straightforward. It felt right to use [`pairwise`](https://docs.python.org/3/library/itertools.html#itertools.pairwise) to compute the differences between each adjacent pair:

```python
diffs = [(b - a) for (a,b) in pairwise(map(int, line.split(' ')))]
```

Then we combine it with `all`:

```python
def is_safe(diffs):
    return all(1 <= n <= 3 for n in diffs) or all(-3 <= n <= -1 for n in diffs)
```

Note that it is necessary to use two `all` expressions. It feels tempting to do:

```python
all(1 <= n <= 3 or -3 <= n <= -1 for n in diffs)
```

...however that's incorrect. For example: `diffs = [1, -1, 1, -1]` with an input
such as `[1, 2, 1, 2]` would pass the test even though it shouldn't.

It also feels tempting to use `abs()` but then an additional check would be
necessary to ensure the diffs are either all positive or all negative.

The second part was trickier.

Initially I was doing:

```python
list(1 <= n <= 3 for n in diffs).count(False) <= 1 or list(-3 <= n <= -1 for n in diffs).count(False) <= 1
```

...but then I realized I misunderstood the problem.

The `1 2 7 8 9` line, whose diff is `[1, 5, 1, 1]`, illustrates it well: in
principle it would pass the test by dropping "5" from the diff. However, that
cannot be correct, because `2 -> 8` is too big of a jump.

The brute force way is to drop elements one by one, splitting the original list
into two, and then checking `is_safe` in the merged sublists. That would
require computing `diffs` every time, which would yield an `O(n^2)` solution.

We can do better by pre-computing `diffs` only once, and then adding a bit of
manipulation to reconstruct what the merged diffs would be. The end goal is to
compute this:

```python3
is_safe(diffs[:i-1] + [l[i+1] - l[i-1]] + diffs[i+1:]):
```

...i.e. the left part of `diffs`, the right part of `diffs`, and a rolling diff
element in the middle.

The full solution:

```python
#!/usr/bin/env python3
import sys

from itertools import pairwise

def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    safe = 0
    safe_damp = 0

    def is_safe(diffs):
        return all(1 <= n <= 3 for n in diffs) or all(-3 <= n <= -1 for n in diffs)

    for line in lines:
        l = list(map(int, line.split(' ')))
        diffs = [(b - a) for (a,b) in pairwise(l)]

        is_this_safe = is_safe(diffs)
        if is_this_safe:
            safe += 1
            safe_damp += 1
            continue

        for i in range(len(l)):
            if i == 0:
                if is_safe(diffs[1:]):
                    safe_damp += 1
                    break
            elif i == len(l) - 1:
                if is_safe(diffs[:-1]):
                    safe_damp += 1
                    break
            else:
                if is_safe(diffs[:i-1] + [l[i+1] - l[i-1]] + diffs[i+1:]):
                    safe_damp += 1
                    break

    # part one
    print(safe)

    # part two
    print(safe_damp)

if __name__ == '__main__':
    main()
```

A few notes:

- there's no need for `pairwise`; a plain `for-range` loop would have done the
  job just fine; `pairwise` is stylish though
- `1 <= n <= 3` is syntactic sugar for `1 <= n and n <= 3`. Python is sweet.
- part two could become a bit more elegant by introducing another helper
  function
- naming is hard
- `pairwise` is only available from Python 3.10+. macOS 15 (Sequoia) ships with
  Python 3.9. Oh well...I needed to use the Python binary from homebrew.
