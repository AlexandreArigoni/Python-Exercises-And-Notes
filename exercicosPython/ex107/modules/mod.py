def half(num, op=False):
    r = num / 2
    if op:
        return better(r)
    else:
        return r


def double(num, op=False):
    r = num * 2
    if op:
        return better(r)
    else:
        return r


def plus(num, pl, op=False):
    r = num + (num*pl) / 100
    if op:
        return better(r)
    else:
        return r


def minus(num, mi, op=False):
    r = num - (num*mi) / 100
    if op:
        return better(r)
    else:
        return r


def better(num):
    return f'{int(num):.2f}'.replace('.', ',')


def resume(num, pl=0, mi=0):
    print('-='*25)
    print('                    Resume')
    print('-=' * 25)
    print(f'Price analysed: \t\t\t{num}')
    print(f'Half of the price: \t\t\t{better(half(num))}')
    print(f'Double of the price: \t\t{better(double(num))}')
    print(f'{pl}% added on the price: \t{better(plus(num, pl))}')
    print(f'{mi}% reduced in the price: \t{better(minus(num, mi))}')
    print('-=' * 25)
