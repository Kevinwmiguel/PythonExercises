"""
EX 43 - Design a program that calculates the amount
 to be paid for a product, considering its normal price
 and payment terms:
- CASH / CHECK: 10% Off
- Cash on card: 5% off
- Up to 2x on credit card: normal price
- 3x or more on credit card: 20% interest
"""

# -------------------- Header --------------------
print('-=' * 15)
print('SuperMarket'.center(30))
print('-=' * 15)

#  -------------------- input zone --------------------
p = float(input("Enter the product's price: "))
print('-=' * 20)

esc = int(input(f'\t[1] Cash / cash check (\033[36m 10% off \033[m)\n'           # options to the User
                ' \t[2] cash payment on card (\033[36m 5% off \033[m)\n'
                ' \t[3] up to 2x on the card (\033[32m normal price \033[m)\n'
                ' \t[4] up to 3x or more (\033[31m 20% interest \033[m)\n'
                '\nChoose the payment way: '))

while True:  # Block to force the user to choice a right option
    try:
        # putting a discount or interest
        if esc == 1:
            p = p - (p / 100 * 10)
            print(f'The price to be paid will be: {p:.2f}')
        elif esc == 2:
            p = p - (p / 100 * 5)
            print(f'The price to be paid will be: {p:.2f}')
        elif esc == 3:
            print(f'The price to be paid will be: {p:.2f}')
        elif esc == 4:
            p = (p/100 * 20) + p
            print(f'The price to be paid will be: {p:.2f}')
        break
    except ValueError:
        print(f'did you entered a invalid value')

input()
