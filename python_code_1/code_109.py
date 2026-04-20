Here's a concise implementation:

def move_one_ball(arr):
    """Return True if arr can be rotated (right shifts) into non-decreasing order."""
    if not arr:
        return True
    drops = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            drops += 1
            if drops > 1:
                return False
    return True

This counts "descents" in the circular array — at most one descent means the array is a rotation of a sorted sequence.

