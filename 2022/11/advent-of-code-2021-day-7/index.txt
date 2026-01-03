
Refer to the [previous post]({{< ref "2022-01-28-advent-of-code" >}}) about AoC,
and to the [git repository](https://github.com/thiagowfx/adventofcode) with my
solutions in Python 3.

Link to [Day #7](https://adventofcode.com/2021/day/7) puzzle.

Calculate optimal position for crab submarines. Part one uses median, part two uses triangular cost function.

```python
#!/usr/bin/env python3
import statistics
import sys

with open(sys.argv[1]) as input:
    numbers = list(map(int, input.read().split(',')))

def part1():
    median = int(statistics.median(numbers))
    fuel = int(sum(abs(median - number) for number in numbers))

    print(fuel)

def cost(n):
    return (n * (n + 1)) / 2

def part2():
    fuel = float('inf')

    for guess in range(min(numbers), max(numbers) + 1):
        fuel = min(int(sum(cost(abs(guess - number)) for number in numbers)), fuel)

    print(fuel)

part1()
part2()
```

