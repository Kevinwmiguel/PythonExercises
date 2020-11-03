"""
70 - Create a program that has a unique tuple with product names and prices.
At the end, it shows a price list, organized with tabular data
"""
items = ('Pencil', 1,
         'Eraser', 3.20,
         'Book', 4,
         'Color pencil', 3,
         'Snacks', 3.50,
         'Pen', 2,
         'Table', 8,
         'Case', 3)


# ----- Function -----
def line():
    print('=' * 35)


def header():
    line()
    print(f'{"Price List"}'.center(35))
    line()


# ----- Header -----
header()

# ----- Loop -----
for c in range(0, len(items)):          # if C equal a even number, show the name of product, else show the price
    if c % 2 == 0:
        print()
        print(f'{items[c]:.<30}', end='')
    else:
        print(f'{items[c]:>1.2f}')

input('\nEnter to Exit')
