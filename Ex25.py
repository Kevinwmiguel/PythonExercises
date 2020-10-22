"""
Ex 25 - Create a program that reads a person's name and tells them if they have '' Silva '' in their name
"""""

name = str(input('Type your name: ')).strip()
print(f'do you have Silva in your name ?: {"SILVA" in name.upper()}')

input()
