"""
Ex 61 - Create a program using multiple integers from the keyboard. 
at the end of the run, show the average of all values and which was 
the highest and lowest values read. the program should ask the user 
whether he wants to continue or not.

"""
# ----- Header Zone -----
print('-=' * 15)
print('Numbers'.center(30))
print('-=' * 15)
# ----- Var Zone -----
biggest = smallest = 0
m = n = c = 0
s = ''
# ----- Loop Zone -----

while s != 'N':
    n = int(input('Enter a number: '))
    c = c + 1
    if c == 1:              # if the C starts with one, the smallest and biggest will be equal to n
        smallest = biggest = n
    else:
        if biggest < n:
            biggest = n
        elif smallest > n:
            smallest = n
    m = m + n
    s = str(input('Do you want continue? [Y, N]: ')).upper()        # Test if the user want continue


m = m / c       # Calculate the mean

# ----- Output zone -----
print(f'The mean between all the {c} numbers entered is: {m:.2f}')
print(f'the biggest number was:  {biggest}')
print(f'the smallest number was: {smallest}')

input('Enter to exit')
