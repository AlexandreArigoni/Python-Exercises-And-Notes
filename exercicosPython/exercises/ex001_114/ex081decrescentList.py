lista = list()
cont = 0
contf = 0
while True:
    n = int(input('Enter a number[0 to exit]: '))
    if n == 0:
        break
    else:
        lista.append(n)
        cont += 1
        if n == 5:
            contf += 1

print(sorted(lista, reverse=True))
print(cont)
if contf >= 1:
    print('The number 5 is on the list')


