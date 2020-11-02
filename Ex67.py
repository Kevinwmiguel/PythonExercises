"""
Ex 67 - Draw five numbers, place them inside a tuple,
take the highest and lowest value

"""
# ----- Import Zone -----
from random import sample   # take some values in random

Random_number = tuple(sample(range(0, 1000), 5))  # Create a tuple with 5 numbers between 0 and 1000
print(Random_number)
print(f'The highest was: {max(Random_number)}')  # the highest value in the tuple
print(f'The lowest was: {min(Random_number)}')   # the lowest value in the tuple

input('Enter to Exit')
