from collections import Counter

def search(lst):
    cnt = Counter(lst)
    candidates = [num for num, freq in cnt.items() if num > 0 and freq >= num]
    return max(candidates) if candidates else -1
