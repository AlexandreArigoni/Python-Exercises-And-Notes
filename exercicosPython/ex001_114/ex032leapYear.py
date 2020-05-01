from termcolor import colored
from datetime import date
y = int(input('Enter the year or put 0 for the actual year: '))
if y == 0:
    y = date.today().year
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print(colored('{} is a leap year '.format(y), 'blue'))
else:
    print(colored('{} is not a leap year '.format(y), 'red'))

# print(date.today().day)


