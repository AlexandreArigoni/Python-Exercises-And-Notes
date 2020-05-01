p = int(input('Enter an number '))
x = 1
for c in range(1, p+1):
    if c != 1 != c != p and p % c == 0:
        x = 0
        break
if x == 0:
    print('Not Prime')
elif p == 1:
    print('Not Prime')
else:
    print('Prime')

