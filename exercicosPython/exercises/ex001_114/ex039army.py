import datetime
from termcolor import colored
yb = int(input(colored('Enter the year you were born ', 'blue')))
ty = datetime.date.today().year
if ty - yb == 18:
    print('\033[1;36mYou are in the year to enlist')
elif ty - yb > 18:
    if (ty - yb) - 18 == 1:
        print('Have already passed one year of your year to enlist')
    if (ty - yb) - 18 > 1:
        print('Have already passed {} years of your year to enlist'.format((ty - yb) - 18))
else:
    if 18 - (ty - yb) == 1:
        print('One year left for you to enlist')
    else:
        print('{} years left for you to enlist'.format(18 - (ty - yb)))





