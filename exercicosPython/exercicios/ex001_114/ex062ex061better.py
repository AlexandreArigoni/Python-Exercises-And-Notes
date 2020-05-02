n = int(input('Enter the first term of the arithmetical progression: '))
m = int(input('Enter the ratio of the arithmetical progression: '))
c = 1
print("{}, ".format(n), end='')
while c < 10:
    n += m
    c += 1
    print("{}.\n".format(n) if c == 10 else "{}, ".format(n), end='')
c = int(input('Continue?\n[1]YES\n[2]NO\n'))
while c != 2:
    if c == 1:
        q = int(input('Enter how much times: '))
        x = 0
        while x < q:
            n += m
            x += 1
            print("{}.\n".format(n) if x == q else "{}, ".format(n), end='')
        c = int(input('Continue?\n[1]YES\n[2]NO\n'))
    else:
        c = int(input('Enter a valuable number \n'))
print('Bye!')


