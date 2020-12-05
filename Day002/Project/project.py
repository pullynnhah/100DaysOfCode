# 1. Create a greeting for your program.
print('Welcome to the tip calculator.')

# 2. Ask for the bill
prompt = 'What was the total bill? $'
bill = float(input(prompt))

# 3. Ask for the tip percentage
prompt = 'What percentage tip would you like to give? 10, 12 or 15? '
tip_rate = int(input(prompt)) / 100

# 4. Ask for the number of people to split the bill with.
prompt = 'How many people to split the bill? '
people = int(input(prompt))

# 5. Calculate the total bill and the bill per person.
total_rate = 1 + tip_rate
total_bill = bill * total_rate
bill_per_person = total_bill / people

# 6. Display the bill per person with 2 decimal places.
print(f'Each person should pay: ${bill_per_person:.2f}')
