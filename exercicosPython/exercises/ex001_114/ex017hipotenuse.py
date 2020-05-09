"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa."""
from math import hypot
co = float(input('Enter the cat op of the triangle '))
ca = float(input('Enter the cat a of the triangle '))

print('The hypotenuse is of the triangle is: {:.2f}'.format(hypot(ca, co)))




