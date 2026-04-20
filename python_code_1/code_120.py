def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    import heapq
    # heapq.nlargest handles k==0 and duplicates correctly; sort ascending before returning
    return sorted(heapq.nlargest(k, arr))

