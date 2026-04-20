Here's a concise implementation that matches the examples:

def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    if not txt[-1].isalpha():
        return False
    # find start index of the token that contains the last character
    i = len(txt) - 1
    j = i
    while j >= 0 and txt[j] != ' ':
        j -= 1
    token = txt[j+1:i+1]
    return len(token) == 1

This returns True when the string ends with a single-letter token (separated by spaces) and False otherwise.

