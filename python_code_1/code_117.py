Here's a concise implementation that counts consonants (treating y as a consonant):

def select_words(s, n):
    """Given a string s and a natural number n, return list of words that contain exactly n consonants."""
    if not s:
        return []
    vowels = set('aeiouAEIOU')
    result = []
    for word in s.split():
        consonant_count = sum(1 for ch in word if ch.isalpha() and ch not in vowels)
        if consonant_count == n:
            result.append(word)
    return result

