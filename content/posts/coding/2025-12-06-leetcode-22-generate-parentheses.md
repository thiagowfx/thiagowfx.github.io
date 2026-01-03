---
title: "LeetCode #22: Generate Parentheses"
date: 2025-12-06T03:58:02-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #22: Generate Parentheses](https://leetcode.com/problems/generate-parentheses):

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(n, o, s):
            assert n >= 0

            if n == 0:
                assert s
                ans.append(s + ')' * o)
                return

            # (
            backtrack(n - 1, o + 1, s + '(')

            # )
            if o > 0:
                backtrack(n, o - 1, s + ')')

        backtrack(n, 0, "")

        return ans
```

In each node, decide whether to add '(' or ')'.

`n` keeps track of available '('.

`o` keeps track of available ')'.

Strings in Python are immutable, making it easier to backtrack.

If we used an array, then we would have to employ a pattern like this:

```python
s.append('(')
backtrack(n - 1, o + 1, s)
s.pop()
```
