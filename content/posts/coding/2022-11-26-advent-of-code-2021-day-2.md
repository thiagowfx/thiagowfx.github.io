---
title: "Advent of Code 2021: Day 2"
date: 2022-11-26T00:00:00+00:00
tags:
  - advent-of-code
  - dev
categories:
  - coding
---

Refer to the [previous post]({{< ref "2022-01-28-advent-of-code" >}}) about AoC,
and to the [git repository](https://github.com/thiagowfx/adventofcode) with my
solutions in Python 3.

Link to [Day #2](https://adventofcode.com/2021/day/2) puzzle.

Calculate final position using forward, down, and up instructions. Part two introduces an aim variable.

```python
#!/usr/bin/env python3
import sys

with open(sys.argv[1]) as input:
    lines = input.readlines()

units = [line.split(' ') for line in lines]

# Part 1
x = sum(int(unit[1]) for unit in units if unit[0] == 'forward')
y = sum(int(unit[1]) if unit[0] == 'down' else (-1) * int(unit[1]) if unit[0] == 'up' else 0 for unit in units)

print(x * y)

# Part 2
x = 0
y = 0
aim = 0

for unit in units:
    instruction = unit[0]
    distance = int(unit[1])

    if instruction == 'forward':
        x += distance
        y += aim * distance
    elif instruction == 'up':
        aim -= distance
    elif instruction == 'down':
        aim += distance

print(x * y)
```
