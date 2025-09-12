---
title: "LeetCode #283: Move Zeroes"
date: 2025-09-12T23:07:57+02:00
tags:
  - coding
---

[LeetCode #283: Move Zeroes](https://leetcode.com/problems/move-zeroes/):

## Low-stress

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [num for num in nums if num != 0] + [num for num in nums if num == 0]
```

Or even:

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zeroes = [num for num in nums if num != 0]
        nums[:] = non_zeroes + [0] * (len(nums) - len(non_zeroes))
```

It's in-place, but it creates a new list – O(n) memory.

We can do better, with O(1) memory.

## In-place

TODO.
