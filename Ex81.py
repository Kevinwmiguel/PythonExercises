"""
Ex 81 - Make a program that helps a MEGA SENA player to
create guesses. the program will ask how many games will be
generated and will draw 6 numbers between 1 and 60 for each
 game, registering everything in a composed list
"""

# ----- Import -----
from random import sample

# ----- Var -----
draw = list()
game = list()


# ----- Function -----
def header():
    print('=' * 30)
    print(f'{"PLAY IN MEGA SENA"}'.center(30))
    print('=' * 30)
    print('-=' * 3, 'Sorting numbers', '-=' * 3)


header()
# the function sample that choice a random numbers to put in a list to the game
draw = int(input('How many game do you want to play?: '))
for c in range(1, draw+1):
    draw = sample(range(1, 60), 6)
    game.append(draw[:])        # Copy a list into another list
    draw.clear()    # Clear first the list
for c,v in enumerate(game):
    print(f'Game {c+1}: {v} ')

input('Enter to exit')
