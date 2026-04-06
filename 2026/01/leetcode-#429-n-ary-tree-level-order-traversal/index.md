---
title: "LeetCode #429: N-ary Tree Level Order Traversal"
url: https://perrotta.dev/2026/01/leetcode-%23429-n-ary-tree-level-order-traversal/
last_updated: 2026-01-03
---


[LeetCode #429: N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal):

```python
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        ans = []

        queue = deque([root])

        while queue:
            n = len(queue)
            row = []

            for _ in range(n):
                node = queue.popleft()
                row.append(node.val)

                for child in node.children:
                    assert child
                    queue.append(child)

            ans.append(row)

        return ans
```

