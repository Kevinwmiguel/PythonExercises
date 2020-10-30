"""
Ex 56 - Program that reads a person's gender and only accepts M or F. Otherwise ask again
"""
# ----- Function zone -----

def header():
    print('=' * 15)
print('Sex validator')
print('=' * 15)

# ----- Header ----- 
header()

sex = ''

while sex != 'M' and sex != 'F':
    sex = str(input('Enter your sex (M , F): ')).upper()        # the Upper function, make sure to convert the string on uppercase 
    if sex != 'M' and sex != 'F':
        print('\033[31mInvalid Sex, try again!\033[m')
print('\033[36mYou entered a valid sex!')

input('Enter to exit')