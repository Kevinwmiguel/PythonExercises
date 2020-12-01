def read_money(msg):
    valid = False
    while not valid:
        cash = str(input(msg)).replace(',', '.').strip()
        if cash.isalpha() or cash == '':
            print(f'\033[0;31mError: \"{cash}\" This is not a valid \033[m')
        else:
            valid = True
            return float(cash)

