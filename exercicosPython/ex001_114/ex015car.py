km = float(input('How many kilometres you run? '))
km = km*0.15
days = int(input('How many days did you stay with the car? '))
days = days*60
pay = days + km
print('You need to pay R${:>8.2f}'.format(pay))





