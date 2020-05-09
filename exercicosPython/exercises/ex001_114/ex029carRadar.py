"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
 foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""
from random import randint
v = randint(60, 100)
print('The velocity of your car is {}'.format(v))
if v > 80:
    print('You received a mulct of {} '.format((v-80)*7))
else:
    print('You dont have received a mulct')
