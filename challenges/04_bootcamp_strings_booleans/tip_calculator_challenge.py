# DO NOT WORRY ABOUT THE LINES BELOW THIS LINE
def format_currency(amount: float) -> str:
    return "${:,.2f}".format(amount)
# DO NOT WORRY ABOUT THE LINES ABOVE THIS LINE

# CHALLENGE 1.2:
# Get number of people splitting the bill and convert from string to int
num_people_str = input("> Type the number of people splitting this bill: ")
num_people_int = int(num_people_str)

# CHALLENGE 1.3:
#Get bill amount and convert from string to float
bill_total_str = input("> Total of bill to be split: ")
bill_total_float = float(bill_total_str)

# Get percentage to tip and convert from string to float
tip_percent_str = input("> What tip did you want to leave? Percentage%: ")
tip_percent_float = float(tip_percent_str)

# CHALLENGE 1.4:
# Confirm input with user
print(f"You are splitting {(bill_total_float)} among {num_people_int} people with a {tip_percent_float}% tip.")
confirm_input = input("> Type y if this input is correct, or any other key to quit: ")
correct_input = confirm_input == 'y'

# Don't worry about this if statement! We will review later!
if correct_input == False:
    print("Incorrect input. Quitting...")
    exit()

# Q: What is the data type of confirm_input? 
print("The confirm input is a string")
# Q: What is the data type of correct_input?
print('It is a boolean')
# CHALLENGE 1.5:
# Split bill and print amount
amount_per_person = bill_total_float/num_people_int
tip_per_person = amount_per_person * tip_percent_float/100
total_per_person = amount_per_person + tip_per_person
print(f"the bill is split so each person is {amount_per_person}!")
print(f"The previous equation is NOT INCLUDING the tip so don't be stingy!!{tip_per_person}")
print(f"After this wonderful meal and including the tip each person should pay {total_per_person}!")

