def notes(*num, sit=False):
    """
    :param num: Notes of the student
    :param sit: If you wanna see his situation
    :return: return the dict
    """
    dic = dict()
    co = hi = lo = tot = 0
    for c in num:
        if co == 0:
            hi = lo = tot = c
        else:
            tot += c
            if c > hi:
                hi = c
                dic['bigger'] = hi
            if lo > c:
                lo = c
                dic['lower'] = lo
        co += 1
    dic['total'] = co
    dic['mean'] = tot / co
    if sit:
        if dic['mean'] > 6:
            dic['sit'] = 'Approved'
        else:
            dic['sit'] = 'Rejected'
    return dic


n = notes(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(n)
help(notes)
