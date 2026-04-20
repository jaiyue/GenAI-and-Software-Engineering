def specialFilter(nums):
    """Return count of numbers > 10 whose first and last digits are odd."""
    count = 0
    for n in nums:
        try:
            n_int = int(n)
        except Exception:
            continue
        if n_int > 10:
            s = str(n_int)
            if int(s[0]) % 2 == 1 and int(s[-1]) % 2 == 1:
                count += 1
    return count

