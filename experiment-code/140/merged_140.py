import re

def fix_spaces(text):
    """
    Replace sequences of spaces: any run of 3+ spaces -> '-', any remaining single space -> '_'.
    """
    # replace runs of 3 or more spaces with a single '-'
    s = re.sub(r' {3,}', '-', text)
    # replace remaining single spaces with underscores
    return s.replace(' ', '_')

