---
title: "LeetCode #3370: Smallest Number With All Set Bits"
date: 2026-01-06T19:40:00-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #3370: Smallest Number With All Set Bits](https://leetcode.com/problems/smallest-number-with-all-set-bits):

```python
class Solution:
    def smallestNumber(self, n: int) -> int:
        return n | (1 << n.bit_length()) - 1
```
