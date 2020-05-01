x = 0
for c in range(0, 6):
    n = int(input('Enter a number '))
    if n % 2 != 0:
        x += n
    else:
        print(end='')
print(f'Sum of odds: {x}')

