lista = []
pares = []
impares = []
while True:
    n = int(input('Enter a number[0 to exit]: '))
    if n == 0:
        break
    else:
        lista.append(n)
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'Odd: {impares}')
print(f'Even: {pares}')
print(f'All: {lista}')
