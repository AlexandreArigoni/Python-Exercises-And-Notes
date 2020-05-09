"""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""
num = int(input('Meters: '))
print('{:^5} meters is equal {:^} centimeters'.format(num, num*100))
print('{:^5} meters is equal {:^5} millimeters'.format(num, num*1000))
