"""
Ex 28 - Write a program that makes the computer "think" of an integer between 0 and 5 and ask the user to try to find out which number was chosen by the computer. the program should display whether the user lost or won!

"""

from random import randrange
from time import sleep
gg = 0
tt = 1
while gg < 1:
    print('\033[1;33mWhat number did I think of??... \nprocessing\033[m')
    sleep(1)
    n = int(input('Enter a number between 1 to 10: '))
    ran = randrange(1, 10)
    print(f'the number thought was {ran}')
    if n == ran:
        gg = 1
    else:
        print('\033[1;31mTry again! \n\033[m')
        tt += 1
print(f'The total number of attempts was {tt}')
print('\033[1;32mVERY WELL!\033[m')

input('Enter to exit')
