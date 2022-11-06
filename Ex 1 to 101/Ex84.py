"""
Ex 84 - Create a program where four players play a dice and can have the random results.
 keep this results in a dictionary. at the end, put this dictionary in order,
  knowing that the winner took the highest number on the dice

"""
# ----- Import -----
from random import randint
from operator import itemgetter
from time import sleep
# ----- Var -----
rank = list()
players = {'Player1': randint(1, 6),
           'Player2': randint(1, 6),
           'Player3': randint(1, 6),
           'Player4': randint(1, 6)}

# ----- Loop -----
for k, v in players.items():
    sleep(0.5)
    print(f'The {k} scored {v} on the dice')  # Raffle the numbers for each player
rank = sorted(players.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)

print("Ranking".center(30))  # Shows the rank list at the screen
print('-=' * 15)
for i, v in enumerate(rank):
    print(f'{i + 1} position: {v[0]} with {v[1]}')
    sleep(1)

input('\nEnter to exit')
