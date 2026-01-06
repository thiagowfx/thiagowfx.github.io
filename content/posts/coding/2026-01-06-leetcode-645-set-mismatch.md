---
title: "LeetCode #645: Set Mismatch"
date: 2026-01-06T19:23:08-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #645: Set Mismatch](https://leetcode.com/problems/set-mismatch):

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        s = set(nums)
        t = set(range(1, n + 1))

        missing = (t - s).pop()
        duplicate = Counter(nums).most_common(1)[0][0]

        return [duplicate, missing]
```
