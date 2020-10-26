"""
Ex 44 - Make a program that makes the computer play Jokenpô with the user

"""
# -------------------- import --------------------

from random import choice
from time import sleep

# -------------------- Def Zone--------------------


def line():
    print('\033[36m-=\033[m' * 15)


# -------------------- Var Zone --------------------

Jokenpo = ['Scissors', 'Stone', 'Paper']
pc = choice(Jokenpo)
esc = 0

# -------------------- Header Zone --------------------

sleep(1)
line()
print('JOKENPO TIME'.center(30))
line()

# -------------------- Input zone --------------------

sleep(1)
while esc < 1 or esc > 3:
    esc = int(input('\t[1] Scissors\n'
                    '\t[2] Stone\n'
                    '\t[3] Paper\n'
                    'Option: '))
    if esc < 1 or esc > 3:
        print('\033[31mERROR! Please enter a valid option!\033[m')
        line()
line()

# -------------------- Conditional and Result Zone --------------------

print('Processing..')
sleep(1)
print(f'PC option: {pc}')

if esc == 1 and pc == 'Stone' or esc == 2 and pc == 'Paper' or esc == 3 and pc == 'Scissors':
    print('\033[4;31mYou lose this one man xD\033[m')
elif esc == 1 and pc == 'Paper' or esc == 2 and pc == 'Scissors' or esc == 3 and pc == 'Stone':
    print('\033[4;32mGood one, you beat me x( \033[m')
else:
    print('\033[4;34this match finished with a draw. go again! ?\033[m')

input()
