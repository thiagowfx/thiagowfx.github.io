---
title: "LeetCode #1047: Remove All Adjacent Duplicates In String"
date: 2026-01-18T13:37:46-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #1047: Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string):

Initial:

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        ans = []

        for c in s:
            if not stack:
                stack.append(c)
                ans.append(c)
            else:
                if stack[-1] != c:
                    stack.append(c)
                    ans.append(c)
                else:
                    stack.pop()
                    ans.pop()

        return ''.join(ans)
```

Optimized:

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        ans = []

        for c in s:
            if not stack or stack[-1] != c:
                stack.append(c)
                ans.append(c)
            else:
                stack.pop()
                ans.pop()

        return ''.join(ans)
```
