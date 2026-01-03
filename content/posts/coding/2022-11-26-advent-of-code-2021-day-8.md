---
title: "Advent of Code 2021: Day 8"
date: 2022-11-26T00:00:00+00:00
tags:
  - dev
categories:
  - coding
---

Refer to the [previous post]({{< ref "2022-01-28-advent-of-code" >}}) about AoC,
and to the [git repository](https://github.com/thiagowfx/adventofcode) with my
solutions in Python 3.

Link to [Day #8](https://adventofcode.com/2021/day/8) puzzle.

Decode seven-segment display signals. Count unique digit segments in output values.

```python
#!/usr/bin/env python3
import sys

with open(sys.argv[1]) as input:
    lines = input.read().splitlines()

def part1():
    total = 0

    for line in lines:
        outputs = line.split(' | ')[1].split(' ')
        total += sum(len(output) in [2, 3, 4, 7] for output in outputs)

    print(total)

part1()
```
