"""
Ex 27 - make a program that reads from the keyboard the first and last name of a person
"""

name = str(input('Type your full name:')).upper().strip()
pri = name.find(' ')
ult = name.rfind(' ')
print(f'Your first name is: {name[:pri]}')
print(f'Your last name is: {name[ult:]}')

input('Enter to exit')
