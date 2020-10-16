print('Double, Triple and Square root ')
print('-' * 30)

n = str(input('Enter a number: ')).replace(',', '.')
n = float(n)
print(f'the double of {n}: {n * 2:.2f}')
print(f'the triple {n:}: {n * 3:.2f}')
print(f'The square root {n}: {n ** (1/2):.2f}')

input()
