n = int(input('Enter the number: '))
c = n
n = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    n *= c
    c -= 1

print(n)

