---
title: "Advent of Code 2024: Day 1"
date: 2024-12-01T22:29:19+01:00
tags:
  - aoc
  - dev
---

Refer to the [previous post]({{< ref "2022-01-28-advent-of-code" >}}) about AoC,
and to the [git repository](https://github.com/thiagowfx/adventofcode) with my
solutions in Python 3.

Link to [Day #1](https://adventofcode.com/2024/day/1) puzzle.

This is just a warm-up.

Given two lists of integers, iterate over them and sum the absolute difference
between each pair. `zip` + `sum` is the perfect pair[^1] for the job.

Part two: iterate over the left list whilst accumulating how often the element
appears in the right list. "How often" has, almost always, the smell of a
[`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter).

The full solution[^2]:

```python
#!/usr/bin/env python3
import sys

from collections import Counter

def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    left = []
    right = []

    for line in lines:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    # part one
    print(sum(abs(l - r) for (l, r) in zip(left, right)))

    freqs = Counter(right)

    # part two
    print(sum(l * freqs[l] for l in left))

if __name__ == '__main__':
    main()
```

[^1]: [I'm not sure I like it, And I'm so tired of
    fighting](https://www.youtube.com/watch?v=3WpdCZC9q6w)
[^2]: The git repository is ever-evolving and the source of truth, whereas the
    blog post is a snapshot. I'll experiment with cross-posting solutions here
    even though it duplicates the repository ones.
