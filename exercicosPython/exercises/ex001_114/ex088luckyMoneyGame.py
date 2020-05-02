from random import randint
from time import sleep
r = list()
x = 0
games = list()
n = int(input('Enter how many games: '))
for c in range(0, n):
    for s in range(0, 6):
        r.append(randint(1, 60))
    r.sort()
    games.append(r[:])
    r.clear()
for c in range(0, n):
    sleep(0.7)
    print('Game {}: {}'.format(c + 1, games[c]))


