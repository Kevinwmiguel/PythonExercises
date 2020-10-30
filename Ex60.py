"""
Ex 60 - Create a program that reads several integers from the keyboard. the program will only stop when the user enters the value 999, which is the stop condition. at the end, show how many numbers were entered and what was the sum between them. (disregarding the flag)
"""


# ----- function -----
def header():
    print('\n')
    print('=' * 40)
    print('The program will stop when you press 999')
    print('=' * 40)
    print('\n')

    
# ----- Var -----
c = 0
tt = 0
tn = 0

# ----- Header -----
header()

# ----- Loop -----
while c != 999:
    c = int(input('Enter a number: '))
    if c != 999:
        tt += c
        tn += 1
print(f'You entered {tn} numbers')
print(f'The total sum is: {tt}')

input('Enter to exit')
