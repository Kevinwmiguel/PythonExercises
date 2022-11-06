"""
Ex 19 - a teacher wants to raffle one of his four students to erase the board,
make a program that helps him, reading their name and writing the name of the chosen one
"""

from random import choice
print('Help a teacher to choice a student')
print('-' * 30)

name_1 = input('Type the first student: ')
name_2 = input('Type the second student: ')
name_3 = input('Type the third student: ')
name_4 = input('Type the forth student: ')

list_1 = [name_1, name_2, name_3, name_4]
chosen_one = choice(list_1)
print('-' * 30)

print(f'The the student chosen was {chosen_one}')

input('Enter to exit')
