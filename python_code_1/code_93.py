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

# Quick check
if __name__ == "__main__":
    print(encode('test'))               # TGST
    print(encode('This is a message'))  # tHKS KS C MGSSCGG

