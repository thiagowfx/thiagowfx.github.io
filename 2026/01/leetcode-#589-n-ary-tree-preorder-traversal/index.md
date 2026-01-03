
[LeetCode #589: N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal):

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        def dfs(node):
            if node:
                ans.append(node.val)
                for child in node.children:
                    dfs(child)

        dfs(root)

        return ans
```

