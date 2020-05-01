from random import randint
from time import sleep
from operator import itemgetter
gamers = dict()
gamers['jogador1'] = randint(1, 6)
gamers['jogador2'] = randint(1, 6)
gamers['jogador3'] = randint(1, 6)
gamers['jogador4'] = randint(1, 6)
for k, v in sorted(gamers.items(), key=itemgetter(1), reverse=True):
    print(f'The {k} took {v}')
    sleep(0.4)

print(gamers)
