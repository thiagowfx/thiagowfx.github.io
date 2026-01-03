
[LeetCode #1506: Find Root of N-Ary Tree](https://leetcode.com/problems/find-root-of-n-ary-tree):

Dictionary:

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # d[val] -> is child?
        d = {}
        # n[val] -> Node
        n = {}

        for node in tree:
            assert node
            n[node.val] = node
            if node.val not in d:
                d[node.val] = False
            for child in node.children:
                d[child.val] = True

        for (val, child) in d.items():
            if not child:
                return n[val]
```

Set:

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        seen = set()

        for node in tree:
            assert node
            for child in node.children:
                seen.add(child.val)

        for node in tree:
            if not node.val in seen:
                return node
```

