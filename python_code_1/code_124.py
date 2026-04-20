def valid_date(date):
    if not date or not isinstance(date, str):
        return False
    parts = date.split('-')
    if len(parts) != 3:
        return False
    mm, dd, yyyy = parts
    if not (len(mm) == 2 and len(dd) == 2 and len(yyyy) == 4):
        return False
    if not (mm.isdigit() and dd.isdigit() and yyyy.isdigit()):
        return False
    m, d = int(mm), int(dd)
    if m < 1 or m > 12 or d < 1:
        return False
    if m in {1, 3, 5, 7, 8, 10, 12}:
        return d <= 31
    if m in {4, 6, 9, 11}:
        return d <= 30
    # February: allowed up to 29 per specification (no leap-year logic)
    return d <= 29

Implemented validation per the rules: non-empty, mm-dd-yyyy format with two-digit month/day and four-digit year, month/day ranges including Feb max 29.

