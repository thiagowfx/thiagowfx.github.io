---
title: "LeetCode #247: Strobogrammatic Number II"
date: 2025-12-25T05:55:33-03:00
categories:
  - coding
---

[LeetCode #247: Strobogrammatic Number II](https://leetcode.com/problems/strobogrammatic-number-ii):

```python
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # special: 0, 1, 8: auto-symmetric
        # special: 6, 9: complement-symmetric

        ans = []

        m = {
            '0': '0',
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6',
        }

        def backtrack(n, s, t, first):
            if n < 0:
                return

            if n == 0:
                if s + t:
                    ans.append(s + t)
                return

            if n == 1:
                for c in m.keys() - set('69'):
                    ans.append(s + c + t)
                return

            for c in m.keys():
                if c == '0' and first:
                    continue
                backtrack(n - 2, s + c, m[c] + t, False)

        backtrack(n, "", "", True)

        return ans
```

Alternatively:

```python
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # special: 0, 1, 8: auto-symmetric
        # special: 6, 9: complement-symmetric

        ans = []

        m = {
            '0': '0',
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6',
        }

        def backtrack(n, s, t, first):
            if n < 0:
                return

            if n == 0:
                if s + t:
                    ans.append(s + t)
                return

            for c in m.keys():
                if n == 1 and c not in '69':
                    backtrack(n - 1, s + c, t, False)

                if c == '0' and first:
                    continue
                backtrack(n - 2, s + c, m[c] + t, False)

        backtrack(n, "", "", True)

        return ans
```
