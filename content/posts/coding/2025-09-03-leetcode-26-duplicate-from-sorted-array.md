---
title: "LeetCode #26: Duplicate From Sorted Array"
date: 2025-09-03T20:00:06+02:00
tags:
  - dev

categories:
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

We need to modify the original list in-place. Using a two-pointer approach, we iterate through the array and only move forward when we find a different element:

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        prev = None

        for i, num in enumerate(nums):
            if prev is None:
                prev = num
                p += 1
            else:
                if prev != num:
                    prev = num
                    nums[p] = nums[i]
                    p += 1

        return p
```

The algorithm maintains a pointer `p` that tracks where the next unique element should be placed. We iterate through all elements, and whenever we find a new unique value, we place it at position `p` and increment the pointer.

For example with `[1, 2, 2, 3, 4, 4]`:

- We place 1 at position 0, 2 at position 1, 3 at position 2, 4 at position 3
- Return 4 (the length of unique elements)

## Alternative: Backwards approach

Another way is to go backwards and remove duplicates as we find them:

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums))[::-1][:-1]:
            if nums[i] == nums[i - 1]:
                del nums[i]

        return len(nums)
```
