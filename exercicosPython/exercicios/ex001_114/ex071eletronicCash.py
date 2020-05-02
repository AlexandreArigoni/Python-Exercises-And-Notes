n = int(input('Value: '))
c50 = c20 = c10 = c5 = c1 = 0
while n - 50 >= 0:
    n -= 50
    c50 += 1
while n - 20 >= 0:
    n -= 20
    c20 += 1
while n - 10 >= 0:
    n -= 10
    c10 += 1
while n - 5 >= 0:
    n -= 5
    c5 += 1
while n - 1 >= 0:
    n -= 1
    c1 += 1
print(f'{c50} notes of 50')
print(f'{c20} notes of 20')
print(f'{c10} notes of 10')
print(f'{c5} notes of 5')
print(f'{c1} notes of 1')

