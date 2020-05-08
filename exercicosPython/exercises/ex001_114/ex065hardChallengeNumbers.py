h = s = co = c = lo = 0
while True:
    c = int(input('Enter an int number: '))
    cont = str(input('Want to continue? [S/N]'))
    co += 1
    if c > h:
        h = c
    if co == 1 or c < lo:
        lo = c
    s += c
    if cont in 'Nn':
        break
print(f'\nAverage: {s/co}')
print(f'You entered {co} numbers')
print(f'The lowest number is: {lo} and the highest: {h}')



