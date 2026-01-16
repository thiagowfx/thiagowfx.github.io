---
title: "LeetCode #23: Merge k Sorted Lists"
date: 2026-01-15T23:20:52-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #23: Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists):

Heap of ListNodes:

```python
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other: HeapNode):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        prehead = ListNode(None)

        curr = prehead
        heap = []

        for lst in lists:
            if lst:
                heapq.heappush(heap, HeapNode(lst))

        while heap:
            # find next element: val
            next_heap_node = heapq.heappop(heap)
            next_node = next_heap_node.node

            curr.next = ListNode(next_node.val)
            curr = curr.next

            next_node = next_node.next
            if next_node:
                heapq.heappush(heap, HeapNode(next_node))


        head = prehead.next
        return head
```
