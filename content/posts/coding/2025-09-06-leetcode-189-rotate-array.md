---
title: "LeetCode #189: Rotate Array"
date: 2025-09-06T20:18:36+02:00
categories:
  - coding
---

[LeetCode #189: Rotate Array](https://leetcode.com/problems/rotate-array/):

## Easy

Use another list (`v`) for aux.

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
      # Input: nums = [1,2,3,4,5,6,7], k = 3
      # Output (v): [5,6,7,1,2,3,4]
      #
      # v[0] = nums[7 - k + 0]
      # v[1] = nums[7 - k + 1]

      v = [None] * len(nums)

      for i in range(len(nums)):
        v[i] = nums[(len(nums) + i - k) % len(nums)]

      nums[:] = v
```

Or we can populate the aux list from the perspective of `nums`:

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
      v = [None] * len(nums)

      for i, n in enumerate(nums):
        v[(k + i) % len(nums)] = n

      nums[:] = v
```

## Optimal

We can solve it by slicing + reversing the input tactically a couple of times:

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
      # Input: nums = [1,2,3,4,5,6,7], k = 3
      # Output: [5,6,7,1,2,3,4]

      # [1,2,3,4,5,6,7] -> in-place reverse the first len(nums) - k elements
      # [4,3,2,1,5,6,7] -> in-place reverse the last k elements
      # [4,3,2,1,7,6,5] -> in-place reverse the entire list
      # [5,6,7,1,2,3,4]

      nums[:len(nums) - k] = reversed(nums[:len(nums) - k])
      nums[len(nums) - k:] = reversed(nums[len(nums) - k:])
      nums.reverse()
```

For the last statement, `nums[:] = nums[::-1]` works too. No need to memorize
`.reverse()`. You could also do `nums[:] = reversed(nums)`.
