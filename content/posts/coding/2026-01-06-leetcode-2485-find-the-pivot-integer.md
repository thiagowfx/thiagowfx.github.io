---
title: "LeetCode #2485: Find the Pivot Integer"
date: 2026-01-06T03:40:23-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #2485: Find the Pivot Integer](https://leetcode.com/problems/find-the-pivot-integer):

```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        def s(n):
            return (n * (n + 1)) // 2

        for x in range(1, n + 1):
            if s(x) == (s(n) - s(x) + x):
                return x

        return -1
```

With binary search:

```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        def s(n):
            return (n * (n + 1)) // 2

        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2

            sleft = s(mid)
            sright = (s(n) - s(mid) + mid)

            if sleft == sright:
                return mid
            elif sleft < sright:
                left = mid + 1
            else:
                right = mid - 1

        return -1
```
