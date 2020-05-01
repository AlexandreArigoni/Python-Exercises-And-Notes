player = dict()
g = ga = 0
player['name'] = str(input('Enter the player name: '))
player['games'] = int(input('Enter how many games he played: '))
goals = list()
for c in range(0, player['games']):
    goals.append(int(input(f'How many goals in the game {c}? ')))
    g += goals[len(goals) - 1]
player['g'] = g
player['goals'] = goals.copy()
print(f'The player {player["name"]} did {player["g"]} goals in his career')
for p, c in enumerate(player['goals']):
    print(f'In the game {p} he did {c} goals.')

