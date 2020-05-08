from random import randint
count = 0
print('EVEN OR ODD GAME!')
print('How many times can you win until your lost?')
while True:
    r = randint(1, 10)
    n = int(input('Enter your number: '))
    eo = input('The result will be EVEN or ODD? [E/O] ').upper()
    if eo == 'E':
        if (n + r) % 2 == 0:
            print('You won!')
            count += 1
            print("Let's play another match")
        else:
            print('You lost...')
            print(f'GAME OVER! You won {count} time(s)!')
            break
    if eo == 'O':
        if (n + r) % 2 != 0:
            print('You won!')
            count += 1
            print("Let's play another match")
        else:
            print('You lost...')
            print(f'GAME OVER! You won {count} time(s)!')
            break

