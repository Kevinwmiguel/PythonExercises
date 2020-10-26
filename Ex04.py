"""
Ex 04 - Make a program that reads something on the keyboard and shows on the screen its primitive type and some information about it
"""
# ---------- Header Zone ----------
print('Dissecting variables')
print('-' * 30)

# ---------- Input zone ----------
Name = input('Type your full name: ')

# ---------- Output zone ----------
print(f'The primitive type of this value is: {type(Name)}')
print(f'does this have spaces? {Name.isspace()}')
print(f'is it number? {Name.isnumeric()}')
print(f'is it alphabetic? {Name.isalpha()}')
print(f'Is it alphanumeric? {Name.isalnum()}')
print(f'Is it upper? {Name.upper()}')
print(f'letter in lower: {Name.lower()}')
print(f'Capitalize: {Name.capitalize()}')

input()
