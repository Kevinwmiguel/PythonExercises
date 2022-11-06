"""
Ex 58 - Make a program that reads any number and shows its factorial
"""

# ----- import Zone -----
from math import factorial
# ----- Input Zone -----

n = int(input('Number: '))
f = factorial(n)
count = n

# ----- Loop Zone ----- 
while count > 1:
    print(f'{count} ',end='')
    if count == 2:
        print('1: ')
    count -= 1  

# Result
print(f'\nthe factorial of {n} is {f}')

input('Enter to exit')
