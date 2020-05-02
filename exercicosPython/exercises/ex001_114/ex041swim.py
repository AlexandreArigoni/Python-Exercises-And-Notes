from datetime import date
y = int(input('Enter the year you were born: '))
th = date.today().year
x = th - y
if x <= 9:
    print('Little')
elif 9 < x <= 14:
    print('Infant')
elif 14 < x <= 19:
    print('Junior')
elif x == 20:
    print('Senior')
else:
    print('Master')
