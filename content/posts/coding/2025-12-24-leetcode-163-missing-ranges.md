---
title: "LeetCode #163: Missing Ranges"
date: 2025-12-24T04:31:59-03:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #163: Missing Ranges](https://leetcode.com/problems/missing-ranges):

```python
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        assert nums == sorted(nums)

        nums = [lower - 1] + nums + [upper + 1]

        ans = []

        for (a, b) in zip(nums[:-1], nums[1:]):
            assert b >= a

            if (b - a) > 1:
                ans.append([a + 1, b - 1])

        return ans
```

This:

```python
nums = [lower - 1] + nums + [upper + 1]
```

...is a workaround to account for the outer ranges within the same loop.

Alternatively, we could handcraft `[lower, nums[0] - 1]` and `[nums[-1] + 1,
upper]` as needed.
