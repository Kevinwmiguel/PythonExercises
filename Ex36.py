"""
 Ex 36 - Write a program to approve a bank loan for the purchase of a home. ask the value of the house, the buyer's salary and how many years he will pay. the monthly installment cannot exceed 30% of the salary or the loan will be denied
"""
print('\033[1;34m-=' * 15)
print('LOAN'.center(30))
print('\033[1;34m-=\033[m' * 15)
house_value = float(input('Enter the value of the house: '))
salary = float(input('Enter your salary: '))
year_paying = int(input('Payment years: '))

print('-=' * 13)
ml = year_paying * 12
installment = house_value / ml
pm = (salary / 100) * 30
if installment <= pm:
    print('\033[1;32m The loan was approved!\033[m')
    print(f'\033[1;30m The installment price will be: {installment:.2f}\033[m')
else:
    print("\033[1;31m the loan was denied !\033[m")
print('-=' * 13)

input('Enter to exit')
