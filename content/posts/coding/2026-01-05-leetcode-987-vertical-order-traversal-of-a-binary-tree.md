---
title: "LeetCode #987: Vertical Order Traversal of a Binary Tree"
date: 2026-01-05T18:44:29-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #987: Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree):

```python
from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        columns = defaultdict(list)
        ## row = 0

        queue = deque([(root, 0)])  ## col = 0

        while queue:
            n = len(queue)
            ## row += 1

            columns_incoming = defaultdict(list)

            for _ in range(n):
                (node, col) = queue.popleft()

                columns_incoming[col].append(node.val)

                if node.left:
                    queue.append((node.left, col - 1))

                if node.right:
                    queue.append((node.right, col + 1))

            for col in columns_incoming:
                columns[col].extend(sorted(columns_incoming[col]))

        ans = []

        for nodes in sorted(columns.keys()):
            ans.append((columns[nodes]))

        return ans
```
