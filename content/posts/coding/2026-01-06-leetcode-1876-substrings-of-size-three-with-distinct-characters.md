---
title: "LeetCode #1876: Substrings of Size Three with Distinct Characters"
date: 2026-01-06T16:53:27-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #1876: Substrings of Size Three with Distinct Characters](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters):

```python
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        def good(s):
            return len(s) == 3 and s[0] != s[1] and s[1] != s[2] and s[2] != s[0]

        ans = 0

        for i in range(0, len(s) - 2):
            ans += good(s[i:i + 3])

        return ans
```
