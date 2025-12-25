---
title: "Advent of Code 2024: Day 11"
date: 2024-12-12T19:15:35-03:00
tags:
  - coding
  - dev
---

Link to [Day #11](https://adventofcode.com/2024/day/11) puzzle.

Part one can be done with a simulation.

It is very delightful to do it in python: lists are quite flexible, and
converting from integers to strings and vice-versa is seamless. Counting the
number of digits of `x` is just a matter of `len(str(x))`. In C++ it's a bit
kludgier with `std::string(x).size()` and `std::stoi(s)`, but then you need to
remember which header to import[^1].

I thought of using `reduce` to do `blink(blink(stone))...` and so on:

```python
print(len(reduce(lambda stone: blink(stone), range(25), stones)))
```

...nonetheless it's more readable to simply use a plain `for-range` loop:

```python
for _ in range(25):
    stones = blink(stones)
print(len(stones))
```

The secret sauce is in `blink`:

```python
def blink(stones):
    stones_next = []

    for stone in stones:
        s = str(stone)

        if stone == 0:
            stones_next.append(1)

        elif len(s) % 2 == 0:
            index = len(s) // 2
            stones_next.append(int(s[:index]))
            stones_next.append(int(s[index:]))

        else:
            stones_next.append(stone * 2024)

    return stones_next
```

For part two we need to be cleverer. In principle the same approach would work,
however it takes too long to process due to its exponential nature. In my laptop
I can get up to the 42nd `blink` iteration without losing my patience to wait
even longer.

The main observation to account for is that we only care about the length of the
stone sequence, hence the original task transforms into a simple 2D dynamic
programming problem.

I call:

```python
print(dp_blink(stones, 75))
```

Which is defined this way:

```python
def dp_blink(stones, times):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(stone: int, times: int) -> int:
        if times == 0:
            return 1

        return sum([dp(stone, times - 1) for stone in blink([stone])])

    return sum([dp(stone, times) for stone in stones])
```

The DP consists of the stone, and how many times are left for you to blink at it.

The full solution:

```python
#!/usr/bin/env python3
import sys

def blink(stones):
    stones_next = []

    for stone in stones:
        s = str(stone)

        if stone == 0:
            stones_next.append(1)

        elif len(s) % 2 == 0:
            index = len(s) // 2
            stones_next.append(int(s[:index]))
            stones_next.append(int(s[index:]))

        else:
            stones_next.append(stone * 2024)

    return stones_next

def dp_blink(stones, times):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(stone: int, times: int) -> int:
        if times == 0:
            return 1

        return sum([dp(stone, times - 1) for stone in blink([stone])])

    return sum([dp(stone, times) for stone in stones])

def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    stones = [int(stone) for stone in lines[0].split()]

    for _ in range(25):
        stones = blink(stones)

    # part one
    print(len(stones))

    # This is very slow, with an exponential complexity runtime.
    # What did you expect?
    #
    # for i in range(50):  # 50 = 75 - 25
    #     print(i)
    #     stones = blink(stones)

    # # part two
    # print(len(stones))

    stones = [int(stone) for stone in lines[0].split()]

    # part two
    print(dp_blink(stones, 75))

if __name__ == '__main__':
    main()
```

[^1]: It's `#include <string>`.
