
[LeetCode #211: Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure):

```python
from collections import defaultdict

class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        ## "hello"
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        def node_search(node, word: str) -> bool:
            for i, c in enumerate(word):
                if c == '.':
                    for child in node.children.values():
                        if node_search(child, word[i + 1:]):
                            return True
                    return False

                if c not in node.children:
                    return False
                node = node.children[c]

            return node.end

        return node_search(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

