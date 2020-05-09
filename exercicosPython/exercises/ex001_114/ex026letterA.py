"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela
 aparece a primeira vez e em que posição ela aparece a última vez."""
phrase = str(input('Enter a phrase ')).upper().strip()
print(phrase.upper().count('A'))
print('First A: {}'.format(phrase.find('A')+1))
# find = first time
print('Last A: {}'.format(phrase.rfind('A')+1))



