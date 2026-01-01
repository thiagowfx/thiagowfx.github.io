---
title: "ByteByteGo: Longest Chain of Consecutive Numbers"
date: 2025-11-24T00:41:57-03:00
rss: false
categories:
  - coding
---

[ByteByteGo: Longest Chain of Consecutive Numbers](https://bytebytego.com/exercises/coding-patterns/hash-maps-and-sets/longest-chain-of-consecutive-numbers):

```python
from typing import List

def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    nums.sort()

    ans = 0

    size = 0
    last = None

    for n in nums:
        if last is None:
            last = n
            size = 1
        elif n == last + 1:
            last = n
            size += 1
        elif n == last:  # alternatively: put nums in a set
            continue
        else:
            last = n
            size = 1
        ans = max(ans, size)

    return ans
```

Alternative:

```python
from typing import List

def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    ans = 0

    size = 0
    last = None

    for n in sorted(set(nums)):
        if last is None:
            last = n
            size = 1
        elif n == last + 1:
            last = n
            size += 1
        else:
            last = n
            size = 1
        ans = max(ans, size)

    return ans
```
