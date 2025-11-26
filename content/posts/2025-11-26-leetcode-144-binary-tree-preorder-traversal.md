---
title: "LeetCode #144: Binary Tree Preorder Traversal"
date: 2025-11-26T00:08:23-03:00
tags:
  - coding
rss: false
---

[LeetCode #144: Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal):

Sequence:

- current node
- left
- right

## Recursive

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
```
