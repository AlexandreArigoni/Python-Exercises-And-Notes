"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados."""
num = int(input('Enter a number between 0 and 9999 '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('U: {}'.format(u))
print('D: {}'.format(d))
print('C: {}'.format(c))
print('m: {}'.format(m))



