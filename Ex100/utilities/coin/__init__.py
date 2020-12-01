def summary(p,c=10,x=5):
    print('-' * 30)
    print(f'Value Summary'.center(30))
    print('-' * 30)
    print(f'{"analyzed price:"}   \t{coins(p)}')
    print(f"{'Half-price: '}      \t{half(p, True)}")
    print(f'{"double the price: "}\t{double(p, True)}')
    print(f'{c}% {"increase: ":}  \t{increase(p, c, True)}')
    print(f'{x}% {"reduction: "}  \t{reduction(p, x, True)}')
    print('-'*30)
def increase(p = 0, por= 0, formato=False):
   #increase the desired%
    """
     => Function that increases the price by the desired percentage
     : param p: original price
     : param por: desired percentage
     : param format: formatting if desired
     : return: returns the price to the variable
     """
    p = ((p / 100) * por) + p
    return p if formato is False else coins(p)
def reduction(p = 0, por= 0, formato=False):
    """
    => Function that decreases the price by the desired percentage
    :param p: Original price
    :param por: porcentagem desejada
    :param formato: formatting if desired
    :return: returns the price to the variable
    """
    p = p - ((p / 100) * por)
    return p if not formato else coins(p)
    #Reduction the desired %

def double(p = 0, formato=False):
    """
        => Function that doubles the price
        :param p: Original price
        :param formato: formatting if desired
        :return: returns the price to the variable
        """
    p = p * 2
    return p if not formato else coins(p)
    #dobra o preço
def half(p = 0, formato=False):
    """
    => Function that cuts the price in half
    :param p: Original price
    :param formato: formatting if desired
    :return: returns the price to the variable
    """
    p = p / 2
    # Half-Price
    return p if formato is False else coins(p)
def coins(p = 0, moeda = 'R$'):
    """
    => Formatting function
    :param p: Original price
    :param moeda: currency
    :return: returns the formatted price
    """
    return f'{moeda}{p:>.2f}'.replace('.',',')