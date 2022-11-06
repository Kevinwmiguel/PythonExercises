"""
Ex 99 - make a mini-system that uses python's interactive help.
The user will enter the command and the manual will appear.
When the user types the word 'END', the program will end.

PS: use colors

"""


def help_system():
    while True:
        print('\033[m', end='')
        from time import sleep
        print('\033[30;42m~' * 25)
        print(" Help system PyHelp")
        print('~' * 25)
        var = input("\033[mLibrary's function : ")
        if var == 'END':
            break
        sleep(0.5)
        print('\033[1;30;44m~' * 30)
        print('  accessing command manual')
        print('~' * 30)
        sleep(0.5)
        print('\033[7;30;42m')
        help(var)


help_system()

input('Enter to Exit')
