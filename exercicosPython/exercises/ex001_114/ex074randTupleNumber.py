from random import randint
lo = count = hi = 0
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for c in n:
    if count == 0:
        hi = c
    elif c > hi:
        hi = c
    if count == 0:
        lo = c
    elif c < lo:
        lo = c
    count += 1
print(f'Tuple: {n}')
print(f'Lower number in the tuple: {lo}')
print(f'Higher number in the tuple: {hi}')




