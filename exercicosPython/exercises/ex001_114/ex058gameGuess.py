from random import randint
from time import sleep
from termcolor import colored
print(colored('Thinking in a number between 1 and 10 ...', 'red'))
z = 0
sleep(3)
i = randint(1, 10)
print(i)
x = int(input('What number im thinking? '))
z += 1
while x != i:
    z += 1
    print('Try again')
    x = int(input('What number im thinking? '))
print("Processing ...")
sleep(3)
print(colored('~~'*20, 'blue'))
print(colored('Congratulations, you won after trying {}'.format(z), 'red'))
print(colored('~~'*20, 'blue'))
