def intersection(interval1, interval2):
    s1, e1 = interval1
    s2, e2 = interval2
    start = max(s1, s2)
    end = min(e1, e2)
    length = end - start
    if length < 2:
        return "NO"
    if length % 2 == 0:
        return "YES" if length == 2 else "NO"
    i = 3
    while i * i <= length:
        if length % i == 0:
            return "NO"
        i += 2
    return "YES"

