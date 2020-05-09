"""Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome."""
name = input('Enter your full name: ')
name2 = name.upper().split()
print('SILVA' in name2)



