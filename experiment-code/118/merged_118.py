def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    n = len(word)
    if n < 3:
        return ""
    for i in range(n - 2, 0, -1):  # i from n-2 down to 1 (can't be first or last)
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i]
    return ""
