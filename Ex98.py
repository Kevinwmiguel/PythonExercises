"""
Ex 98 - Make a program that has a grades function()
that can receive multiple grades from a student
and will return a dictionary with the following information:
- Quantity of school grades
- the highest grade
- the lowest grade
- the class's mean
- the situation of the student (optional)
PS: add too docstrings
"""


def notes(*num, sit=False):  # Function to return a dictionary and check all the conditions
    """ 
    => Program that checks the quantify of school grades, highest, lowest, the class mean and the student's situation
    :param num: variable that receive the amount of notes
    :param sit: (optional) if wish know the student's situation set sit=True
    :return: return everything in a dictionary.
    """

    dictionary = dict()
    s = 0
    tot_sum = 0
    for c in num:   # Sum the total grades school
        s += 1
        tot_sum = tot_sum + c
    dictionary['Total'] = s
    dictionary['Lowest'] = min(num)
    dictionary['Highest'] = max(num)
    m = tot_sum / s
    dictionary['Mean'] = round(m, 2)
    if sit:  # check if the situation is True or False
        if m > 7:
            dictionary['Situation'] = 'Approved'
        else:
            dictionary['Situation'] = 'Reproved'
    return dictionary


print('-' * 60)
help(notes)  # print the docstrings to the user understand how the function works
print('-' * 60)
resp = notes(8.8, 6.5, 9.5, sit=True)  # The notes that the student got and the situation
print(resp)

input('\nEnter to exit')
