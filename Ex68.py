"""
Ex 68 - Develop a program that reads four values from the keyboard and saves them has a tuple at the end show
a) How many times did the value 9 appear
b) What position was typed the value 3
c) Witch was the even numbers
"""
# ----- Var -----
n = []

# ----- Loop Zone -----
for count in range(0, 4):
    n.append(int(input('Enter a number: ')))
n = tuple(n) # Cast the list to tuple

print(f'You entered the values: {n}')   # print all the tuple
print(f'The 9 appeared: {n.count(9)} times')  # Count how many times did the number 9 entered
if 3 in n:  # check if the number 3 was entered
    print(f'The value 3 appeared in: {n.index(3)+1}ª position')  # Check the position of the number 3
print(f'the even numbers entered was: ', end=' ')
for c in n:     # check if n tuple have even numbers and show on the screen
    if c % 2 == 0:
        print(c, end=' ')

input()
