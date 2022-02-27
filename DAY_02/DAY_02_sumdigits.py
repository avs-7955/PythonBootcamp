import string

from numpy import integer


number = input("Enter a 2 digit number:\n")
# taking the input of the number as a string
first_digit = int(number[0])
second_digit = int(number[1])
# Converting both the digits from string data type to integer
print(first_digit + second_digit)
# Printing the sum of both the digits
