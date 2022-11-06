"""
Ex 63 - create a program that reads the name and
price of various products. the program should ask
if the user will continue. At the end, show:
A) what is the total amount spent on the purchase
B) how many products cost more than 1000
C) What is the cheapest product name
"""
# ----- Function -----
def line():
    print('=' * 20)


def header():
    line()
    print('CHEAPEST STORE'.center(20))
    line()

# ----- Header -----
header()

# ----- var zone -----
total_price = expensive = current_price = count = 0
p_name = ''


# ----- Loop Zone ----- 
while True:
    product_name = str(input('Product name: ')).strip()
    price = float(input('Price: '))
    total_price = total_price + price
    if price > 1000:
        expensive = expensive + 1
    if count == 0:
        current_price = price
    if price <= current_price:
        current_price = price
        p_name = product_name
    count = count + 1
    answer = str(input('Do you want to continue? [Y/N]: ')).upper()
    if answer == 'N':
        break
line()
print(f'The total was RS{total_price}')
print(f'Has {expensive} products that cost more than 1000,00')
print(f'The cheapest product was {p_name} with the price of {current_price}')
line()
input('Enter to exit')
