---
title: "sorting algorithms"
date: 2026-01-14T03:30:25-03:00
tags:
  - dev
categories:
  - coding
---

```python
def swap(a, x, y):
    a[x], a[y] = a[y], a[x]

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                swap(a, i, j)

a = list(range(10)[::-1])
bubble_sort(a)
assert a == list(range(10))

def selection_sort(a):
    for i in range(len(a) - 1):
        ## el = min(a[i + 1:])
        ## eli = a.index(el)
        el = float('inf')
        eli = None
        for j in range(i + 1, len(a)):
            if a[j] < el:
                el = a[j]
                eli = j
        if eli:
            if a[i] > a[eli]:
                swap(a, i, eli)

a = list(range(10)[::-1])
selection_sort(a)
assert a == list(range(10))

def merge_sort_inplace(a):
    a[:] = merge_sort(a)

def merge_sort(a): ## no indices! (indexes)
    n = len(a)

    if n < 2: ## in [0, 1]
        return a

    # 0 1 2 3 4
    # 0   m   n

    # 0 1 2 3
    # 0 m   n
    mid = n // 2

    ## left: [0, mid - 1]
    ## right: [mid, len(a) - 1]
    A = merge_sort(a[:mid])
    B = merge_sort(a[mid:])

    ## A
    ## 1 4 7
    ##       2 3 6
    ##       B

    return merge(A, B)

def merge(A, B):
    ans = []

    a = 0
    b = 0

    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            ans.append(A[a])
            a += 1
        else:
            ans.append(B[b])
            b += 1

    ans.extend(A[a:])
    ans.extend(B[b:])

    return ans


a = list(range(10)[::-1])
merge_sort_inplace(a)
assert a == list(range(10))

def quick_sort(a):
    if len(a) < 2:
        return
    pivot = a[0]
    left = [x for x in a[1:] if x < pivot]
    right = [x for x in a[1:] if x >= pivot]

    quick_sort(left)
    quick_sort(right)
    a[:] = left + [pivot] + right

a = list(range(10)[::-1])
quick_sort(a)
assert a == list(range(10))
```
