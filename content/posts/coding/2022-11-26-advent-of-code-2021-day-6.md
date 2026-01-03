---
title: "Advent of Code 2021: Day 6"
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

Link to [Day #6](https://adventofcode.com/2021/day/6) puzzle.

Simulate lanternfish population growth using a counter to track fish by their internal timer.

```python
#!/usr/bin/env python3
from collections import Counter
import sys

with open(sys.argv[1]) as input:
    numbers = list(map(int, input.read().split(',')))

def simulation(days):
    fish = Counter(numbers)

    for _ in range(days):
        next_fish = Counter()
        for timer, count in fish.items():
            if timer == 0:
                next_fish[8] += fish[timer]
                next_fish[6] += fish[timer]
            else:
                next_fish[timer - 1] += fish[timer]
        fish = next_fish

    print(sum(fish.values()))

simulation(80)
simulation(256)
```
