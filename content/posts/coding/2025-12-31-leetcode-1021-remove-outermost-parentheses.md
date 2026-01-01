---
title: "LeetCode #1021: Remove Outermost Parentheses"
date: 2025-12-31T02:06:03-03:00
categories:
  - coding
---

[LeetCode #1021: Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses):

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # (()())(())
        open = []

        remove = set()

        for i, c in enumerate(s):
            if c == '(':
                open.append(i)
            elif c == ')':
                d = open.pop()
                if len(open) == 0:
                    remove.add(d)
                    remove.add(i)

        ans = []
        for i, c in enumerate(s):
            if i not in remove:
                ans.append(c)
        return ''.join(ans)
```
