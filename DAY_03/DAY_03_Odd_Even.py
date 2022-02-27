print("CHECKING ODD OR EVEN")
number = int(input("Enter any number: \n"))
# taking the input of the number to be checked

# Using if-else conditions to check if the number is odd or even
if number % 2 == 0:
    message = "The number is even."
else:
    message = "The number is odd."
print(message)
