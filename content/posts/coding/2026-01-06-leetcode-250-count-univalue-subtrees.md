---
title: "LeetCode #250: Count Univalue Subtrees"
date: 2026-01-06T03:15:55-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #250: Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees):

193 / 201 testcases passed:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # a leaf
        if not root.left and not root.right:
            return 1

        if not root.left and root.right:
            w = self.countUnivalSubtrees(root.right)

            if root.val == root.right.val:
                if w > 0:
                    return 1 + w
            return w

        if root.left and not root.right:
            w = self.countUnivalSubtrees(root.left)

            if root.val == root.left.val:
                if w > 0:
                    return 1 + w
            return w

        return self.countUnivalSubtrees(root.left) + self.countUnivalSubtrees(root.right) + (1 if (root.val == root.left.val == root.right.val) else 0)
```

Pass:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def univalue(node): ## -> (int, bool)
            if not node:
                return (0, False)

            # a leaf
            if not node.left and not node.right:
                return (1, True)

            if not node.left and node.right:
                w = univalue(node.right)

                if node.val == node.right.val:
                    if w[1]:
                        return (1 + w[0], True)
                return (w[0], False)

            if node.left and not node.right:
                w = univalue(node.left)

                if node.val == node.left.val:
                    if w[1]:
                        return (1 + w[0], True)
                return (w[0], False)

            w1 = univalue(node.left)
            w2 = univalue(node.right)
            terminal = (node.val == node.left.val == node.right.val) and w1[1] and w2[1]

            return (w1[0] + w2[0] + int(terminal), terminal)

        return univalue(root)[0]
```
