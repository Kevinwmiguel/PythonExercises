"""
Ex 85 - Create a program that reads your name, year of birth and work card and register them (aged)
in a dictionary if by chance the CTPS is different from zero, the dictionary will
also receive the year of hire and salary. Calculate and add, in addition
to age, how old the person will retire
"""

from datetime import date

person = dict()

person['Name'] = input('Name: ')
birth = int(input('year of birth: '))
person['Age'] = date.today().year - birth
person['CTPS'] = int(input("Work Card (0 don't have): "))

if person['CTPS'] == 0:
    print('=-' * 20)
    for k, v in person.items():
        print(f'O {k} tem o valor {v}')
else:
    print('=-' * 20)
    person['Year of hiring'] = int(input('Year of hiring: '))
    person['salary'] = int(input('Salary: '))
    person['Retirement'] = person['Year of hiring'] - birth + 35
    for k, v in person.items():
        print(f'{k} has a value {v}')

input('Enter to exit')
