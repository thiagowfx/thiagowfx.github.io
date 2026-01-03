---
title: "ByteByteGo: Josephus"
date: 2025-11-30T17:26:22-03:00
tags:
  - bytebytego
  - dev

categories:
  - coding
---

[ByteByteGo: Josephus](https://bytebytego.com/exercises/coding-patterns/math-and-geometry/the-josephus-problem):

With an array:

```python
def josephus(n: int, k: int) -> int:
    circle = list(range(n))
    victim = 0
    # [0, 1, 2, 3, 4]
    #  ^
    #
    # clockwise: victim += 1
    #
    # next victim: victim + k - 1 (remember to mod)

    while len(circle) > 1:
        victim = (victim + (k - 1)) % len(circle)
        del circle[victim]

    return circle[0]
```

With a linked list (`deque`):

```python
from collections import deque

def josephus(n: int, k: int) -> int:
    circle = deque(range(n))
    victim = 0
    # [0, 1, 2, 3, 4]
    #  ^
    #
    # clockwise: victim += 1
    #
    # next victim: victim + k - 1 (remember to mod)

    while len(circle) > 1:
        victim = (victim + (k - 1)) % len(circle)
        del circle[victim]

    return circle[0]
```

With a linked list, efficient removals from the end (beginning) of the list:

```python
from collections import deque

def josephus(n: int, k: int) -> int:
    circle = deque(range(n))

    while len(circle) > 1:
        # rotate left so that the k‑th person becomes the leftmost element
        # deque.rotate moves elements to the right; negative rotates left
        circle.rotate(-(k - 1))

        # eliminate that person
        circle.popleft()

    return circle[0]
```
