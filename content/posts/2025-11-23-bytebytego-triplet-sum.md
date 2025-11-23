---
title: "ByteByteGo: Triplet Sum"
date: 2025-11-23T17:00:21-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: Triplet Sum](https://bytebytego.com/exercises/coding-patterns/two-pointers/triplet-sum):

```python
from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    sequence = sorted(nums)

    ans = []

    for ia, a in enumerate(sequence):
        if a > 0:  # positive numbers cannot add up to zero
            break

        if ia > 0 and sequence[ia - 1] == sequence[ia]:  # prevent duplicates
            continue

        ib = ia + 1
        ic = len(sequence) - 1

        while ib < ic:
            b = sequence[ib]
            c = sequence[ic]

            target = -a
            if (b + c) == target:
                ans.append([a, b, c])
                ib += 1
                ic -= 1

                # keep going, preventing duplicates
                while ib < ic and sequence[ib - 1] == sequence[ib]:
                    ib += 1
                while ib < ic and sequence[ic + 1] == sequence[ic]:
                    ic -= 1
            elif (b + c) < target:
                ib += 1
            else:
                ic -=1

    return ans
```

Time complexity: O(n^2)
