cont2 = cont3 = num = num2 = num3 = 0
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
for p, c in enumerate(li):
    if c % 2 == 0:
        num += c
    if p == 2 or p == 5 or p == 8:
        num2 += c
    if p == 3 or p == 4 or p == 5:
        if c > num3:
            num3 = c
print(f'Sum of the even numbers: {num}')
print(f'Sum of the numbers in the third column: {num2}')
print(f'The biggest number in the second line is: {num3}')
