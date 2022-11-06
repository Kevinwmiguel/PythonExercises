"""
Ex 86 - Create a program that manages the performance of a football player.
 the program will read the player's name and how many matches he has played. 
 Then you will read the number of goals scored in each match. In the end, all of 
 this will be kept in a dictionary, including the total goals scored during the championship

"""


def line():
    print('-='*30)


# ----- Var -----
player = {}
gl = []
tg = x = 0
time = list()

# ---- Body -----
gl.clear()  # Clean the list
player['name'] = input("Player's name: ")
matches = int(input(f'how many matches {player["name"]} played?: '))  # Ask the amount of match the player had played
for c in range(0, matches):
    g = int(input(f'How many goals in the match {c}: '))
    gl.append(g)
    tg = tg + g
player['goals'] = gl[:]  # copy the list into dictionary
player['total'] = tg
time.append(player.copy())

line()
print(player)
line()

for k, v in player.items():
    print(f'The key {k} has a value {v}')
line()
print(f" The player {player['name']} played {len(player['goals'])} matches")
for i, v in enumerate(player['goals']):
    print(f'   => In match {i} did {v} goals')

input('Enter to Exit')
