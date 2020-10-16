print('Multiplication table')
print('-' * 30)

n = int(input('Enter a number: '))
print('-' * 10)
#the FOR repeat loop will loop until the condition is met.
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')
print('-' * 10)

input()
