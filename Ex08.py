print('Converter to measurement')

#print a character '-' 30 times on the screen to do a line

print('-' * 30)
m = float(input('Enter a measurement in meters: '))
print(f' Measure {m} corresponds to:')
print(f'{m / 1000} km')
print(f'{m / 100} hm')
print(f'{m / 10} dam')
print(f'{m * 10} dm')
print(f'{m * 100} cm')
print(f'{m * 1000} mm')

input()
