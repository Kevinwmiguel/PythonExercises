"""
Ex 73 - Create a program where the user can enter several numerical
 values and register them in a list. if the number
  already exists inside it, it will not be added. at the end 
  display the values in ascending order

"""

# ----- Var -----
Value = list()

# ----- Loop -----

while True:
    print('-=' * 15)
    n = int(input('Enter a Value: '))
    if n not in Value:
        Value.append(n)     # Added the value in a list
        print('Value was added')
    else:
        print('This value already in list, give another one')
    r = input('Do you want continue? [Y/N]: ').upper()
    if r in 'N':
        break

print(sorted(Value))        # show the list Value in order

input('Enter to exit')
