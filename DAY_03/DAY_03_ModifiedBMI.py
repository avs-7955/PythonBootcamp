# Getting input of height and weight from the user
height = float(input("Enter your height in metres:\n"))
weight = float(input("Enter your weight in kg:\n"))
# Calculating the bmi_index
bmi_index = weight / height ** 2

# using if-elif-else to get the interpretation correctly.
if(bmi_index < 18.5):
    interpretation = "underweight"
elif(bmi_index < 25):
    interpretation = "normal weight"
elif(bmi_index < 30):
    interpretation = "overweight"
elif(bmi_index < 35):
    interpretation = "obese"
else:
    interpretation = "clinically obese"

# Printing the message using f-string
print(f"Your BMI is {round(bmi_index)}, you are {interpretation}.")
