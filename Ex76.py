"""
Ex 76 - Create a program that will read several numbers and
 put them on a list. After that, create two extra lists that
 will contain only the even values and the odd values
 entered, respectively. At the end show the content of
 the three lists generated
"""
# ----- Var -----
List = list()
list_e = list()  # list to Even numbers
list_o = list()  # list to odd numbers

# ----- Loop ----
while True:
    r = ''
    n = int(input('Enter a Value: '))
    List.append(n)
    if n % 2 == 0:
        list_e.append(n)
    else:
        list_o.append(n)
    while r != 'N' and r != 'Y':    # Force the user to choice a right option ( between Yes or No).
        r = input('Do you want to continue ?  [Y/N]: ').upper().strip()
        if r != 'Y' and r != 'N':
            print('Please enter a acceptable answer')
            continue
    if r == 'N':
        break
print(f'The complete list {sorted(List)}')
print(f'The list just with even numbers {sorted(list_e)}')
print(f'The list just with odd numbers {sorted(list_o)}')

input('Enter to exit')
