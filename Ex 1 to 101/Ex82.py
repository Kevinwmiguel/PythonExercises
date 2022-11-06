"""
Ex 82 - Create a program that reads the name and
         two notes of several students
         and stores everything in a compound list.
         at the end show, a grades report card containing the average of each
         one and allow the user to show the grades of each student individually
"""
# ----- Import -----
import numpy  # importing numpy to take the mean - VERY USEFUL


# ----- Function -----
def line():
    print('-' * 25)


# ----- Var -----
note = []
notes = []
name_student = []
total = 0
m = []

# ----- Loop -----
while True:    # loop to enter the student name and grade
    total += 1
    name = str(input('Name: ')).strip().capitalize()
    if name.isnumeric():   # Validator
        print('Please enter a valid name')
        continue
    name_student.append(name)
    note.append(float(str(input('Note 1: ')).replace(',', '.')))  # be sure if the user use comma and not 
    note.append(float(str(input('Note 2: ').replace(',', '.'))))  # point to split the decimal
    m.append(numpy.mean(note))
    notes.append(note[:])
    note.clear()
    while True:   # Validator
        answer = input('Do you want to continue? [Y/N]').upper()
        if answer in 'NY':
            break
        else:
            print('Please enter a valid option between "YES and NO" ')
    if answer == 'N':
       break
line()
print(f'{"No.":<4} {"Name":<10}{"Mean":>8}')
line()
for c in range(0, total):
    print(f'{c:<4} {name_student[c]:<10} {m[c]:>8.1f} ')  # Show a Grade of all the students
line()

while True:
    opt = str(input('show grades for which student? (999 Stop): '))
    if opt.isalpha():    # Validator
        print('Please enter a valid option (just numbers)')
        continue
    opt = int(opt)  # Cast the var str to int
    print(f'Notes of {name_student[opt]} are {notes[opt]}')    # Show just the grade of the chosen students
    if opt == 999:
        break

input('Enter to Exit')
