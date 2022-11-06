"""
Ex 49 - Create a program that reads 6 numbers, if the number is even, add it and show it on the screen

"""
# input
s = 0

# loop
for c in range(0, 6):
    number = int(input('Number: '))
    if number % 2 == 0:
        s += number
# shows the sum
print(f'The total sum between even numbers is: {s}')

input('Enter to exit')
