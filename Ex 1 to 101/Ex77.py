"""
Ex 77 - Create a program where the user types any
expression that uses parentheses. your application
should analyze whether the passed expression has open
 and closed parentheses in the correct order

"""
ex = input('Type some mathematical expression : ')
if ex.count('(') == ex.count(')'):
    print('The expression is valid')
else:
    print('The expression is invalid')

input('Enter to exit')
