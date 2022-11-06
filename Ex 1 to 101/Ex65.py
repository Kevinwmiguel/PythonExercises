"""
Ex 65 - Create a tuple fully with a count in full,
from zero to twenty. your program should read a number
 on the keyboard (between 0 and 20) and show it in full.

"""
numbers = ('Zero', 'one', 'two', 'Three', 'Four', 'Five',
           'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
           'twelve', 'Thirteen', 'fourteen', 'fifteen',
           'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')


def line():
    print('-=' * 15)


line()
print('write the number in full')
line()

while True:
    num = int(input('Enter a number between 0 and 20: '))
    if 0 <= num <= 20:
        print(f'You entered {numbers[num]}')
        break
    else:
        print('Try again ')

input('Enter to exit')
