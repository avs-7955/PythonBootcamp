height = float(input("Enter your height in metres:\n"))
weight = float(input("Enter your weight in kg:\n"))
# Getting input of height and weight from the user

bmi_index = weight / height ** 2
# Calculating the bmi_index
print(int(bmi_index))
# Converting the float into integer value and printing it
