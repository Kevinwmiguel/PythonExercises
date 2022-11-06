"""
Ex 014 - Write a program with the temperature given in degrees Celsius and convert it to fahrenheit
"""

c = float(input('Enter degrees celsius: '))

f = (1.8 * c) + 32

print(f'°C{c:.2f} to fahrenheit goes to {f:.2f}°F')

input('Enter to exit')
