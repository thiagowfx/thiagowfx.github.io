---
title: "Advent of Code 2022: Day 3"
date: 2022-12-03T00:00:00+00:00
tags:
  - dev
categories:
  - coding
---

Refer to the [previous post]({{< ref "2022-01-28-advent-of-code" >}}) about AoC,
and to the [git repository](https://github.com/thiagowfx/adventofcode) with my
solutions in Python 3.

Link to [Day #3](https://adventofcode.com/2022/day/3) puzzle.

Find misplaced items in rucksacks. Part two finds common items across three rucksacks.

```python
#!/usr/bin/env python3
import sys


def priority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        assert item.isupper()
        return ord(item) - ord('A') + 27


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    total_priority = 0

    # Part 1
    for line in lines:
        c1 = line[:len(line)//2]
        c2 = line[len(line)//2:]
        item = next(iter(set(c1).intersection(c2)))
        total_priority += priority(item)

    print(total_priority)

    # Part 2
    print(sum([priority(next(iter(set(line1).intersection(line2).intersection(line3))))
               for (line1, line2, line3) in zip(lines[::3], lines[1::3], lines[2::3])]))


if __name__ == '__main__':
    main()
```
