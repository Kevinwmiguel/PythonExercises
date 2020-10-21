"""
Ex 22 - create a program that reads a person's full name and shows:

- The name in all uppercase and lowercase letters.
- How many letters in all (without considering spaces).
- How many letters have the first name.
"""
n = str(input('Type your full name '))
print('your Name in uppercase: ',n.upper())
print('Your Name in lowercase',n.lower())
div1 = n.split()
print(f'Your first name have {len(div1[0])} letters')
n = n.replace(" ","")
print(f'Your full name have :{len(n)} letters')

input()
