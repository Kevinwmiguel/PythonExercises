"""
Ex 52 - Create a program that reads any sentence and says if it is a palindrome, disregarding spaces
"""

# ------ input zone ------
phrase = str(input('Type the phrase: ')).strip().upper()
newph = phrase.replace(' ', '')  # take the spaces out of the phrase
p = newph[len(newph)::-1].upper() # p receive the newph reversed

print(p)

if p == newph:
    print("it's a palindrome")
else:
    print('it is not a palindrome')

input('Enter to exit')
