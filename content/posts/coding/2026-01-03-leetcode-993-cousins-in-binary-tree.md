---
title: "LeetCode #993: Cousins in Binary Tree"
date: 2026-01-03T20:08:02-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #993: Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree):

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from functools import cache

        parent = {}

        @cache
        def depth(n, node = root):
            if not node:
                return None

            if node.val == n:
                return 0

            l = depth(n, node.left)
            r = depth(n, node.right)

            if l is not None:
                parent[node.left.val] = node.val
                return 1 + l

            elif r is not None:
                parent[node.right.val] = node.val
                return 1 + r

            return None

        assert root
        parent[root.val] = None

        return depth(x) == depth(y) and parent[x] != parent[y]
```
