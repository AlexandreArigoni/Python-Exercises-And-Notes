from random import randint
import emoji
from termcolor import colored
from time import sleep
"""
1 == scissor  :v:
2 == rock     :fist:
3 == paper    :hand:
"""
print('~*~'*20)
print('Welcome to the jokenpô game')
print('~*~'*20)
print('[1] for Scissor\n'
      '[2] for Rock\n'
      '[3] for Paper\n')
n = int(input('Select what you want to pick '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

j = randint(1, 3)
if j == 1 and n == 1:
    print(emoji.emojize(':scissors:'), ' X ', emoji.emojize(':scissors:'))
    print(colored('Draw!', 'yellow'))
elif j == 1 and n == 2:
    print(emoji.emojize(':scissors:'), ' X ', emoji.emojize(':crystal_ball:'))
    print(colored('You won!', 'green'))
elif j == 1 and n == 3:
    print(emoji.emojize(':scissors:'), ' X ', emoji.emojize(':raised_hand:'))
    print(colored('You lost!', 'red'))
elif j == 2 and n == 1:
    print(emoji.emojize(':crystal_ball:'), ' X ', emoji.emojize(':scissors:'))
    print(colored('You lost!', 'red'))
elif j == 2 and n == 2:
    print(emoji.emojize(':crystal_ball:'), ' X ', emoji.emojize(':fist:'))
    print(colored('Draw!', 'yellow'))
elif j == 2 and n == 3:
    print(emoji.emojize(':crystal_ball:'), ' X ', emoji.emojize(':raised_hand:'))
    print(colored('You won!', 'green'))
elif j == 3 and n == 1:
    print(emoji.emojize(':raised_hand:'), ' X ', emoji.emojize(':scissors:'))
    print(colored('You won!', 'green'))
elif j == 3 and n == 2:
    print(emoji.emojize(':raised_hand:'), ' X ', emoji.emojize(':crystal_ball:'))
    print(colored('You lost!', 'red'))
elif j == 3 and n == 3:
    print(emoji.emojize(':raised_hand:'), ' X ', emoji.emojize(':raised_hand:'))
    print(colored('Draw!', 'yellow'))
else:
    print(colored('Enter an correct number ', 'blue'))

# Use if inside if (after the first if inside u can use elif normally)
