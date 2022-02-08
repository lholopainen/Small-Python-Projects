#1. Create a greeting for your program.
print('Welcome to the tip calculator.')
#2. Ask the user what was the total bill.
total_bill = input('What was the total bill? $')
#3. Ask the tip percentage.
tip_percentage = input('What percentage tip would you like to give? 10, 12 or 15?')
#4. Ask the number of people to split the bill.
num_of_people = input('How many people to split the bill?')
#5. Calculate payment per person and print it.
payment_per_person = float(total_bill) * (int(tip_percentage) / 100 + 1) / int(num_of_people)
payment_per_person = round(payment_per_person, 2)
print('Each person should pay: ${}'.format(payment_per_person))
