"""
Write a program that asks how many KM a rental car has driven and how many days it has been rented. Calculate the price to pay, knowing that the car costs 60 a day and 0.15 per km driven
"""

d = int(input('Enter the number of days: '))
km = int(input('Enter the number of kilometers: '))
day = d * 60
kmr = 0.15 * km
print(f'The total amount to be paid is {kmr+day:.2f}')

input()
