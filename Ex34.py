"""
Ex 34 - Create a program that reads a salary and shows on the screen the new salary with 15% increase. If the salary is highest that 1250 just give 10% increase
"""
s = float(input('Enter your salary: '))

# increase
if s > 1250:
    s = (s / 100) * 10 + s
else:
    s = (s/100) * 15 + s
# shows the new salary
print(f'Your new salary is: {s:.2f}')

input()
