"""
Ex 62 - make a program that plays even or odd with the computer.
the game will only be stopped when the player loses. showing the total number of consecutive surveys he won at the end of the game
"""

# ----- Import Zone -----
from random import randint

# -----Function Zone -----
def header():
    print('=-'*15)
    print('Game Even or Odd!'.center(30))
    print('=-'*15)

# ----- Header -----
header()

# ----- Var -----
td = 0
pco = ''

# ----- Loop Zone -----
while True:
    v = int(input('how many fingers? : '))
    c = str(input('Even or odd? [E/O]: ')).upper().strip()
    if c == 'E':                                # Make sure that the computer will choise the another option
        pco = 'O'
    elif c == 'O':
        pco = 'E'
    pc = randint(0, 10)

    s = v + pc
    
    print(f'{s}: is even'if s % 2 == 0 else f'{s}: is odd')         # Check if the number is even or odd
    if s % 2 == 0 and c == 'E' or s % 2 == 1 and c == 'O':          # Check if you chose the right option
        print('\033[32mYou won!\033[m')
        print(f'you played {v} the computer {pc}. Total {s}')
        print('=-' * 15)
        break
    else:
        print(f'you played {v} and the computer {pc}. Total {s}')
        print('\033[31mYou lost go again\033[m')
        print('=-' * 15)

    td += 1
# show the results
print(f'You lost {td} times, before won')

input()
