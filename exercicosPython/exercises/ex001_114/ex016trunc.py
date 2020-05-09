"""Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira."""
from math import trunc
num = float(input('Enter a number '))
print('Number without nothing after the point: {}'.format(trunc(num)))

