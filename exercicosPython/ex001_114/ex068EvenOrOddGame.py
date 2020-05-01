from random import randint
count = 0
while True:
    r = randint(1, 10)
    print(r)
    n = int(input('Enter a number: '))
    eo = input('Even or Odd? [E/O]').upper()
    if eo == 'E':
        if (n + r) % 2 == 0:
            print('You won!')
            count += 1
        else:
            print('You lost...')
            break
    if eo == 'O':
        if (n + r) % 2 != 0:
            print('You won!')
            count += 1
        else:
            print('You lost...')
            break
print(count)
