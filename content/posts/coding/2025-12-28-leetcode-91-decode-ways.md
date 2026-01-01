---
title: "LeetCode #91: Decode Ways"
date: 2025-12-28T20:38:44-03:00
categories:
  - coding
---

[LeetCode #91: Decode Ways](https://leetcode.com/problems/decode-ways):

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        from functools import cache

        @cache
        def solve(n):
            if n < 0:
                return 1

            if n == 0:
                if s[n] in "123456789":
                    return 1
                else:
                    return 0

            ans = 0

            # take one char, s[n]
            if s[n] in "123456789":
                ans += solve(n - 1)

            # take two chars, s[n - 1] and s[n]
            if s[n - 1] in "12" and 10 <= int(s[n - 1] + s[n]) <= 26:
                ans += solve(n - 2)

            return ans

        return solve(len(s) - 1)
```
