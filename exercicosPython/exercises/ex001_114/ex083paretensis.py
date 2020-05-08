n = list()
n.append(input('Enter an expression: '))
le = n[0].count('(')
ri = n[0].count(')')
if le == ri:
    print('The expression is correct!')
else:
    print('The expression is wrong!')
