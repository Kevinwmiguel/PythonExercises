"""
Ex 46 - creates a program that shows on the screen all the even numbers that are in the range of 1 and 50
"""
# -------- Import zone --------
from time import sleep

# -------- Header zone --------

print('Even number between 1 and 50')

# --------- Function to count ---------
for c in range(2, 51, 2):
    sleep(0.5)
    print(f'{c}..', end='')

input('Enter to exit')
