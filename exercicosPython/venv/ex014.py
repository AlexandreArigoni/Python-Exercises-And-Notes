d = float(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos km você rodou? '))
t = (d*60)+(km*0.15)
print('Você terá que pagar {} reais'.format(t))