"""
Ex 23 - Make a program that reads a number from 0 to 9999 and shows each of its separate digits on the screen:
"""

n = int(input('Type a number between 0 until 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'unity:, {u}')
print(f'dozen:, {d}')
print(f'Hundred, {c}')
print(f'thousands, {m}')

input()
