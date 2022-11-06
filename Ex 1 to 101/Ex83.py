"""
Ex 83 - Make a program that reads a student's name and average,
also keeping the situation in a dictionary. At the end,
show the structure content on the screen
"""

student = {}

print('Please Enter just notes between 1 and 10')
student['Name'] = str(input('Student name: '))
# ----- Loop -----
while True:         # Make sure all notes are correct
    n1 = float(str(input('Note 1: ')).replace(',', '.'))
    if n1 > 10 or n1 < 0:
        print('please enter a valid note')
        continue
    else:
        pass
    n2 = float(str(input('Note 2: ')).replace(',', '.'))
    if n2 > 10 or n2 < 0:
        print('please enter a valid note')
    else:
        break

student['Mean'] = (n1 + n2) / 2  # Take the mean and put in a dictionary

if student['Mean'] > 7:  # Check and show the student's situation
    student['Situation'] = 'Approved'
else:
    student['Situation'] = 'Reproved'
print('-=' * 20)

# Shows the results on the screen
for k, v in student.items():
    print(f'{k} is equal: {v}')

input('Enter to exit')
