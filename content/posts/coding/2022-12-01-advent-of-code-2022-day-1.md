---
title: "Advent of Code 2022: Day 1"
date: 2022-12-01T00:00:00+00:00
tags:
  - advent-of-code
  - dev
categories:
  - coding
---

Refer to the [previous post]({{< ref "2022-01-28-advent-of-code" >}}) about AoC,
and to the [git repository](https://github.com/thiagowfx/adventofcode) with my
solutions in Python 3.

Link to [Day #1](https://adventofcode.com/2022/day/1) puzzle.

Find the elf carrying the most calories. Part two finds the top three elves.

```python
#!/usr/bin/env python3
import itertools
import sys


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    # ['1', '2', '', '3'] -> [1, 2, '', 3]
    lines = [int(line) if line != "" else line for line in lines]

    # [1, 2, '', 3] -> [[1, 2], [3]]
    groups = [list(group) for key, group in itertools.groupby(
        lines, lambda a: a == "") if not key]

    # Part 1
    calories = [sum(group) for group in groups]

    print(max(calories))

    # Part 2
    print(sum(sorted(calories, reverse=True)[:3]))


if __name__ == '__main__':
    main()
```
