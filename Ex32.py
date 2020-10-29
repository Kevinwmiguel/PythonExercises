"""
Ex 32 - Make a program that reads any year and shows if it is leap
"""
# importing the datatime module
from datetime import date
year = int(input('Enter the year (Type 0 to current year):  '))

# descovering is the year is leap or not, if the year equal 0 will be the current year
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'the year: {year} is leap year')
else:
    print(f'the year: {year} is not leap year')

input('Enter to exit')
