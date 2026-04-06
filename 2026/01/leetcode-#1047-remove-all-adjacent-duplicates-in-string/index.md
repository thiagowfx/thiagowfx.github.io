---
title: "LeetCode #1047: Remove All Adjacent Duplicates In String"
url: https://perrotta.dev/2026/01/leetcode-%231047-remove-all-adjacent-duplicates-in-string/
last_updated: 2026-01-18
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

