"""
Ex 87 - Create a program that reads the name, sex and age of several people,
saving each person's data in a dictionary and all dictionaries in a list. At the end, show:
A) How many people are registered
B) The average age
C) A list just with woman
D) A list with age above the average

"""
# ----- Import -----
import os
# ----- Var -----
people = dict()
dudes = list()
Sum = m = 0

# ----- Loop -----
while True:
    people.clear()      # Clear the list
    people['name'] = str(input('Name: ')).strip().capitalize()
    if people['name'].isnumeric():      # make sure of the name is not be numeric
        print('Please enter a valid name')
        print('0')
        continue
    elif not people['name']:
        print('Please enter a valid name')  # make sure of the name is not null
        print('2')
        continue
    while True:
        people['sex'] = input('Sex: [M/F] ').upper()[0]     # make sure of the sex is between M or F
        if people['sex'] in 'MF':
            break
        else:
            print('Enter a valid sex')
    while True:                 # Make sure the age is numeric and highest than 0
        try:
            people['age'] = int(input('Age: '))
            if people['age'] < 0:
                print('Enter a valid age')
                continue
        except ValueError:
            print('please enter a valid age')
            continue
        else:
            break
    Sum += people['age']
    dudes.append(people.copy())
    while True:
        r = input('Want to continue? [Y/N]').upper().strip()[0]  # Take the answer of the user
        if r in 'YN':
            break
        print('ERROR! Answer just Y ou N')
        print(end='')
    if r == 'N':
        break
os.system('cls')
m = Sum / len(dudes)
# Shows the result on the screen
print('-=' * 25)
print(f'A) total we have {len(dudes)} people registered')
print(f'B) The average age is {m:5.2f} years')
print('C) registered women were: ', end=' ')

# A list of people that is above the average
for c in dudes:
    if c['sex'] in 'Ff':
        print(f'{c["name"]}', end=' ')
print(f'\nD) List of people who are above average:: ')

for p in dudes:
    if p['age'] >= m:
        print('\n', end=' ')
        for k, v in p.items():
            print(f'{k} = {v} |', end=' ')

input('\nEnter to exit')
