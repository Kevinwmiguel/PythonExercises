"""
Ex 30 - Create a program that reads an integer and shows on the screen whether it is even or odd
"""
n = int(input('\033[35mEnter a integer: \033[m'))

if n % 2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')

input()
