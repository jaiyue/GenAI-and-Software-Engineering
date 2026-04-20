Here's a simple implementation that splits the input on whitespace and computes the maximum nesting per group:

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if not paren_string or not paren_string.strip():
        return []

    depths: List[int] = []
    for group in paren_string.split():
        cur = 0
        mx = 0
        for ch in group:
            if ch == '(':
                cur += 1
                if cur > mx:
                    mx = cur
            elif ch == ')':
                cur -= 1
                if cur < 0:
                    # malformed group: treat as zero or clamp
                    cur = 0
        depths.append(mx)
    return depths
```

