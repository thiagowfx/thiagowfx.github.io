---
title: "LeetCode #268: Missing Number"
date: 2025-12-24T17:26:11-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #268: Missing Number](https://leetcode.com/problems/missing-number):

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if i != num:
                return i

        return len(nums)
```

Without `sort`:

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) // 2
        return total - sum(nums)
```
