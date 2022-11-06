"""
Create a program that reads two grades of a student and calculates their average, showing a message at the end, according to the average achieved:

 - Average below 5.0: Failed 
 - Average between 5.0 and 6.9: recovery 
 - average 7.0 or higher: approved
 """
print('-=' * 15)
print("SCHOOL APPROVAL".center(30))
print('-=' * 15)

n1 = float(input('First school grade:'))

n2 = float(input('Second school grade:'))
print('-=' * 15)
m = (n1 + n2) / 2

if m < 5 and m >= 0:
    print(f'{m:.2f}: You were Disapproved')

elif m > 5 and m < 6.9:
    print(f'{m:.2f}: You are Recovering')

elif m >= 7:
    print(f'{m:.2f}: You were Aproved')
else:
    print('Invalid Note')

input('Enter to exit')
