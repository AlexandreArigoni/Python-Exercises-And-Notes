"""Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit."""
temp = float(input('Enter the temperature in celsius degrees: '))
fh = temp*1.8 + 32
print('The temperature in fahrenheit is: {}'.format(fh))
