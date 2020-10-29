"""
Ex 53 - Create a program that reads the birth year of seven people. at the end, show how many people have not yet reached the age of majority and how many are already older

"""

from datetime import date  # import datetime module to calculate the year of birth
year = date.today().year  # take the current year
old = young = 0

for c in range(0, 7):
    birth = int(input('Enter the year of birth: '))
    if year - birth >= 18:
        old += 1
    else:
        young += 1

print(f'The number of oldest people is: {old}')
print(f'the number of the youngest people is: {young}')

input('Enter to exit')
