"""
Ex 013 - make an algorithm that reads an employee's salary and shows his new salary, with a 15% increase
"""

S = float(input('Enter the salary: '))

NS = (S/100) * 15 + S

print(f'the old salary of {S:.2f} with + 15% of increase goes to {NS:.2f}')

input()
