print('Dissecting variables')
print('-' * 30)

Name = input('Type your full name: ')

print(f'The primitive type of this value is: {type(Name)}')
print(f'does this have spaces? {Name.isspace()}')
print(f'is it number? {Name.isnumeric()}')
print(f'is it alphabetic? {Name.isalpha()}')
print(f'Is it alphanumeric? {Name.isalnum()}')
print(f'Is it upper? {Name.upper()}')
print(f'letter in lower: {Name.lower()}')
print(f'Capitalize: {Name.capitalize()}')

input()
