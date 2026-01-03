
Refer to the [previous post]({{< ref "2022-01-28-advent-of-code" >}}) about AoC,
and to the [git repository](https://github.com/thiagowfx/adventofcode) with my
solutions in Python 3.

Link to [Day #5](https://adventofcode.com/2024/day/5) puzzle.

It is a topological sort problem, plain and simple.

In part one all we care about is whether certain input sequences are valid,
within the sort constraints. It's very straightforward to verify that by
exhaustively checking all constraints ("edges"):

```python
import sys

def is_correct(update, edges):
    position = defaultdict(lambda: sys.maxsize, {node: i for (i, node) in enumerate(update)})

    for (first, second) in edges:
        if first in update and second in update and position[first] > position[second]:
            return False
    return True
```

`position` is a dictionary representing in which index (position) each element
occurs. I make use of a `defaultdict` with a very large value set by default
(instead of a vanilla `dict`) to avoid the need to explicitly check for element
presence.

In part two we need to perform the actual topological sort. Or...do we? Doing
toposort would be the most efficient way to resolve it, however, in this case,
plain brute force is good enough:

```python
def toposort(update, edges):
    position = defaultdict(lambda: sys.maxsize, {node: i for (i, node) in enumerate(update)})

    change = True
    while change:
        change = False
        for (first, second) in edges:
            if first in update and second in update and position[first] >= position[second]:
                position[first] = position[second] - 1
                change = True

    return sorted(update, key=lambda x: position[x])
```

Once again, we iterate through all the input constraints until we find a
violation. Whenever we find one, we fix the position of the element in the wrong
order by updating it to occur before the other element. We repeat this procedure
until there are no more violations.

The full source:

```python
#!/usr/bin/env python3
from collections import defaultdict
import sys

def is_correct(update, edges):
    position = defaultdict(lambda: sys.maxsize, {node: i for (i, node) in enumerate(update)})

    for (first, second) in edges:
        if first in update and second in update and position[first] > position[second]:
            return False
    return True

def toposort(update, edges):
    position = defaultdict(lambda: sys.maxsize, {node: i for (i, node) in enumerate(update)})

    change = True
    while change:
        change = False
        for (first, second) in edges:
            if first in update and second in update and position[first] >= position[second]:
                position[first] = position[second] - 1
                change = True

    return sorted(update, key=lambda x: position[x])

def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    edges = []
    updates = []

    for line in lines:
        if "|" in line:
            edges.append(list(map(int, line.split("|"))))
        elif len(line) == 0:
            continue
        else:
            updates.append(list(map(int, line.split(","))))

    total_one = total_two = 0
    for update in updates:
        if is_correct(update, edges):
            total_one += update[len(update) // 2]
        else:
            sorted_update = toposort(update, edges)
            total_two += sorted_update[len(sorted_update) // 2]

    # part one
    print(total_one)

    # part two
    print(total_two)

if __name__ == '__main__':
    main()
```

