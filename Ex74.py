"""
Ex 74 - Create a program where the user can enter five numeric 
values and register them in a list, already in the correct 
insertion position (without using sort ()). at the end show the 
ordered list on the screen
"""
# ----- Var -----
values = list()

# ----- Loop -----
for c in range(0, 5):
    n = int(input('Enter a value: '))
    if c == 0 or n > values[-1]:  # if the count == 0, or n highest than the
        values.append(n)          # last value, add the number on the last position
        print('Value added in the last position...')
    else:
        pos = 0
        while pos < len(values):  # if n lowest than the values in
            if n <= values[pos]:  # count position, add n to that position
                values.insert(pos, n)
                print(f'Value added in the position {pos}..')
                break       # Break the loop if find the condition to add the number
            pos += 1

print('-=' * 15)
print(values)

input('Enter to exit')
