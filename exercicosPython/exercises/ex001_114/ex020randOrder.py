"""O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
 leia o nome dos quatro alunos e mostre a ordem sorteada."""
from random import shuffle
n1 = str(input('Student 1: '))
n2 = str(input('Student 2: '))
n3 = str(input('Student 3: '))
n4 = str(input('Student 4: '))
lista = [n1, n2, n3, n4]
chosen = shuffle(lista)
print(lista)


