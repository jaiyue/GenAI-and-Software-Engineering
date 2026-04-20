Here's a simple implementation that shifts letters forward by 4 (wraps z→d); non-letters are unchanged.

def encrypt(s):
    """Shift alphabetic characters forward by 4 places (Caesar cipher)."""
    res = []
    for ch in s:
        if 'a' <= ch <= 'z':
            res.append(chr((ord(ch) - ord('a') + 4) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            res.append(chr((ord(ch) - ord('A') + 4) % 26 + ord('A')))
        else:
            res.append(ch)
    return ''.join(res)

