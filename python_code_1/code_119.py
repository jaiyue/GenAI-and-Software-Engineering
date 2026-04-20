Here's a concise implementation — it checks both concatenation orders using each string's net balance and minimum prefix balance:

def match_parens(lst):
    def stats(s):
        bal = 0
        min_pref = 0
        for ch in s:
            bal += 1 if ch == '(' else -1
            min_pref = min(min_pref, bal)
        return bal, min_pref

    a, b = lst
    netA, minA = stats(a)
    netB, minB = stats(b)

    def valid_first(net1, min1, net2, min2):
        # while scanning first string from 0, never go negative
        # while scanning second string its prefixes are shifted by net1 and must not go negative
        return min1 >= 0 and (min2 + net1) >= 0 and (net1 + net2) == 0

    return 'Yes' if valid_first(netA, minA, netB, minB) or valid_first(netB, minB, netA, minA) else 'No'

Example: match_parens(['()(', ')']) -> 'Yes'.

