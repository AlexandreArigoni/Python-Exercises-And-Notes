from datetime import date
z = 0
for c in range(1, 8):
    y = int(input('Enter the year the person were born: '))
    x = date.today().year - y
    if x >= 21:
        z += 1
print('{} peoples are adults'.format(z))
