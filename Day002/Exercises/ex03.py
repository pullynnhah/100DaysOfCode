age = int(input("What is your current age? "))

years_left = 90 - age
months_left = round(years_left * 12)
weeks_left = round(years_left * 52)
days_left = round(years_left * 365)
print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.')
