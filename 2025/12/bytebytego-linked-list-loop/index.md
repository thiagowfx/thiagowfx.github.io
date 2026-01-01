
[ByteByteGo: Linked List Loop](https://bytebytego.com/exercises/coding-patterns/fast-and-slow-pointers/detect-linked-list-loops):

Slow and fast pointers.

```python
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_loop(head: ListNode) -> bool:
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        slow = slow.next

        if not fast or not fast.next:
            return False

        fast = fast.next.next

    return True
```

