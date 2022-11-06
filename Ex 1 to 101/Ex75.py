"""
Ex 75 - Create a program that will read several
numbers and put them on a list. After that, show:
A) how many numbers were entered
B) the list of values, ordered in descending order
C) if the value 5 was entered and is or is not in the list
"""
# ----- Var -----

Numbers = list()
tt = 0
five = ''

# ----- Loop -----
while True:

    n = int(input('Enter a value: '))
    Numbers.append(n)
    tt += 1
    # request a answer, if negative break the loop
    r = input('Do you want to continue? [Y/N]: ').upper()
    if r == 'N':
        break
    if 5 in Numbers:
        five = 'the value/number Five is in the list!'
    else:
        five = ''
# put the numbers in decreasing order
Numbers.sort(reverse=True)
print(f'You entered {tt} values')
print(f'decreasing values are {Numbers}')
# check if the number 5 is in the list
if five in Numbers:
    print(f'The value {five} is in the list')
print('-=' * 25)

input('Enter to Exit')
