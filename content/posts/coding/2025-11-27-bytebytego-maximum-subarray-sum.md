---
title: "ByteByteGo: Maximum Subarray Sum"
date: 2025-11-27T02:51:23-03:00
rss: false
categories:
  - coding
---

[ByteByteGo: Maximum Subarray Sum](https://bytebytego.com/exercises/coding-patterns/dynamic-programming/maximum-subarray-sum):

```python
from typing import List

def maximum_subarray_sum(nums: List[int]) -> int:
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def solve(i, must_take=False):
        if i < 0:
            return 0

        if i == 0:
            if must_take:
                return max(0, nums[i])
            else:
                return nums[i]

        take = nums[i] + solve(i - 1, True)
        if must_take:
            return max(0, take)

        skip = solve(i - 1)
        return max(take, skip)

    return solve(len(nums) - 1)
```
