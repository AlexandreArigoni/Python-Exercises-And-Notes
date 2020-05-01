student = list()
classe = []
count = 0
while True:
    student.append(str(input('Name: ')))
    student.append(int(input('First grade: ')))
    student.append(int(input('Second grade: ')))
    n = str(input('Continue [S/N]? ')).upper()
    classe.append(student[:])
    student.clear()
    if n in 'N':
        break
print('       Name         Grade')
print('-'*26)
for c in classe:
    print('{:<4} {:<8} {:>10}'.format(count, c[0], (c[1] + c[2])/2))
    count += 1
print('-'*26)
while True:
    n = int(input('Show the grades of who?(999 to end) '))
    if n == 999:
        break
    print(f'The grades of {classe[n][0]} are {classe[n][1]} and {classe[n][2]}')
