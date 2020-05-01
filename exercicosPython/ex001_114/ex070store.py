s = cp = lo = count = 0
ch = ''
while True:
    n = input('Product: ')
    p = float(input('Price: '))
    c = input('Continue? [Y/N] ').upper()
    while c not in 'YN':
        c = input('Continue? [Y/N] ').upper()
    if p > 1000:
        cp += 1
    if count == 1:
        lo = p
        ch = n
    if lo > p:
        lo = p
        ch = n
    s += p
    count += 1
    if c == 'N':
        break
print(f'The sum of the prices is {s}')
print(f'{cp} products with price above 1000')
print(f'The cheapest product is {ch} which costs {lo}')

