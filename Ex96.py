"""
Ex 96 - Make a program that has a function called token(),
that receives two optional parameters: the name of a player
and how many goals he scored. the program should be able
to show the player's record, even if some data has not
been entered correctly

"""


def token(names='<unknown>', x_goals=0):
    print(f' The player {names} did {x_goals} score in the match')


name = str(input("Player's name: "))
goals = input('How many goals did the player score in the match?: ')
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
if name.strip() == '':
    token(x_goals=goals)
else:
    token(name, goals)

input('Enter to exit')
