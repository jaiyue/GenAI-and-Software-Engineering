import re

def is_bored(S):
    parts = re.split(r'[.?!]', S)
    count = 0
    for p in parts:
        p = p.lstrip()
        if p and re.match(r'^I\b', p):
            count += 1
    return count
