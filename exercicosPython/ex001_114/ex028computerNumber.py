import random
from time import sleep
from termcolor import colored
num = random.randint(1, 10)
print(colored('-=-'*20, 'green'))
print('I have just thought in a number between 1 and 10')
print(colored('-=-'*20, 'green'))
if num >= 5:
    print('The number is between 5 and 10')
    if num >= 8:
        print('The number is 8 or bigger')
else:
    print('The number is between 1 and 4')
    if num <= 3:
        print('The number is between 1 and 3')
x = int(input('Enter the number im thinking: '))
print('Processing...')
sleep(5)
if x == num:
    print(colored('-=-'*20, 'blue'))
    print('You won!')
    print(colored('-=-'*20, 'blue'))
else:
    print(colored('-=-'*20, 'red'))
    print(f'You lost... the number was {num}')
    print(colored('-=-'*20, 'red'))
