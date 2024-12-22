---
title: "Advent of Code: Day 8"
date: 2024-12-20T22:47:51-03:00
tags:
  - dev
---

Link to [Day #8](https://adventofcode.com/2024/day/8) puzzle.


This is a problem in a 2D grid. I like to start by making a frequency map
(dictionary) from the frequencies to the coordinates where they occur:

```python3
from collections import defaultdict

# {'0': ((1,8), ...)}
freq_map = defaultdict(tuple)
for x, line in enumerate(lines):
    for y, field in enumerate(line):
        if field.isalnum():
            freq_map[field] += ((x, y),)
```

Then it's just a matter of going through every coordinate pair for a given
frequency. `combinations()` from `itertools` is great for that:

```python3
from itertools import combinations

antinodes = set()

for all_coords in freq_map.values():
    for coord1, coord2 in combinations(all_coords, 2):
        antinodes.update(compute_antinodes(coord1, coord2, len(lines), len(lines[0])))
```

The meat of the code lives in `compute_antinodes`. We need to compute two
coordinates and check whether they are within bounds:

```python3
def within_bounds(x, y, height, width):
    return 0 <= x < height and 0 <= y < width

def compute_antinodes(coord1, coord2, height, width):
    x1, y1 = coord1
    x2, y2 = coord2

    dx = x2 - x1
    assert dx >= 0

    dy = y2 - y1

    antinodes = ()

    for (x0, y0, direction) in ((x1, y1, -1), (x2, y2, +1)):
        x, y = x0 + direction * dx, y0 + direction * dy
        if within_bounds(x, y, height, width):
            antinodes += ((x, y),)

    return antinodes
```

The `assert`ion gives us peace of mind.

The answer is the number of `antinodes`.

For part two, we need to extend the `compute_antinodes` logic to keep going
until it gets out-of-bounds:

```python3
def compute_antinodes(coord1, coord2, height, width, unbounded=False):
    x1, y1 = coord1
    x2, y2 = coord2

    dx = x2 - x1
    assert dx >= 0

    dy = y2 - y1

    if unbounded:
        antinodes = ((x1, y1), (x2, y2))
    else:
        antinodes = ()

    for (x0, y0, direction) in ((x1, y1, -1), (x2, y2, +1)):
        steps = 1
        while True:
            x, y = x0 + direction * steps * dx, y0 + direction * steps * dy
            if within_bounds(x, y, height, width):
                antinodes += ((x, y),)
                steps += 1
            else:
                break

    return antinodes
```

The full solution:

```python3
#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations

import sys

def within_bounds(x, y, height, width):
    return 0 <= x < height and 0 <= y < width


def compute_antinodes(coord1, coord2, height, width, unbounded=False):
    x1, y1 = coord1
    x2, y2 = coord2

    dx = x2 - x1
    assert dx >= 0

    dy = y2 - y1

    if unbounded:
        antinodes = ((x1, y1), (x2, y2))
    else:
        antinodes = ()

    for (x0, y0, direction) in ((x1, y1, -1), (x2, y2, +1)):
        steps = 1
        while True:
            x, y = x0 + direction * steps * dx, y0 + direction * steps * dy
            if within_bounds(x, y, height, width):
                antinodes += ((x, y),)
                steps += 1
            else:
                break

    return antinodes


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    # {'0': ((1,8), ...)}
    freq_map = defaultdict(tuple)
    for x, line in enumerate(lines):
        for y, field in enumerate(line):
            if field.isalnum():
                freq_map[field] += ((x, y),)

    antinodes = set()

    for all_coords in freq_map.values():
        for coord1, coord2 in combinations(all_coords, 2):
            antinodes.update(compute_antinodes(coord1, coord2, len(lines), len(lines[0])))

    # part one
    print(len(antinodes))

    antinodes = set()

    for all_coords in freq_map.values():
        for coord1, coord2 in combinations(all_coords, 2):
            antinodes.update(compute_antinodes(coord1, coord2, len(lines), len(lines[0]), unbounded=True))

    # part two
    print(len(antinodes))

if __name__ == '__main__':
    main()
```

Instead of using tuples or coordinates all over the place, we could simply have
modified the map inplace, and then iterated over it in the end to count the
antinodes. I like the tuple abstraction better, and it's quite efficient anyway.
