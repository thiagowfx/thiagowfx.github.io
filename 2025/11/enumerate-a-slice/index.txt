
Pick your poison:

No `enumerate`:

```python
for i in range(start, len(nums)):
    candidate.append(num)        # include nums[i]
    backtrack(i + 1, candidate)  # recurse on the rest
    candidate.pop()              # backtrack
```

With `enumerate`:

```python
for i, num in enumerate(nums[start:], start=start):
    candidate.append(num)        # include nums[i]
    backtrack(i + 1, candidate)  # recurse on the rest
    candidate.pop()              # backtrack
```

