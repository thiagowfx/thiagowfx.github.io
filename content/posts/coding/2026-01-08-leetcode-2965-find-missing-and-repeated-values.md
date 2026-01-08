---
title: "LeetCode #2965: Find Missing and Repeated Values"
date: 2026-01-08T00:24:02-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #2965: Find Missing and Repeated Values](https://leetcode.com/problems/find-missing-and-repeated-values):

Two sets:

```python
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        numbers = set(range(1, len(grid) ** 2 + 1))

        a = b = None

        for row in grid:
            for num in row:
                if num in seen:
                    a = num
                    continue
                seen.add(num)
                numbers.discard(num)

        assert len(numbers) == 1
        b = numbers.pop()

        return [a, b]
```
