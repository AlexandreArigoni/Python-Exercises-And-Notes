par = []
impar = []
todos = list()
mai = men = 0
for c in range(0, 7):
    n = int(input('Enter a number: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
todos.append(par[:])
todos.append(impar[:])
print(f'Even: {sorted(todos[0])}')
print(f'Odd: {sorted(todos[1])}')







