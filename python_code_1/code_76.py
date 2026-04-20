Here's a concise implementation that handles the common edge cases (n == 0, 1, -1) and checks by repeated division:

```python
def is_simple_power(x, n):
    if x == 1:
        return True
    if n == 1:
        return False
    if n == 0:
        return x == 0
    if n == -1:
        return x in (1, -1)
    if x == 0:
        return n == 0

    # For other n, repeatedly divide while divisible
    while x % n == 0:
        x //= n
    return x == 1
```

This returns True when there exists an integer k >= 0 with n**k == x (matching the examples).

