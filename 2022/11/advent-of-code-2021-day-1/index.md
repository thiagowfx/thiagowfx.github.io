
Refer to the [previous post]({{< ref "2022-01-28-advent-of-code" >}}) about AoC,
and to the [git repository](https://github.com/thiagowfx/adventofcode) with my
solutions in Python 3.

Link to [Day #1](https://adventofcode.com/2021/day/1) puzzle.

Count the number of times a measurement increases from one to the next. Part two
uses a sliding window of three measurements.

```python
#!/usr/bin/env python3
import sys

with open(sys.argv[1]) as input:
    lines = input.readlines()

numbers = [int(line.strip()) for line in lines]

# Part 1
print(sum(y > x for x, y in zip(numbers[:-1], numbers[1:])))

# Part 2
print(sum(y > x for x, y in zip(numbers[:-3], numbers[3:])))
```

