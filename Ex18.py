"""
Ex 018 - Make a program that reads any angle and shows on the display the sine, cosine and tangent value of that angle
"""

print('Sine, Cosine and Tangent')
print('-' * 30)

from math import radians, cos, sin, tan

n = int(input('Enter a number: '))
n = radians(n)

print(f'The sine is: {sin(n):.2f}')
print(f'The cosine is: {cos(n):.2f}')
print(f'The tangent is: {tan(n):.2f}')