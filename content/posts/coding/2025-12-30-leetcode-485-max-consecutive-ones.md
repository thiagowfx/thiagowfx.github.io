---
title: "LeetCode #485: Max Consecutive Ones"
date: 2025-12-30T05:32:45-03:00
rss: false
categories:
  - coding
---

[LeetCode #485: Max Consecutive Ones](https://leetcode.com/problems/leetcode-#485:-max-consecutive-ones):

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0

        prev = 0
        for num in nums:
            if num == 0:
                prev = False

            elif num == 1:
                prev += 1
                ans = max(ans, prev)

        return ans
```
