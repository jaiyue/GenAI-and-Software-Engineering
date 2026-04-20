def split_words(txt):
    if any(c.isspace() for c in txt):
        return txt.split()
    if ',' in txt:
        return txt.split(',')
    return sum(1 for ch in txt if 'a' <= ch <= 'z' and ((ord(ch) - ord('a')) % 2 == 1))

