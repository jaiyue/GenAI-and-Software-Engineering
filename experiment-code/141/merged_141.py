def file_name_check(file_name):
    # No more than three digits anywhere in the name
    if sum(ch.isdigit() for ch in file_name) > 3:
        return 'No'
    # Exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    name, ext = file_name.split('.')
    # Name before dot must be non-empty and start with a latin letter
    if not name or not name[0].isalpha():
        return 'No'
    # Extension must be one of the allowed values
    if ext not in ('txt', 'exe', 'dll'):
        return 'No'
    return 'Yes'

