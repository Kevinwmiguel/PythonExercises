"""
Ex 59 - Write a program that reads any integer and shows the first n elements of a fibonacci sequence on the screen

"""
# ----- Input zone -----
f1 = c = 0
f2 = f3 = 1
n = int(input('How many terms do you want?: '))

# ----- Loop Zone -----
while c <= n:
    print(f'{f1} - ', end='')
    f1 = f2
    f2 = f3
    f3 = f1 + f2
    c += 1

input('Enter to exit')
