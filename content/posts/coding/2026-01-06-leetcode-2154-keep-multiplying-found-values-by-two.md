---
title: "LeetCode #2154: Keep Multiplying Found Values by Two"
date: 2026-01-06T20:43:08-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #2154: Keep Multiplying Found Values by Two](https://leetcode.com/problems/keep-multiplying-found-values-by-two):

```python
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)

        while True:
            if original in s:
                original <<= 1
            else:
                break

        return original
```
