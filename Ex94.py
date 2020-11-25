"""
Ex 94 - create a program that has a function called vote() that will
receive as a parameter the year of birth of a person, returning a literal
 value indicating whether a person has a denied, optional or mandatory vote in the elections
"""

from datetime import date


def vote(years):
    age = date.today().year
    age = age - years
    if age < 18:
        right = "you don't vote!"
    elif age >= 65:
        right = "optional vote"
    else:
        right = 'MANDATORY VOTE'
    print(f'with {age} years: ', end='')
    return right


print('=' * 25)
year = int(input('what is the year of your birth: '))
votes = vote(year)
print(votes)

input('Enter to exit')
