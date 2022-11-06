"""
Ex 95 - Create a program that has a factorial 
function() that receives two parameters: the first that indicates 
the number to be calculated and the other called show, which will be a logical value 
(optional) indicating whether or not the  factorial calculation process is shown on the screen

"""


def factorial(n, show):
    """
    => calculates the factorial of a number.
    :param n: The number to be factored.
    :param show: (Optional True or False) shows the process or not.
    :return: return the value and shows it
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    return f


num = int(input('Type a number to be factored: '))

print(factorial(num, show=True))
help(factorial)

input('Enter to exit')
