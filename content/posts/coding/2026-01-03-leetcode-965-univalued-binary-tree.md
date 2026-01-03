---
title: "LeetCode #965: Univalued Binary Tree"
date: 2026-01-03T03:07:23-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #965: Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree):

With a single function:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.left and root.val != root.left.val:
            return False

        if root.right and root.val != root.right.val:
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
```

With a `dfs` helper – there's no reason to do this though:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True

            if root.left and root.val != root.left.val:
                return False

            if root.right and root.val != root.right.val:
                return False

            return dfs(root.left) and dfs(root.right)

        return dfs(root)
```
