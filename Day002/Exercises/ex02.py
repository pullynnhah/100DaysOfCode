# Don't change the lines below
height = float(input('Enter your height (m): '))
weight = float(input('Enter your weight (kg): '))

# Your code here
bmi = int(weight / height ** 2)
print('Your BMI is: ' + str(bmi))
