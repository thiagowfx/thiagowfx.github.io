---
title: "Advent of Code 2024: Day 9"
date: 2024-12-25T16:09:53-03:00
tags:
  - aoc
  - dev
---

Link to [Day #9](https://adventofcode.com/2024/day/9) puzzle.

A disk fragmentation problem.

It's mostly an ad-hoc problem, there isn't much commentary to make.

Part two was quite annoying so I simply skipped it.

The full solution:

```python
#!/usr/bin/env python3
import sys

def expand(disk: list[int]) -> str:
    output = []
    fill = True
    d = 0

    for n in disk:
        if fill:
            output += [str(s) for s in n * [d]]
            d += 1
        else:
            output += n * '.'
        fill = not fill

    return output


def defrag(disk: str) -> str:
    p = expand(disk)

    left = 0
    right = len(p) - 1

    while left < right:
        if p[left] == '.':
            p[left], p[right] = p[right], p[left]
            right -= 1
            while p[right] == '.' and left < right:
                right -= 1

        left += 1

    return p


def checksum(disk):
    total = 0

    for i, d in enumerate(disk):
        if d == '.':
            break
        total += i * int(d)

    return total


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    disk = [int(x) for x in lines[0]]

    # part one
    print(checksum(defrag(disk)))


if __name__ == '__main__':
    main()
```
