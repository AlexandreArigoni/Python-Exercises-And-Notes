n = list()
n.append(input())
le = n[0].count('(')
ri = n[0].count(')')
if le % 2 == 0 and ri % 2 == 0:
    print('Correct')
else:
    print('Wrong')
print(n)

