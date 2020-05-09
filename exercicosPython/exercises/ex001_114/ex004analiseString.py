"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
sobre ele."""
x = input('type anything ')
print(type(x))
print('is upper? {}'.format(x.isupper()))
print('is space? {}'.format(x.isspace()))
print('is numeric? {}'.format(x.isnumeric()))
print('is alpha? {}'.format(x.isalpha()))
print('is isalnum? {}'.format(x.isalnum()))
print('is capitalized(title)? {}'.format(x.istitle()))



