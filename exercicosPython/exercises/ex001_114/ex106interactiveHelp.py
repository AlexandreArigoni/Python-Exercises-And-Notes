c = ('\033[m', '\033[1;30;41m', '\033[1;30;45m', '\033[1;30;47m')


def pyhelp():
    from time import sleep
    while True:
        n = input('Function or Library: ')
        sleep(1)
        if n == 'end':
            break
        print(c[3], end='')
        print('~' * len(f' Accessing the command {n} '))
        print(f' Accessing the command {n}')
        print('~' * len(f' Accessing the command {n} '))
        sleep(1)
        print(c[0], end='')
        print(c[1], end='')
        help(n)
        print(c[0], end='')


pyhelp()
