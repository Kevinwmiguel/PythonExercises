"""
Ex 10 - Create a program that reads how much money a person have on the wallet and shows how much Dollars it can buy
"""
print('Euro to Dollar')

print('-' * 20)

value = str(input('Money in the wallet: ')).replace(',', '.')
print('-' * 20)

Euro = 1.17

print('DATE: 2020/10/16')
print(f'With the value R $ {float(value):.2f} you can have {float(value) / Euro:.2f} Euros')

input('Enter to exit')
