print("Welcome to the tip calculator")

# TAKING ALL THE INPUT FROM THE USER
total_bill = float(input("What was the total bill?\n$"))
perc_tip = int(
    input("What percentage tip would you like to give? 10, 12, or 15? \n"))
no_of_people = int(input("How many people to split the bill?\n"))

# CALCULATING THE AMT TO BE PAID BY EVERYONE
total_splitamt = total_bill * perc_tip / 100
total_splitamt += total_bill
total_splitamt /= no_of_people

# PRINTING THE AMOUNT TO BE PAID TO THE USER
# print(f"Each person should pay: ${round(total_splitamt,2)}.")
# Doesn't print Rs. 22.50..Instead prints Rs. 22.5
final_splitup = "{:.2f}".format(total_splitamt)
print(f"Each person should pay: ${final_splitup}.")
