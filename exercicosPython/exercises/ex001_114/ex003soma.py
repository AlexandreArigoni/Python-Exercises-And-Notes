"""Crie um programa que leia dois números e mostre a soma entre eles."""
n1 = float(input('First Number: '))
n2 = float(input('Second Number: '))
s = n1 + n2
print('the sum between {} and {} is {}'.format(n1, n2, s))
# Test
print(type(s))
