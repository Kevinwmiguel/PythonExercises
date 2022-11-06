"""
Ex 97 - Create a program that has the function readInt(),
which will work in a similar way to Python's input() function, but doing
the validation to accept only a numeric value.
"""


def read_int():
    while True:
        n = input('Type a integer number: ')
        if n.isnumeric():
            break
        else:
            print('\033[1;31mError, enter a integer number\033[m')
    return n


number = read_int()
print(f'The number entered was {number}')

input('Enter to Exit')
