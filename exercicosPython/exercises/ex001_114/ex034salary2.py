s = float(input('Enter your salary: '))
if s > 1250:
    print('Your new salary is R${:.2f}'.format(1.1*s))
else:
    print('Your new salary is: R${:.2f}'.format(1.15*s))

