pessoas = dict()
tudo = list()
mean = 0
while True:
    pessoas['name'] = str(input('Enter the name of the person: '))
    pessoas['sex'] = str(input('Enter the gender of the person: '))
    pessoas['age'] = int(input('Enter the age of the person: '))
    cont = str(input('Want to continue [S/N]? '))
    mean += pessoas['age']
    tudo.append(pessoas.copy())
    if cont in 'Nn':
        break
print(f'Have {len(tudo)} persons in the list')
print(f'The mean of the age of the persons is: {mean/len(tudo)}')
print('Women: ')
for c in tudo:
    if c['sex'] in 'Ff':
        print(c['name'])
print('Persons with more age than the mean: ')
for c in tudo:
    if c['age'] > mean/len(tudo):
        print(c['name'])






