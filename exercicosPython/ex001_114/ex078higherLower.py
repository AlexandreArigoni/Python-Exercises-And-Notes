hi = lo = 0
value = list()
for c in range(0, 5):
    value.append(int(input('Enter a number: ')))
    if c == 0:
        hi = lo = value[c]
    else:
        if value[c] > hi:
            hi = value[c]
        if value[c] < lo:
            lo = value[c]
print("Highest in position(s): ", end='')
for z, x in enumerate(value):
    if x == hi:
        print(f'{z}... ', end='')
print('\n')
print("Lowest in position(s): ", end='')
for z, x in enumerate(value):
    if x == lo:
        print(f'{z}... ', end='')


