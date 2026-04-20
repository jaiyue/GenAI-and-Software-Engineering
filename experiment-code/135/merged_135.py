def can_arrange(arr):
    """Return the largest index i where arr[i] < arr[i-1], or -1 if none."""
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return i
    return -1

