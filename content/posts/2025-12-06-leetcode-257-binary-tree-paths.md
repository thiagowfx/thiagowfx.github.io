---
title: "LeetCode #257: Binary Tree Paths"
date: 2025-12-06T04:30:43-03:00
tags:
  - coding
rss: false
---

[LeetCode #257: Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths):

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def backtrack(node, path: list):
            if not node:
                return

            if not node.left and not node.right:
                path.append(node.val)
                ans.append('->'.join(str(val) for val in path))
                path.pop()
                return

            if node.left:
                path.append(node.val)
                backtrack(node.left, path)
                path.pop()

            if node.right:
                path.append(node.val)
                backtrack(node.right, path)
                path.pop()

        backtrack(root, [])

        return ans
```

One pitfall, this fails:

```python
if node.left:
        path.append(node.val)
        backtrack(node.left, path.copy().append(node.val))  # or path[:]
        path.pop()
```

Whereas this doesn't:

```python
if node.left:
    path.append(node.val)
    backtrack(node.left, path)
    path.pop()
```

Why? Because `list.append()` modifies the list in place and returns `None`.
