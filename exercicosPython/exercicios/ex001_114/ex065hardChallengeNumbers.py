h = s = co = c = 0
lo = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
'''when co = 1 -> equalize the variables'''
while c != 33:
    c = int(input())
    co += 1
    if c > h and c != 33:
        h = c
    if c < lo:
        lo = c
    s += c
if co != 1:
    print((s - 33)/(co-1))
    print(co-1)
    print(lo)
else:
    print('Bye')


