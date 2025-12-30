---
title: "LeetCode #941: Valid Mountain Array"
date: 2025-12-30T10:38:22-03:00
tags:
  - coding
rss: false
---

[LeetCode #941: Valid Mountain Array](https://leetcode.com/problems/leetcode-#941:-valid-mountain-array):

```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        prev = arr[0]
        inc = True

        for i, num in enumerate(arr[1:]):
            if prev == num:
                return False

            if inc:
                if prev < num:
                    prev = num
                    continue
                else:
                    if i == 0:
                        return False
                    prev = num
                    inc = False
            else:
                if num < prev:
                    prev = num
                    continue
                else:
                    return False

        return not inc
```
