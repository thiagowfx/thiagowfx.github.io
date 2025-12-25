---
title: "LeetCode #278: First Bad Version"
date: 2025-12-25T04:50:40-03:00
tags:
  - coding
rss: false
---

[LeetCode #278: First Bad Version](https://leetcode.com/problems/first-bad-version):

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # both inclusive
        p = 1
        q = n

        last = None

        while p < q:
            m = p + (q - p) // 2  # m = (p + q) // 2

            if not isBadVersion(m):
                p = m + 1

            else:
                last = m
                q = m

        if isBadVersion(p):
            return p

        return last

        # a b c d
        # p m   q

        # a b c
        # p m q
```

Beware of off-by-one errors.
