"""Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""
num = int(input('Enter a number '))
print('Double: {:>5}'.format(num*2))
print('Triple: {:>5}'.format(num*3))
print('Pow: {:>5.2f}'.format(pow(num, 1/2)))



