"""
Ex 57 - Create a program that reads two values and displays a menu.
Your program should perform the requested operation in each case.
 - 1 Add
 - 2 multiply
 - 3 larger
 - 4 new numbers
 - 5 exit the program

"""


def line():
    print('-=' * 10)


def header():
    print('-=' * 14)
    print("Calculator prototype".center(28))
    print('-=' * 14)


# var
choices = 0
result = 0

# header
header()

# input
n1 = int(input('1° Value: '))
n2 = int(input('2° Value: '))

# loop
while choices != 5:
    esc = int(input(f'\t[1] Sum \n'
                    f'\t[2] Multiply\n'
                    f'\t[3] Highest \n'
                    f'\t[4] New numbers\n '
                    f'\t[5] Exit the program\n'
                    f'Your option: '))
    if esc == 1:
        result = n1 + n2
        print(f'\033[36mthe sum is: {result}\033[m')
        line()
    elif esc == 2:
        result = n1 * n2
        print(f'\033[36mthe multiply is: {result}\033[m')
        line()
    elif esc == 3:
        if n1 >= n2:
            print(f'\033[36mThe highest number is: {n1}\033[m')
            line()
        else:
            print(f'\033[36mthe highest number is: {n2}\033[m')
            line()
    elif esc == 4:
        n1 = int(input('1° Value: '))
        n2 = int(input('2° Value: '))
        line()
    elif esc == 5:
        choices = esc
    else:
        print('\033[31mInvalid Option, Try again!\033[m')

input('Enter to exit')
