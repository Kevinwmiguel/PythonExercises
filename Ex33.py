"""
Ex 33 - Make a program that reads three numbers and shows which is the largest and which is the smallest
"""
a = int(input('Type the first number: '))
b = int(input('Type the second number: '))
c = int(input('Type the third number: '))

# declaring variables
bigger = 0
smaller = a

# the biggest and smallest numbers
if b < a and b < c:
    smaller = b
if c < a and c < b:
    smaller = c
bigger = a
if c > a and c > b:
    bigger = c
if b > a and b > c:
    bigger = b

# shows the results
print(f'The biggest number is: {bigger}')
print(f'The smallest number is: {smaller}')

# The easy way
print('-' * 30, '\n Easy way')
print(f'biggest: {max(a, b, c)}')
print(f'smallest: {min(a, b, c)}')

input()
