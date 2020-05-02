cont2 = cont3 = 0
li = []
for c in range(0, 9):
    if 0 <= c <= 2:
        n = int(input(f'Digite o numero na posição [0] [{c}] '))
        li.append(n)
    if 3 <= c <= 5:
        n = int(input(f'Digite o numero na posição [1] [{cont2}] '))
        li.append(n)
        cont2 += 1
    if 6 <= c <= 8:
        n = int(input(f'Digite o numero na posição [2] [{cont3}] '))
        li.append(n)
        cont3 += 1
print(f'[ {li[0]} ] [ {li[1]} ] [ {li[2]} ]\n[ {li[3]} ] [ {li[4]} ] [ {li[5]} ]\n[ {li[6]} ] [ {li[7]} ] [ {li[8]} ]')


