"""
Ex 29 - Write a program that reads the speed of a car. if it exceeds 80km/h. show a message saying he was fined. The fine will cost 7 dollars for each km above the limit
"""
v = int(input('Enter the current car speed: '))
m = v - 80
if v >= 81:
    m = m * 7
    print('you overstepped, you got a ticket! ')
    print(f'Your payment penalty is: {m} Dollars')
else:
    print("Good, you're following the rules. have a nice day!")

input('Enter to exit')
