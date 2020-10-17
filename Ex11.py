print('calculate the paint needed to paint the wall: ')
print('-=' * 30)

h = float(input('Enter height: '))
w = float(input('Enter the width: '))
area = h * w
ink = area / 2

print(f'Dimension: {w:.2f} height x {h:.2f} width = area {area:.2f}m² ')
print(f"You'll need {ink:.2f}L of ink")

input()
