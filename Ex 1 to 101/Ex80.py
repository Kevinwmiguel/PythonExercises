"""
Ex 80 - Create a program that creates a 3x3 dimension matrix and fills in values
read from the keyboard. At the end, show the matrix on the screen, with the correct formatting

"""


def line():
    print('-=' * 15)

# ----- Making a list as an Array/Matrix -----

matrix = [[[], [], []], [[], [], []], [[],  [], []]]

even = sum_third = 0
# ----- Loop to build a matrix -----
for c in range(0, 3):
    for d in range(0, 3):
        matrix[c][d] = int(input(f'Enter a Value [{c}, {d}]: '))
        if matrix[c][d] % 2 == 0:  # Check if the number is even
            even = even + matrix[c][d]
        if matrix[c][2]:        # Do the sum in the numbers of the third column
            sum_third = sum_third + matrix[c][2]
line()
# ----- Shows the matrix on the screen -----
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matrix[c][d]:^5}] ', end='')
    print()
line()
# ----- Result -----
print(f'The sum of the even values is: {even}')
print(f'The total sum of values in the third column is: {sum_third}')
print(f'The max value in the second line is: {max(matrix[1])}')

input('enter to exit')
