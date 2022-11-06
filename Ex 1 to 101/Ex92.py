"""
Ex 92 - Make a program that has a function called greater (), that receives 
several parameters with integer values. your program has to analyze all the 
values and tell which one is the biggest

"""

from time import sleep


def line():
    print('-='*25)
    
    
def highest(*num):
    s = 0
    if not num:  # Make sure to run the program if the value is zero
        print('Analysing the entered values...')
        num = 0
        print(f'In total {s} values were informed ')
        print(f'The highest value was {num}')
    else:
        print('Analysing the entered values...')
        sleep(0.5)
        for n in num:
            s += 1
            print(f'{n} ', end='', flush=True)
        print(f'In total {s} values were informed ')
        num_2 = max(num)
        print(f'the highest value was  {num_2}')  # Show the highest number informed
        line()


highest(2,9,4,5,7,1)
highest(4,7,0)
highest(1,2)
highest(6)
highest()

input('Enter to exit')
