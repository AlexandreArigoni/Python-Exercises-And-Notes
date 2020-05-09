"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""
h = int(input('height: '))
w = int(input('width: '))
a = h*w
print('Area: {:>5}'.format(a))
print('Gallons of paint: {:>5}'.format(a/2))
