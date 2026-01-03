---
title: "LeetCode #590: N-ary Tree Postorder Traversal"
date: 2026-01-03T02:43:02-03:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #590: N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal):

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        def dfs(node):
            if not node:
                return

            for child in node.children:
                dfs(child)

            ans.append(node.val)

        dfs(root)

        return ans
```
