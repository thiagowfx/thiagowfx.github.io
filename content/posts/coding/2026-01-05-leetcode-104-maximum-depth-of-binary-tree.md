---
title: "LeetCode #104: Maximum Depth of Binary Tree"
date: 2026-01-05T19:05:12-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree):

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```
