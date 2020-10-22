"""
Ex 016 - Create a program that reads any float from the keyboard and shows it on the display its entire portion
"""

#import a library (module) math.
from math import trunc

N = float(input('Enter a number: '))
print('-' * 30)
print(f' The value entered was {N} and its entire portion is {trunc(N)}')

input()