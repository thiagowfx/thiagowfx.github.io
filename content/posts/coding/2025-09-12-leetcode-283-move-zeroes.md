---
title: "LeetCode #283: Move Zeroes"
date: 2025-09-12T23:07:57+02:00
categories:
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

**Two pointers**:

- `i` scans the entire list once
- `j` tracks the position of the next zero to swap

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 5, 0, 0, 1, 0, 3, 12
        #          i
        #    j

        j = None

        for i, num in enumerate(nums):
            if num != 0:
                if j is not None:
                    assert j < i
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            else:
                if j is None:
                    j = i
```
