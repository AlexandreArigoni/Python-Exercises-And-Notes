count = 0
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
t = (n1, n2, n3, n4)
for c in t:
    if c == 9:
        count += 1
    if c % 2 == 0:
        print(f'Pair: {c}')
for pos, c in enumerate(t):
    if c == 3:
        print(f'3 in position: {pos+1}')
print(f'\nHave {count} nine(s) in the tuple ')

