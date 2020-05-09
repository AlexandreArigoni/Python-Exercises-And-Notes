"""Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor."""
num = int(input('Enter a number '))
ant = num - 1
suc = num + 1
print('Ant: {:>5}'.format(ant))
print('Suc: {:>5}'.format(suc))


