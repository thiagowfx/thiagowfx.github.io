---
title: "LeetCode #1180: Count Substrings with Only One Distinct"
date: 2026-01-06T13:49:04-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #1180: Count Substrings with Only One Distinct](https://leetcode.com/problems/count-substrings-with-only-one-distinct):

```python
class Solution:
    def countLetters(self, s: str) -> int:
        def f(n):
            # if n == 1:
            #     return 1
            # if n == 2:
            #     return 3
            # if n == 3:
            #     return 6
            # if n == 4:
            #     return 10
            return (n * (n + 1)) // 2

        ans = 0

        prev = None
        q = 0
        for c in s:
            # aaa b
            if c != prev:
                ans += f(q)

                prev = c
                q = 1
            else:
                ## prev = c
                q += 1

        ans += f(q)

        return ans
```
