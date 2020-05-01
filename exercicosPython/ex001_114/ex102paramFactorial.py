def factorial(n, show=False):
    """
    :param n: The number that you want the factorial
    :param show: Shows the process
    :return:
    """
    total = n
    if show:
        for c in range(n, 0, -1):
            if c != 1:
                print(c, end=' x ')
                if c != n:
                    total *= c
            else:
                print(c, end=f' = {total}')
    else:
        for c in range(n, 0, -1):
            if c != n:
                total *= c
        print(total)


factorial(5, False)
print(factorial.__doc__)
