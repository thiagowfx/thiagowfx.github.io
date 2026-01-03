---
title: "LeetCode #1299: Replace Elements with Greatest Element on Right Side"
date: 2025-12-30T10:52:29-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #1299: Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/leetcode-#1299:-replace-elements-with-greatest-element-on-right-side):

```python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev_max = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], prev_max = prev_max, max(prev_max, arr[i])
        return arr
```
