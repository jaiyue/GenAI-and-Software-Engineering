def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    sorted_lst = sorted(lst)
    res = []
    i, j = 0, len(sorted_lst) - 1
    take_min = True
    while i <= j:
        if take_min:
            res.append(sorted_lst[i])
            i += 1
        else:
            res.append(sorted_lst[j])
            j -= 1
        take_min = not take_min
    return res

