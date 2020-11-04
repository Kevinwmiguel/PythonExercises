"""
Ex 72 - make a program that reads 5 numerical values
and save them in a list. at the end, show which was the highest
and lowest value entered and their respective positions in the list

"""
# starting a list
value = []

for c in range(0, 5):           # enter the Value to the list
    value.append(int(input(f'Value to position {c}: ')))

# Take highest and lowest numbers in list
highest = max(value)
lowest = min(value)

#
print('='*25)
print(f'Entered values {value}')

# take the max value and show the position of the number in the list
print(f'The max value: {highest} at position ', end='')
for i, p in enumerate(value):
    if p == highest:
        print(f'{i}...', end='')

# take the min value and show the position of the number in the list
print(f'\nThe min value: {lowest} at position ', end='')
for i, p in enumerate(value):
    if p == lowest:
        print(f'{i}...', end='')

input()
