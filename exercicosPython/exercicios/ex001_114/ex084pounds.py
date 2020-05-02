pessoas = list()
tudo = []
mai = men = 0
while True:
    pessoas.append(str(input('Name: ')))
    pessoas.append(int(input('Weight: ')))
    c = str(input('Want to continue? ')).upper()
    if len(tudo) == 0:
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    tudo.append(pessoas[:])
    pessoas.clear()
    if c == 'N':
        break
for p in tudo:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
for p in tudo:
    if p[1] == men:
        print(f'[{p[0]}]', end='')

# print(tudo)
# print(men)
