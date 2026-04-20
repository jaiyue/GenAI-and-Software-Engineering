def histogram(test):
    from collections import Counter
    parts = test.split()
    if not parts:
        return {}
    counts = Counter(parts)
    max_count = max(counts.values())
    return {k: v for k, v in counts.items() if v == max_count}

This counts the space-separated tokens and returns only those with the maximum frequency (empty input returns {}).

