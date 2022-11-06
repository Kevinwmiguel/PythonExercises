"""
Ex 90 - Make a program that has a function called write(), that receives
 any text as a parameter and shows a message with an adaptable size.

"""


def write(sgx):
    tam = sgx + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


msg = str(input('Type your message: '))

write(len(msg))

input('Enter to exit')
