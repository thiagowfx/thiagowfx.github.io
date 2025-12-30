---
title: "LeetCode #922: Sort Array By Parity II"
date: 2025-12-30T19:43:29-03:00
tags:
  - coding
rss: false
---

[LeetCode #922: Sort Array By Parity II](https://leetcode.com/problems/leetcode-#922:-sort-array-by-parity-ii):

```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        def interleave(a, b):
            assert len(a) == len(b)
            ans = []
            for (x, y) in zip(a, b):
                ans += [x, y]
            return ans

        return interleave(
            [num for num in nums if num % 2 == 0],
            [num for num in nums if num % 2 == 1],
        )
```
