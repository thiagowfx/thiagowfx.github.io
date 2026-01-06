---
title: "LeetCode #1018: Binary Prefix Divisible By 5"
date: 2026-01-06T20:40:49-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #1018: Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5):

```python
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []

        n = 0

        for i, num in enumerate(nums):
            n = n * 2 + num
            ans.append(n % 5 == 0)

        return ans
```
