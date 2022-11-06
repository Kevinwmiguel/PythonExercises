"""
Ex 41 - The national swimming confederation needs a
program that reads the year of birth of an athlete and
shows his category, according to age:
- up to 9 years: child
- up to 14 years: infant
- up to 19 years: Junior
- up to 25 years: Senior
- above: master

"""

from datetime import date
birth = int(input('Enter the year of your birth: '))
current_year = date.today().year
age = current_year - birth

if age <= 9:
    print(f'Age: {age}')
    print('Classification: child')
elif age <= 14:
    print(f'Age: {age}')
    print('Classification: infant')
elif age <= 19:
    print(f'Age: {age}')
    print('Classification: Junior')
elif age <= 25:
    print(f'Age: {age}')
    print('Classification: Senior')
else:
    print(f'Age: {age}')
    print('Classification: Master')

input('Enter to exit')
