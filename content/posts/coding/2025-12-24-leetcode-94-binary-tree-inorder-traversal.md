---
title: "LeetCode #94: Binary Tree Inorder Traversal"
date: 2025-12-24T03:58:41-03:00
categories:
  - coding
---

[LeetCode #94: Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal):

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)

        inorder(root)

        return ans
```

It feels a bit odd to define `inorder` inside `inorderTraversal`.

My initial solution was:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        self.inorderTraversal(root.left)
        self.ans.append(root.val)
        self.inorderTraversal(root.right)

        return self.ans
```

...but it fails because the leetcode environment reuses `self.ans` across
successive runs.

The editorial uses a sibling helper instead of an inner function:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root):
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if root is not None:
            self.helper(root.left, ans)
            ans.append(root.val)
            self.helper(root.right, ans)
```

...which is OK, but it feels dirty. I don't like passing a reference to `ans`
around. I prefer my original approach.
