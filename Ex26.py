"""
Ex 26 - Make a program that reads a sentence on the keyboard and shows:
=> How often does the letter A appear
=> In what position does she appear for the first time?
=> In what position does she appear for the last time
"""

name = str(input('Enter Any phrase: ')).upper().strip()

print(f'The letter A appears {name.count("A")} times in the sentence')

print(f'The first letter A appears in the position: {name.find("A")+1}')

print(f'The last letter A appears in the position: {name.rfind("A")+1}')

input('Enter to exit')
