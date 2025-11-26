---
title: "ByteByteGo: Kth Largest Integer"
date: 2025-11-26T18:11:54-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: Kth Largest Integer](https://bytebytego.com/exercises/coding-patterns/sort-and-search/kth-largest-integer):

Sort with `reverse=True`:

```python
from typing import List

def kth_largest_integer(nums: List[int], k: int) -> int:
    s = sorted(set(nums), reverse=True)

    if len(s) == 1:
        return list(s)[0]

    return list(s)[k - 1 % len(nums)]
```

Sort with `reversed`:

```python
from typing import List

def kth_largest_integer(nums: List[int], k: int) -> int:
    s = list(reversed(list(sorted(set(nums)))))

    if len(s) == 1:
        return list(s)[0]

    return list(s)[k - 1 % len(nums)]
```

Forego reversion, index from the end of the list instead:

```python
from typing import List

def kth_largest_integer(nums: List[int], k: int) -> int:
    s = sorted(set(nums))

    if len(s) == 1:
        return list(s)[0]

    return list(s)[len(nums) - k]
```
