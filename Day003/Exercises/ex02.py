height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)
underweight = f"Your BMI is {bmi}, you are underweight."
normal_weight = f"Your BMI is {bmi}, you have a normal weight."
overweight = f"Your BMI is {bmi}, you are slightly overweight."
obese = f"Your BMI is {bmi}, you are obese."
clinically_obese = f"Your BMI is {bmi}, you are clinically obese."

if bmi < 18.5:
    print(underweight)
elif bmi < 25:
    print(normal_weight)
elif bmi < 30:
    print(overweight)
elif bmi < 35:
    print(obese)
else:
    print(clinically_obese)
