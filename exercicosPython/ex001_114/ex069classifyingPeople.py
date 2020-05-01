ca = cm = cfa = 0
while True:
    print('Sign in a person ->')
    a = int(input('Enter a age: '))
    g = input('Enter the gender [M/F]: ').upper()
    while g not in 'MF':
        g = input('Enter the gender [M/F]: ').upper()
    c = input('Want to continue? [Y/N]').upper()
    while c not in 'YN':
        c = input('Want to continue? [Y/N]').upper()
    if a > 18:
        ca += 1
    if g == 'M':
        cm += 1
    if g == 'F' and a < 20:
        cfa += 1
    if c == 'N':
        break
print(f'{ca} persons with more than 18 years')
print(f'{cm} men')
print(f'{cfa} women with less than 20 years')
