"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""
from math import sin, cos, tan, radians
ang = int(input('Enter the angle: '))

print('The sine, cosine and tangent of {}º are respectively: \n'.format(ang))
ang = radians(ang)
# can put the function radians inside sen, cos, tan
print('{:.2f}\n{:.2f}\n{:.2f}\n'.format(sin(ang), cos(ang), tan(ang)))

