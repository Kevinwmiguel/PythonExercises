"""
Ex 71 - Ex Create a program that has a tuple with several words.
After that, you must show, for each word, what are your vowels

"""

words = ('Learning', 'Programmer', 'Book', 'Notes', 'Windows', 'Linux', 'MAC-OS',
         'Github', 'Logic', 'Numpy', 'Pandas', 'Lambda', 'C', 'OOP')

for c in words:
    print(f'\nIn the word {c} we have ', end='')    # iteration in the words list
    for g in c:
        if g.lower() in 'aeiou':        # If the word have a vowel, shows it on the screen
            print(g, end=' ')

input('Enter to exit')
