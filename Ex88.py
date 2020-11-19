"""
Ex 88 - Enhance challenge 86 so that it works with multiple players,
including a system for viewing details of each player’s performance
"""


def line():
    print('-='*20)


player = {}
goals = []
tg = 0
players = list()

while True:
    player.clear()
    goals.clear()
    player['name'] = str(input("Player's name: "))
    if player['name'].isnumeric:
        print('please enter a valid name')
        continue
    p = int(input(f'How many matches did {player["name"]} played? '))
    for c in range(0, p):
        gol = int(input(f'how many goals did in the match {c}?: '))
        goals.append(gol)
    player['goals'] = goals[:]
    player['total'] = sum(goals)
    players.append(player.copy())
    while True:
        r = str(input('Want to continue [Y/N]? :')).upper()[0]
        if r in 'YN':
            break
        print('ERROR! Type just Y or N')
    if r == 'N':
        break
line()
print("cod", end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
line()
for p, d in enumerate(players):
    print(f'{p:>4}', end='  ')
    for v in d.values():
        print(f'{str(v):<15}', end='')
    print()
while True:
    data = int(input("Shows which player' data ? (999 to stop) "))
    if data == 999:
        break
    if data >= len(players):
        print("Error! this player doesn't exist")
    else:
        print(f' -- Player survey {players[data]["name"]}: ')
        for e, q in enumerate(players[data]['goals']):
            print(f'In match {e} did {q} goals')
    line()

input('Enter to exit')
