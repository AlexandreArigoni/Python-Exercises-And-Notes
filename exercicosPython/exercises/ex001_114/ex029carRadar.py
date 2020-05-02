from random import randint
from termcolor import colored
v = randint(60, 100)
print(colored('The velocity of your car is {}'.format(v), 'blue'))
if v > 80:
    print(colored('You received a mulct of {} '.format((v-80)*7), 'red'))
else:
    print(colored('You dont have received a mulct', 'green'))

