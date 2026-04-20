def by_length(arr):
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    filtered = [x for x in arr if isinstance(x, int) and 1 <= x <= 9]
    filtered.sort()
    filtered.reverse()
    return [names[x - 1] for x in filtered]

