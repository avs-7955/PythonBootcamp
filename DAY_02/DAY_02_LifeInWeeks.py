current_age = int(input("Enter your current age:\n"))

age_left = 90 - current_age

age_days = (age_left*365)
age_weeks = (age_left*52)
age_months = (age_left*12)
# Calculating the total number of days, months and weeks in 90 yrs.

print(
    f"You have {age_days} days left,{age_weeks} weeks left and {age_months} months left...!!!")
# Using f-string to print the output
# Claculating the remaining days left with subtracting the age spent to the total days/weeks/months calculated before.
