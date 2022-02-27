# To check whether the given year is leap yr or not
year = int(input("Enter the year: \n"))

# using if-else condition to check whether the given year is leap year or not.
if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            message = "Leap year."
        else:
            message = "Not a leap year."
    else:
        message = "Leap year."
else:
    message = "Not a leap year."

print(message)
