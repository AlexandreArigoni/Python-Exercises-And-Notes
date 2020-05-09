"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
 quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""
km = float(input('How many kilometres you run? '))
km = km*0.15
days = int(input('How many days did you stay with the car? '))
days = days*60
pay = days + km
print('You need to pay R${:>8.2f}'.format(pay))





