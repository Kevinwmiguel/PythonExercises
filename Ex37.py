"""
Ex 37 - Write a program that reads any integer and ask the user to choose the conversion base:
- 1 Binary 
- 2 Octal
- 3 hexadecimal

"""

from time import sleep

print('\033[1;34m-=' * 15)
print('Number conversion'.center(30))
print('\033[1;34m-=\033[m' * 15)
n = int(input('Enter a integer: '))
print('\033[1;32m [1] To Binary \n [2] To Octal \n [3] To Hexadecimal\033[m')
op = int(input(': '))
print('\033[4;32mProcessing...\033[m')
sleep(2)
if op == 1:
    print(f'The number in binary is: {bin(n)[2:]}')
elif op == 2:
    print(f'The number in Octal is {oct(n)[2:]}')
elif op == 3:
    print(f'The number in Hexadecimal is  {hex(n)[2:]}')
else:
    print('\033[31msorry something went wrong, try again on next time.')

input('Enter to exit')
