"""
Ex 48 - Create a multiplication table
"""

# Enter the number
t = int(input('Enter the number to be calculated on the multiplication table: '))
print('-=' * 8)

# Loop and Calculation
for c in range(1, 11):
    print(f'||{c} x {t:2} =\t{t * c}||')
print('-=' * 8)

input()
