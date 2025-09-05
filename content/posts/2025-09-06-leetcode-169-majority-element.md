---
title: "Leetcode #169: Majority Element"
date: 2025-09-06T01:37:01+02:00
tags:
  - coding
---

[Leetcode #169: Majority Element](https://leetcode.com/problems/majority-element/):

## Quickly via sorting

It must appear in the middle (`(n - 1) / 2`):

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      return sorted(nums)[(len(nums) - 1) // 2]

    #     1      (n - 1) / 2
    #   a b c d
    #
    #     1
    #   a b c    (n - 1) / 2
```

Because we're sorting the list, this is `O(n * log n)`.

TODO.
