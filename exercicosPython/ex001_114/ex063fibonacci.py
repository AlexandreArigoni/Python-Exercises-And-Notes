t = int(input('How many times? '))
x = 0
n = 0
m = 1
print(n)
x += 1
print(m)
x += 1
while x < t:
    if x != t:
        x += 1
        y = n + m
        print(y)
    if x != t:
        n = y + m
        x += 1
        print(n)
    if x != t:
        m = y + n
        x += 1
        print(m)
print('Bye!')


