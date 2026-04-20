def find_max(words):
    if not words:
        return ""
    counts = {w: len(set(w)) for w in words}
    max_count = max(counts.values())
    candidates = [w for w, c in counts.items() if c == max_count]
    return min(candidates)

