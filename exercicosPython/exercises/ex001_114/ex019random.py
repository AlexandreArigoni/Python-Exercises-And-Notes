"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
nome dos alunos e escrevendo na tela o nome do escolhido."""
from random import choice
n1 = str(input('Student 1: '))
n2 = str(input('Student 2: '))
n3 = str(input('Student 3: '))
n4 = str(input('Student 4: '))
lista = [n1, n2, n3, n4]
chosen = choice(lista)
print('The Student who will clear the board is: {}'.format(chosen))











