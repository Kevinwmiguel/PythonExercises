"""
Ex 39 - Make a program that reads the year of birth of a young person and informs them, according to their age, if they are still going to enlist in the military, if it is time to enlist or if it is past the time of enlistment. Your program should also show how much time is left or past the deadline
"""

from datetime import date  # importing a datetime module
print('-=' * 15)
print('Army force'.center(30))
print('-=' * 15)

a = int(input('Enter your year of birth: '))
aa = date.today().year  #module that read the current year
if aa - a == 18:
    print("It's time to join the Army ")
elif aa - a < 18:
    af = aa - a
    print(f'{18 - af} Years left to join the army')
else:
    af =  aa - a
    print(f"{af - 18} It's past time to join the army: ")

input('Enter to exit')
