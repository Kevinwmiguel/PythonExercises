"""
Ex 54 - make a program that reads the weight of five people. At the end show what was the highest and lowest weight read

"""
# ------ Input zone ------
hv = 0
lt = 100

for c in range(0, 5):
    peso = input('Enter the weight: ').replace(',', '.')
    peso = float(peso)
    if peso > hv:
        hv = peso
    if peso < lt:
        lt = peso
print(f'heaviest: {hv}')  # Show the highest number entered
print(f'lighter: {lt}')  # show the lowest number entered

input('Enter to exit')
