---
title: "ByteByteGo: Remove the Kth Last Node From a Linked List"
url: https://perrotta.dev/2025/12/bytebytego-remove-the-kth-last-node-from-a-linked-list/
last_updated: 2026-01-03
---


[ByteByteGo: Remove the Kth Last Node From a Linked List](https://bytebytego.com/exercises/coding-patterns/linked-lists/remove-the-kth-last-node-from-a-linked-list):

```python
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    pivot = head
    back = head

    for _ in range(k):
        if pivot:
            pivot = pivot.next
        else:
            return head

    if not pivot:
        return head.next

    while pivot.next:
        pivot = pivot.next
        back = back.next

    back.next = back.next.next

    return head
```

