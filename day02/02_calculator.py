print('Welcome to the tip calculator!')

total_bill = float(input('What is the total bill amount?\n'))

tip = float(input('How much tip would you like to give?\nPercent: '))

print('How many people to split the bill?')
people = int(input('People: '))

tip = (6/100) * total_bill

total_bill = total_bill + tip

bill_per_person = total_bill / people

print("Each person should pay: ", bill_per_person)
