"""
Ex 35 - Do a program that reads three number and shows on the screen if they can be a triangle and what kind of triangle
"""
# Enter the sides of triangle

r1 = float(input('Size of the first line: '))
r2 = float(input('Size of the second line: '))
r3 = float(input('Size of the third line: '))

# testing if the sides can turn a triangle

if r3 >= r1 + r2 or r1 >= r2 + r3 or r2 >= r3 + r1:
    print('Cannot :/')
else:
    print('Can')

# descovering what kind of triangle 

    if r1 == r2 and r2 == r3:
        print('The triangle is equilateral')
    elif r1 == r2 and r2 != r3 or r1 == r3 and r3 != r2 or r2 == r3 and r3 != r1:
        print('The triangle is isosceles')
    else:
        print('The triangle is Scalene')

input('Enter to exit')
