def encode(message):
    swapped = message.swapcase()
    vowels = set('aeiouAEIOU')
    out = []
    for ch in swapped:
        if ch in vowels:
            out.append(chr(ord(ch) + 2))
        else:
            out.append(ch)
    return ''.join(out)

