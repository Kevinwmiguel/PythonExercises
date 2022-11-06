"""
Ex 47 - Make a program that starts counting from 1 to 501 and step 2 to 2
"""
# input
s = 0

# loop
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        s += c
print('\n')

# print the total sum numbers
print(f'The total sum of the numbers is: {s}')

input('Enter to exit')
