def count_nums(arr):
    count = 0
    for n in arr:
        s = str(abs(n))
        if n < 0:
            total = -int(s[0]) + sum(int(ch) for ch in s[1:]) if s else 0
        else:
            total = sum(int(ch) for ch in s) if s else 0
        if total > 0:
            count += 1
    return count

