"""
Ex 20 - the same teacher from the previous challenge wants to raffle off the order of students' school assignments. Make a program that reads the names of the four students and shows the order of the names drawn
"""

from random import shuffle

Est_1 = str(input('Type the first student: '))
Est_2 = str(input('Type the first student: '))
Est_3 = str(input('Type the first student: '))
Est_4 = str(input('Type the first student: '))

order = [Est_1, Est_2, Est_3, Est_4]

print('-' * 30)

shuffle(order)

print(order)

input('Enter to exit')
