---
title: "LeetCode #701: Insert into a Binary Search Tree"
date: 2025-12-31T18:40:50-03:00
tags:
  - coding
rss: false
---

[LeetCode #701: Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree):

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        parent = None
        last = None
        node = root
        assert node.val != val

        while node:
            parent = node
            if node.val > val:
                node = node.left
                last = 'left'
            elif node.val < val:
                node = node.right
                last = 'right'

        if last == 'left':
            parent.left = TreeNode(val)
        elif last == 'right':
            parent.right = TreeNode(val)
        else:
            raise Exception

        return root
```
