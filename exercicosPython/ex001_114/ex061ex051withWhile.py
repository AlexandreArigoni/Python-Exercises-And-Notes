n = int(input('Enter the first term of the arithmetical progression: '))
m = int(input('Enter the ratio of the arithmetical progression: '))
c = 1
print("{}, ".format(n), end='')
while c < 10:
    n += m
    c += 1
    print("{}.".format(n) if c == 10 else "{}, ".format(n), end='')







