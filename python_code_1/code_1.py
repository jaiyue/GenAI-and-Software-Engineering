Searching the repository for the function to update and reporting intent.

from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    results: List[str] = []
    current: List[str] = []
    depth = 0

    for ch in paren_string:
        if ch == ' ':
            continue
        if ch == '(':
            depth += 1
            current.append(ch)
        elif ch == ')':
            depth -= 1
            current.append(ch)
            if depth == 0:
                results.append(''.join(current))
                current = []
        else:
            # ignore any other characters
            continue

    return results

Implemented: removes spaces and collects balanced parenthesis groups into a list.

