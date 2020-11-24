"""
Ex 93 - Make a program that has a list called numbers and two functions called draw() and somaPar().
The first function will draw 5 numbers and place them inside the list and the second function
will show the sum of all the even numbers drawn by the previous function
"""

from random import randint


def shuflle(x):  # Function raffle
    print('Sorting list values: ', end=' ', flush=True)
    for c in range(0, 5):
        x.append(randint(0, 20))
        print(x[c], end=' ', flush=True)


#  Function to sum even numbers
def sum_even(x):
    """
    # the program makes the sum of the even values in the list
    :param x: list of values that received random values by int from another function
    :return: returns a print with the sum of the even numbers.
    """
    c = 0
    s = 0
    for c in x:
        if c % 2 == 0:
            s = s + c
    print(f'\n\033[1;34;4mThe sum of the even values of the list {List} the value is:  {s}', end=' ', flush=True)
    return s


List = [6, 8, 9, 4, 5, 2, 3, 4, 8, 5, 6, 9, 8, 5, 6]

# principal
shuflle(List)
sum_even(List)
help(sum_even)

input('Enter to exit')
