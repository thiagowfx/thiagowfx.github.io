---
title: "LeetCode #314: Binary Tree Vertical Order Traversal"
date: 2026-01-03T02:28:59-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #314: Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal):

## This is **wrong**

`xy = {}` collides in test case #2.

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []

        # (x, y) -> node
        xy = {}
        # node -> (x, y)
        n = {}

        queue = deque([root])
        xy[(0, 0)] = root
        n[root] = (0, 0)

        while queue:
            node = queue.popleft()
            (x, y) = n[node]

            if node.left:
                queue.append(node.left)
                n[node.left] = (x - 1, y + 1)
                xy[(x - 1, y + 1)] = node.left

            if node.right:
                queue.append(node.right)
                n[node.right] = (x + 1, y + 1)
                xy[(x + 1, y + 1)] = node.right

        x_prev = None
        col = []

        # (-1, 1)
        # --
        # (0, 0)
        # (0, 2)

        for (x, y) in sorted(xy.keys()):
            print(x, y, xy[(x, y)].val)
            if x_prev is None or x != x_prev:
                if len(col) > 0:
                    ans.append(col)
                col = [xy[(x, y)].val]
                x_prev = x
            else:
                col.append(xy[(x, y)].val)

        if col:
            ans.append(col)

        return ans
```

## This is **right**

We only need to care about the column.

```python
from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # col -> nodes
        cols = defaultdict(list)

        queue = deque([(root, 0)])

        while queue:
            (node, col) = queue.popleft()
            cols[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))

            if node.right:
                queue.append((node.right, col + 1))

        # (-1, 0)
        # --
        # (0, 0)
        # (0, 2)

        # -1: [0]
        # 0: [0, 2]

        return [cols[col] for col in sorted(cols.keys())]
```
