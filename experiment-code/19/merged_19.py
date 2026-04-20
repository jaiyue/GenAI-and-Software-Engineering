from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    word_to_int = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    tokens: List[str] = numbers.split()
    if not tokens:
        return ""

    try:
        tokens.sort(key=lambda w: word_to_int[w])
    except KeyError as e:
        raise ValueError(f"Invalid numeral: {e.args[0]}") from None

    return " ".join(tokens)

