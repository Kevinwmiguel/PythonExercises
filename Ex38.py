"""
Ex 38 - Write a program that reads two integer and compare them, showing a message on the screen:
- The first value is greater  
- the second value is greater 
- there is no greater value, the two are equal
"""


n1 = int(input('Enter the first value: '))

n2 = int(input('Enter the second value: '))

if n1 > n2:
    print(f'The first value {n1} is highest')
elif n2 > n1:
    print(f'The second value {n2} is highest')
else:
    print(f'the values {n1} and {n2} are equals: ')

input('Enter to exit')
