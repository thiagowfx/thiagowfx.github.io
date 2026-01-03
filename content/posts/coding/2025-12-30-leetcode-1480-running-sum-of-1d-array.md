---
title: "LeetCode #1480: Running Sum of 1d Array"
date: 2025-12-30T04:58:24-03:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #1480: Running Sum of 1d Array](https://leetcode.com/problems/leetcode-#1480:-running-sum-of-1d-array):

```python
from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))
```

Primitives:

```python
from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []

        acc = 0
        for num in nums:
            acc += num
            ans.append(acc)

        return ans
```
