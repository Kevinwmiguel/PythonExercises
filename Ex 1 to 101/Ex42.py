"""
Ex 42 - Develop a logic that reads a person's weight and height, calculates the BMI and shows their status according to the table below:
- under 18.5: underweight
- between 18.5 and 25: ideal weight
- 25 to 30: overweight
- 30 to 40: obesity
- over 40: morbid obesity

"""
# -------------------- Header --------------------
print('-=' * 15)
print('BMI ')
print('-=' * 15)

#  -------------------- input zone --------------------
a = float(input('Enter your height:'))
p = float(input('Enter your weight: '))

# var created to calculate the BMI
BMI = p / (pow(a, 2))

# Conditional to see the right place of the person on the table
if BMI < 18.4:
    print('underweight')
elif BMI >= 18.5 and BMI == 24.9:
    print('ideal weight')
elif BMI >= 25.0 and BMI == 29.9:
    print('overweight')
elif BMI >= 30.0 and BMI == 39.9:
    print('Obesity')
else:
    print('morbid obesity')
    
input('Enter to exit')
