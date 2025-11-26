---
title: "ByteByteGo: Repeated Removal of Adjacent Duplicates"
date: 2025-11-25T21:45:48-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: Repeated Removal of Adjacent Duplicates](https://bytebytego.com/exercises/coding-patterns/stacks/repeated-removal-of-adjacent-duplicates):

```python
def repeated_removal_of_adjacent_duplicates(s: str) -> str:
    stack = []

    for c in s:
        if len(stack) == 0 or stack[-1] != c:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()

    return ''.join(stack)
```
