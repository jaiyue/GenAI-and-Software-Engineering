Searching the codebase for the is_bored function to edit and reporting intent "Exploring codebase".

Use regex to split by sentence delimiters and count sentences whose first word is exactly "I" (using a word boundary).

```python
import re

def is_bored(S):
    parts = re.split(r'[.?!]', S)
    count = 0
    for p in parts:
        p = p.lstrip()
        if p and re.match(r'^I\b', p):
            count += 1
    return count
```

