---
title: "Leetcode #80: Duplicate From Sorted Array II"
date: 2025-09-05T20:29:31+02:00
tags:
  - coding
---

[LeetCode #80: Duplicate From Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/):

[Previously]({{< ref "2025-09-03-leetcode-26-duplicate-from-sorted-array.md"
>}}). Now each element can appear at most twice.

## Elegant

Keeping track of a counter is the most straightforward way to do so.

I like to use `defaultdict` for that.

```python
from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      counter = defaultdict(int)

      for i, el in reversed(enumerate(nums)):
        counter[el] += 1
        if counter[el] > 2:
          del nums[i]

      return len(nums)
```

## Optimal

Can we do it without allocating a separate counter, with `O(1)` extra memory?

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      for i in range(len(nums))[::-1][:-2]:
        if nums[i] == nums[i - 1] == nums[i - 2]:
          del nums[i]

      return len(nums)
```
