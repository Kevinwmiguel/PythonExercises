"""
Ex 89 - Make a program that has a function called area (), that takes
the dimensions of a rectangular terrain (width and length) and shows its
area of the terrain

"""


def line():
    print('='*20)


def area(x, y):
    r = x * y
    print(f'The area of {x:.2f} x {y:.2f} is {r:.2f}m²')


line()
print('Land Control'.center(20))
line()
L = float(input('wight (m): '))
c = float(input('length (m): '))
line()
area(L, c)

input('Enter to exit')
