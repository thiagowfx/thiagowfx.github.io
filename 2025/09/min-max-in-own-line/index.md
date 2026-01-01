
This is more readable:

```python
return max(
  # ans1
  {expression 1},
  # ans2
  {expression 2},
)
```

...than this:

```python
return max({expression 1}, {expression 2})
```

And it allows inline comments on each expression.

Trailing commas are perfectly legal.

