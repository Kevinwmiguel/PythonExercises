"""
Ex 31 - Develop a program that asks the distance of a trip in Km. Calculate the ticket price, charging 0.50 per km for trips of up to 200km and 0.45 for longer trips
"""

km = int(input('How many Km has your trip?: '))
price = km * 0.50 if km <= 200 else km * 0.45
print(f"The total price payable is: {price:.2f} ")

input()
