"""
Ex 79 - Create 1 program where the user can enter 7 numeric values
 and register them in 1 single list that keeps even and
 odd values separated at the end and show even and odd values
  in ascending order

"""

Numbers = [[], []]
for c in range(1, 8):
    n = int(input(f'Enter the {c}° value: '))
    if n % 2 == 0:
        Numbers[0].append(n)
    else:
        Numbers[1].append(n)
print(f'the entered even values were: {sorted(Numbers[0])}')
print(f'the entered odd values were {sorted(Numbers[1])}')

input('Enter to exit')
