player = dict()
every = list()
g = ga = 0
while True:
    player['name'] = str(input('Enter the player name: '))
    player['games'] = int(input('Enter how many games he played: '))
    player['s'] = ''
    goals = list()
    for c in range(0, player['games']):
        goals.append(int(input(f'How many goals in the game {c}? ')))
        g += goals[len(goals) - 1]
    player["goals"] = goals[:]
    player["ga"] = ga
    player['g'] = g
    g = 0
    every.append(player.copy())
    ga += 1
    cont = str(input('Want to continue [S/N]? ')).upper()
    if cont in 'N':
        break
print('code  name         goals       total')
print('-='*30)
for c in every:
    print(f'{c["ga"]} {c["name"]:<12}{c["goals"]}{c["s"]:<5}{c["g"]:<5}')
while True:
    cont = int(input('Enter the code number of the player you want to access [999 to exit]: '))
    if cont == 999:
        break
    for c in every:
        if c["ga"] == cont:
            for p, x in enumerate(c['goals']):
                print(f'In the game {p} he did {x} goals.')
print('Good Bye!!!')


