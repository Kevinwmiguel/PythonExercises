"""
Ex 50 - Create a program that reads a number and shows the first 10 terms of this arithmetic progression of that number

"""

# Import zone
from time import sleep

# input zone
pa = int(input('first term of PA: '))
reason = int(input('Reason: '))
count = 0
terms = 10
extraterms = 1

# condition and show the result on the screen
while extraterms != 0:
    while count < terms:
        sleep(0.5)
        print(f'{pa} ')
        pa = pa + reason
        count = count + 1
    print('Finished')
    extraterms = int(input('How many more terms do you want? [ 0 To Exit] '))
    count = 0
    terms = extraterms

input()
