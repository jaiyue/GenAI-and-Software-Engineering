Here's a concise implementation:

def check_dict_case(d):
    if not d:
        return False
    if not all(isinstance(k, str) for k in d):
        return False
    return all(k.islower() for k in d) or all(k.isupper() for k in d)

