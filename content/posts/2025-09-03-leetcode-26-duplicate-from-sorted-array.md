---
title: "LeetCode #26: Duplicate From Sorted Array"
date: 2025-09-03T20:00:06+02:00
tags:
  - coding
---

[LeetCode #26: Duplicate From Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array):

## Naive and elegant

If we can create a new array, it's trivial:

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
```

Initially I thought `list(set(nums))` is enough, but it turns out sets in
Python do not guarantee any order.

`sorted()` returns a list already, there's no need to do `list(sorted())`,
though it wouldn't hurt.

## Optimal

We need to modify the original list in-place. We could create another list and
then copy it to the original list in the end, but let's avoid this approach.

Instead, let's go backwards and remove duplicates as we find them:

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      for i in range(len(nums))[::-1][:-1]:
          if nums[i] == nums[i - 1]:
              del nums[i]

      return len(nums)
```
