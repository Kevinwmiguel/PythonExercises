"""
Ex 45 - make a program that shows on the screen a countdown to the burst of
artifice photos, going from 10 to 0, with a 1 second pause between them.
"""
# -------------------- Import zone --------------------

from time import sleep

# -------------------- Def Zone --------------------


def line():
    print('\033[35m=-\033[m' * 15)

# -------------------- Header Zone --------------------


line()
print('\033[36mCountdown for the New Year!')
line()
# -------------------- Loop zone --------------------
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)

# -------------------- Output zone --------------------
print('\033[4;32m❋!!Happy New Year!!!❋\033[m')

input()
