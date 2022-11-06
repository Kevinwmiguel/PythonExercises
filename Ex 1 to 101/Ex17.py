"""
Ex 017 - Make a program that reads the length of the opposite leg and the adjacent leg of a right triangle, calculate and show the length of the hypotenuse
"""
print('Discovering the Hypotenuse')

from math import hypot
co = float(input('Enter the opposite leg: '))
ca = float(input('Enter the adjacent leg: '))

print(f'The hypotenuse is {hypot(ca,co):.2f}')

input('Enter to exit')
