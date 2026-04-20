def sorted_list_sum(lst):
    """Remove strings with odd lengths and return the remaining strings sorted
    ascending by length and alphabetically for equal lengths."""
    evens = [s for s in lst if len(s) % 2 == 0]
    return sorted(evens, key=lambda s: (len(s), s))

# Examples:
# assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
# assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

