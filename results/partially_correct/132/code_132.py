Here's a concise implementation — it looks for the subsequence "[[]]" (two '[' then two ']' in order):

def is_nested(string):
    first = string.find('[')
    if first == -1:
        return False
    second = string.find('[', first + 1)
    if second == -1:
        return False
    third = string.find(']', second + 1)
    if third == -1:
        return False
    fourth = string.find(']', third + 1)
    return fourth != -1

This returns True iff a nested pair "[[]]" exists as a subsequence.

