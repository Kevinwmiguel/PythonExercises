"""
Ex 55 - Develop a program that reads the name, age and sex of 4 people. At the end of the program, show:
 - the average age of the group.
 - what is the name of the oldest man
 - How many women are under 20 years old.
"""
print('\n')
# ----- Var -----
people = 1
mean = 0
young_woman = 0
h_age = 0
man = ''

# ----- Loop -----
while people <=2:                       # Loop to create a person and get the name, age and sex.
    print(f'{people}º Person')
    name = input('Name:')
    age = int(input('Age:'))
    sex = input('Sex: [M/F]: ').strip().upper()
    # ----- condition zone -----
    if people == 1:
        h_age = age
    mean = mean + age

    if sex == 'M':
        if age >= h_age:
            man = name
            h_age = age
    if sex == 'F':
        if age < 20:
            young_woman += 1
    people += 1

mean = mean / people
print(f'the average age of the group is {mean:.2f} years')
print(f'the oldest man is {h_age} years old and is called {man} ')
print(f'in all there are {young_woman} women under 20')

input('Enter to exit')
