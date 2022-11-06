"""
Ex 11 - Make a algorithm that reads the wall's height and width in meters, calculate its area and how many liters ink is necessary to paint it, knowing that each liter of ink can paint 2m² of area
"""

print('calculate the paint needed to paint the wall: ')
print('-=' * 30)

h = input('Enter height: ').replace(',','.')
w = input('Enter the width: ').replace(',','.')

h = float(h)
w = float(w)

area = h * w
ink = area / 2

print(f'Dimension: {w:.2f} height x {h:.2f} width = area {area:.2f}m² ')
print(f"You'll need {ink:.2f}L of ink")

input('Enter to exit')
