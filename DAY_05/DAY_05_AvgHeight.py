# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights:\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
count = 0
sum = 0
for std_height in student_heights:
    count += 1
    sum += std_height
avg_height = round(sum/count)
print(f"The average height of the class is {avg_height}.")
