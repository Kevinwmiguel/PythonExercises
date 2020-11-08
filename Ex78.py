"""
Ex 84 - Make a program that reads the names and weights of several people running on a list at the end show.
A) How many people were registered
B) A list with the heaviest people
C) A list with the lightest people

"""

# ----- Var -----
first_list = list()
second_list = list()
heaviest = lightest = 0

# ----- Loop Zone -----
while True:
    # putting the name in the list
    first_list.append(input('Nome: ').title())
    # putting the weight in the list
    first_list.append(float(str(input('Peso: ').replace(',', '.'))))
    # start the heaviest and lightest
    if len(second_list) == 0:
        heaviest = lightest = first_list[1]
    else:
        # check and put the heaviest or lightest in the place
        if first_list[1] > heaviest:
            heaviest = first_list[1]
        if first_list[1] < lightest:
            lightest = first_list[1]
    second_list.append(first_list[:])
    first_list.clear()

    while True:  # Force to the user to choice a valid answer
        r = input('Do you want to continue? [Y/N]: ').upper()
        if r == 'N':
            break
        print('Enter a valid option')
    break

# ----- Output Zone -----
print('-' * 30)
print(f'The heaviest with: {heaviest}kg is ', end='')
for p in second_list:
    if p[1] == heaviest:
        print(f'{p[0]} ', end='')   # Check in the list: What is the name of the heaviest person?.
print('\n')
print(f'the lightest with: {lightest}kg is ', end='')
for p in second_list:
    if p[1] == lightest:
        print(f'{p[0]} ', end='')   # Check in the list: What is the name of the lightest person?.

input('Enter to Exit')
