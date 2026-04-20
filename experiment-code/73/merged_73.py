def smallest_change(arr):
    """
    Given an array arr of integers, return the minimum number of single-element changes
    required to make the array a palindrome.
    """
    n = len(arr)
    # Each mismatched pair (i, n-1-i) requires one change.
    return sum(1 for i in range(n // 2) if arr[i] != arr[n - 1 - i])

