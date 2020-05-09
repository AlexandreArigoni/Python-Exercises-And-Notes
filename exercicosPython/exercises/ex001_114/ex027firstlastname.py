"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente."""
name = str(input('Enter your full name: '))
name1 = name.split()
x = (len(name1)) - 1
print(name1[0])
print(name1[x])
