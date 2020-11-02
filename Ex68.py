"""
Ex 68 - Develop a program that reads four values from the keyboard and saves them has a tuple at the end show
a) How many times did the value 9 appear
b) What position was typed the value 3
c) Witch was the even numbers
"""
n = []
for count in range(0, 4):
    n.append(int(input('Enter a number: ')))
n = tuple(n)
print(f'You entered the values: {n}')
print(f'The 9 appeared: {n.count(9)} times')
if 3 in n:
    print(f'The value 3 appeared in: {n.index(3)+1}ª position')
print(f'the even numbers entered was: ', end=' ')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')

input()
