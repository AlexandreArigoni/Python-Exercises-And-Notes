n = 0
x = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        n += c
        x += 1
print('The sum of the {} numbers is {}'.format(x, n))

