---
title: "Advent of Code: Day 3"
date: 2024-12-03T16:41:23+01:00
tags:
  - dev
---

Link to [Day #3](https://adventofcode.com/2024/day/3) puzzle.


It's a pretty typical regex problem.
To choose not to use regex is to endeavour in pain.

The regex for part one to extract all occurrences of `mul`:

```python3
r'mul\(\d+,\d+\)'
```

Note that with `r` there is no need to escape the backslashes in Python.

Later on I extract the numbers with `r'\d+'`.

If we really wanted we could do everything with a single regex by using
capturing groups, however it would become less readable.

Once the numbers are captured, it's just a matter of accumulating their product.

I craft and test my regex with the support of https://regex101.com/ and then
follow up with the Python interpreter in my laptop.

Part two adds two more operators, which we can easily account for with an or
(`|`).

The full solution:

```python
#!/usr/bin/env python3
import re
import sys


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    prod = prod_two = 0

    for memory in lines:
        ops = re.findall(r'mul\(\d+,\d+\)', memory)

        for op in ops:
            (f1, f2) = map(int, re.findall(r'\d+', op))
            prod += f1 * f2

    # part one
    print(prod)

    enabled = True
    for memory in lines:
        ops = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", memory)

        for op in ops:
            if "don't" in op:
                enabled = False
            elif "do" in op:
                enabled = True
            elif 'mul' in op:
                (f1, f2) = map(int, re.findall(r'\d+', op))

                if enabled:
                    prod_two += f1 * f2

    # part two
    print(prod_two)


if __name__ == '__main__':
    main()
```

I intended to use [`match`](https://docs.python.org/3/whatsnew/3.10.html) merely
for style points however it's only available from Python 3.10+, thus I sticked
  with a mere `if-elif` construct.

