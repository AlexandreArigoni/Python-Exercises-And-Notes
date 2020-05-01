w20 = 0
om = 0
summ = 0
no = 0
no1 = 0
no2 = 0
no3 = 0
om1 = 0
om2 = 0
om3 = 0
for c in range(1, 5):
    a = int(input('Enter your age: '))
    n = str(input('Enter your name: '))
    s = int(input('Enter 1 for man and 2 for woman: '))
    summ += a
    if a < 20 and s == 2:
        w20 += 1
    elif c == 1 and s == 1:
        om = a
        no = n
    elif c != 1 and s == 1 and a > om:
        om = a
        no = n
    elif c != 1 and s == 1 and a == om:
        no1 = n
        om1 = a
        om = 0
    elif c != 1 and s == 1 and a == om1 != om:
        no2 = n
        om2 = a
        om1 = 0
    elif c != 1 and s == 1 and a == om2 != om1:
        no3 = n
        om3 = a
if om1 != 0:
    print('The two older men are: {}, {}'.format(no, no1))
elif om2 != 0:
    print('The three older men are: {}, {}, {}'.format(no, no1, no2))
elif om3 != 0:
    print('All the men have the same age')
else:
    print('Older man: {}'.format(no))
    print('Mean of the ages: {}'.format(summ/4))
    print('Women with less than 20 years: {}'.format(w20))
print('Mean of the ages: {}'.format(summ/4))
print('Women with less than 20 years: {}'.format(w20))

