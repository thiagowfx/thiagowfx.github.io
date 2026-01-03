---
title: "Advent of Code 2021: Day 3"
date: 2022-11-26T00:00:00+00:00
tags:
  - dev
categories:
  - coding
---

Refer to the [previous post]({{< ref "2022-01-28-advent-of-code" >}}) about AoC,
and to the [git repository](https://github.com/thiagowfx/adventofcode) with my
solutions in Python 3.

Link to [Day #3](https://adventofcode.com/2021/day/3) puzzle.

Calculate power consumption using binary diagnostic data. Part two finds oxygen and CO2 ratings using bit criteria.

```python
#!/usr/bin/env python3
import numpy as np
import sys

with open(sys.argv[1]) as input:
    lines = input.readlines()

lines = [list(line.strip()) for line in lines]

# Part 1
transposed = np.array(lines).T.tolist()

gamma_str = ''.join(['1' if col.count('1') > col.count('0') else '0' for col in transposed])
gamma = int(gamma_str, base = 2)

epsilon_str = ''.join(['0' if c == '1' else '1' for c in gamma_str])
epsilon = int(epsilon_str, base = 2)

print(gamma * epsilon)

# Part 2
def oxygen(lines, depth = 0):
    if len(lines) == 1:
        return int(''.join(lines[0]), base = 2)

    transposed = np.array(lines).T.tolist()

    most_common = '1' if transposed[depth].count('1') >= transposed[depth].count('0') else '0'

    return oxygen([line for line in lines if line[depth] == most_common], depth + 1)

def co2(lines, depth = 0):
    if len(lines) == 1:
        return int(''.join(lines[0]), base = 2)

    transposed = np.array(lines).T.tolist()

    most_common = '1' if transposed[depth].count('1') < transposed[depth].count('0') else '0'

    return co2([line for line in lines if line[depth] == most_common], depth + 1)

print(oxygen(lines) * co2(lines))
```
