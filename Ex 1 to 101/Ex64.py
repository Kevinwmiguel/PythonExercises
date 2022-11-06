"""
EX 64 - Create a program that simulates the functioning of an ATM.
at the beginning ask the user what will be the amount to be withdrawn (whole number)
 and the program will inform how many bills of each amount will be delivered
 OBS: consider that the cashier has bills of 50 20 10 and 1

"""

# ----- import zone -----
from emoji import emojize           # using a emojis in program

# ----- Function zone -----

def line():
    print('==' * 20)


def header():
    line()
    print('KW BANK'.center(40))
    line()


# ----- Begin -----
header()

# ----- Var Zone -----
v = int(input('How much do you want withdraw?: '))
c = v
c1 = c5 = c10 = c20 = c50 = c100 = c200 = 0

# ----- Loop Zone -----
while c != 0:                                                               # Check if the current money is higher 
    if c >= 200:                                                            #than the bill and if is add a bill with 
        c200 = c200 + 1                                                     #the right value. And discont this money to the money
        c = c - 200
    elif c >= 100:
        c100 = c100 + 1
        c = c - 100
    elif c >= 50:
        c50 = c50 + 1
        c = c - 50
    elif c >= 20:
        c20 = c20 + 1
        c = c - 20
    elif c >= 10:
        c10 = c10 + 1
        c = c - 10
    elif c >= 5:
        c5 = c5 + 1
        c = c - 5
    else:
        c1 = c1 + 1
        c = c - 1
# ----- Conditional Zone -----
if c200 >= 1:                                                                                                # check if the note exist and if True put 
    print(emojize(f'\033[30;43mtotal of {c200} bill of R$200 \033[m :wolf:', use_aliases='True'))            #print the number of notes the user will    
if c100 >= 1:                                                                                                # get
    print(emojize(f'\033[36mtotal of {c100} bill of 100\033[m :fish:', use_aliases='True'))                  
if c50 >= 1:
    print(emojize(f'\033[30;45mtotal of {c50} bill of 50\033[m :tiger:', use_aliases='True'))
if c20 >= 1:
    print(emojize(f'\033[34mtotal of {c20} bill of 20\033[m :monkey_face:', use_aliases='True'))
if c10 >= 1:
    print(emojize(f'\033[32mtotal of {c10} bill of 10\033[m :snake:', use_aliases='True'))
if c5 >= 1:
    print(emojize(f'\033[30;41mtotal of {c5} bill of 5\033[m :bear:', use_aliases='True'))
if c1 >= 1:
    print(emojize(f'\033[30;42mtotal of {c1} bill of 1\033[m :bird:', use_aliases='True'))
line()
print('Come Again To The KW BANK ! Have a Great Day')

input()
