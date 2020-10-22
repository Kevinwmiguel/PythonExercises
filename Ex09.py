""""
Ex 09 - Make a program that reads an integer and shows it on the display its multiplication table
"""

print('Multiplication table')
print('-' * 30)

n = int(input('Enter a number: '))
print('-' * 10)
#the FOR repeat loop will loop until the condition is met.
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')
print('-' * 10)

input()
