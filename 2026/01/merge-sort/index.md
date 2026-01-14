
```python
def merge_sort(a):
    if len(a) < 2: ## [0, 1]
        return a

    ## (0 1) (2 3)
    ##        m
    ##
    ## (0 1) (2 3 4)
    ##        m

    mid = len(a) // 2

    left = a[:mid]
    right = a[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    ans = []

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    ans.extend(left[i:])
    ans.extend(right[j:])

    return ans

a = list(range(10))[::-1]
assert merge_sort(a) == list(range(10))
```

