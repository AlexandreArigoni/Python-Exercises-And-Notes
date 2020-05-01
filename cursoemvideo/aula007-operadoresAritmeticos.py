#nome = str(input('Qual seu nome?'))
#print('Prazer em te conhecer {:<30}!'.format(nome))
#print(type(nome))

n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro valor'))
s = n1+n2
m = n1*n2
d = n1/n2
p = n1**n2
r = n1%n2
di =n1//n2

print('A soma vale {}, \n a multiplicação vale {}, a divisão vale {}, a potenciação vale {}'.format(s,m,d,p),end = ' ')
print('o resto vale {}, a divisão inteira vale {}'.format(r,di))

