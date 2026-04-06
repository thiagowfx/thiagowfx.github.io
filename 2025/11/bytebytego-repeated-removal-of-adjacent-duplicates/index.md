---
title: "ByteByteGo: Repeated Removal of Adjacent Duplicates"
url: https://perrotta.dev/2025/11/bytebytego-repeated-removal-of-adjacent-duplicates/
last_updated: 2026-01-03
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

