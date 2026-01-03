---
title: "AoC 2025 Day 1: Secret Entrance"
date: 2025-12-01T02:33:03-03:00
tags:
  - dev

categories:
  - coding
---

A new year, a new advent of code. My _Pythonista_ self is always happy.

[AoC 2025 Day 1: Secret Entrance](https://adventofcode.com/2025/day/1):

## Part One

```python
#!/usr/bin/env python3
import sys

def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    ans = 0
    dial = 50

    for line in lines:
        direction = line[0]
        assert direction in 'LR'

        delta = int(line[1:])
        assert delta >= 0

        dial = (dial + (-1 if direction == 'L' else 1) * delta + 100) % 100
        # print(direction, delta, dial)

        if dial == 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
```

Straightforward. Just need to `%` once.

## Part Two

```python
#!/usr/bin/env python3
import sys

def part1(lines):
    ans = 0
    dial = 50

    for line in lines:
        direction = line[0]
        assert direction in 'LR'

        delta = int(line[1:])
        assert delta > 0

        dial = (dial + (-1 if direction == 'L' else 1) * delta + 100) % 100
        # print(direction, delta, dial)

        if dial == 0:
            ans += 1

    print(ans)


def part2(lines):
    ans = 0
    dial = 50

    print(dial)

    for line in lines:
        direction = line[0]
        assert direction in 'LR'

        delta = int(line[1:])
        assert delta > 0

        was_zero = dial == 0
        dial = dial + (-1 if direction == 'L' else 1) * delta

        passes = 0

        if dial > 0:
            passes = dial // 100
            dial %= 100
        elif dial < 0:
            passes = abs((dial - 1) // 100)
            dial %= 100
            assert dial >= 0
            passes -= int(was_zero)
        else:
            passes = 1

        # print(direction, delta, dial)
        # print(f'{passes=}')

        ans += passes

    print(ans)


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    part1(lines)
    part2(lines)


if __name__ == '__main__':
    main()
```

Various edge cases.

Positive dials are easy.

Non-positive dials require accounting for whether the dial was initially in
zero.
