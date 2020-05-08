t = float(input('Enter the first term of the arithmetic progression '))
r = float(input('Enter the ratio of the arithmetic progression '))
x = r
print(t, ', ', end='')
for c in range(1, 10):
    t += x
    print(t, end=', ' if c < 9 else '.')
