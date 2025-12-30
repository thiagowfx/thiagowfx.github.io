---
title: "LeetCode #26: Remove Duplicates from Sorted Array"
date: 2025-12-30T10:13:34-03:00
tags:
  - coding
rss: false
---

[LeetCode #26: Remove Duplicates from Sorted Array](https://leetcode.com/problems/leetcode-#26:-remove-duplicates-from-sorted-array):

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        seen = set()

        prev = None
        for i, num in enumerate(nums):
            ## 1 2 2 3 4 4
            ##     p

            if prev is None:
                prev = num
                p += 1
            else:
                if prev != num:
                    prev = num
                    nums[p] = nums[i]
                    p += 1
                ## a duplicate
                ## else:
                    ## prev = num
                    ## p += 0

        return p
```
