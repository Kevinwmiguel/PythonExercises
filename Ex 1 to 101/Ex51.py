"""
Ex 52 - Make a program that reads an integer and
says whether or not it is a prime number

"""
# ------ Header ------
print('Discovering the number prime')

# ------ input zone ------
n = int(input(' Number: '))
tot = 0

# ------ loop zone -----
for c in range(1, n + 1):  # Make sure the number is divisible by other numbers
    if n % c == 0:
       print('\033[33m', end=' ')
       tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')

# ------ Result zone ------
print(f'\n\033[36mThe number {n} was divisible {tot} times')
if tot == 2:
    print('Prime numbers')
else:
    print('this number is not prime')

input('Enter to exit')
