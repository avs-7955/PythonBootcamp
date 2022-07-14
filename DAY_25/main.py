# This method is very difficult to use.
# with open("./DAY_25/weather_data.csv", 'r') as weather_file:
#     weather_data = weather_file.readlines()
#     print(weather_data)

# ============== ANOTHER WAY ================================
# import csv

# with open("./DAY_25/weather_data.csv") as weather_file:
#     weather_data = csv.reader(weather_file)
#     temperature = []
#     # Appending all the temperatures into a temperature list and converting it into int.
#     for row in weather_data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

# Con -  So much work just for extracting a column from our data.

# ============== USING PANDAS ======================
# Takes the first row to be the headings of each columns and uses it to name.
# Series - 1D data; Dataframes - 2D data i.e. tables
import pandas
weather_data = pandas.read_csv("./DAY_25/weather_data.csv")
# Converts the whole table into a dictionary
weather_dict = weather_data.to_dict()

# Converts a series into a list
weather_temp_list = weather_data["temp"].to_list()


# Using Pandas Series.mean() to find the average temperature.
avg = weather_data["temp"].mean()


# Get data from a row
monday = weather_data[weather_data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_farenheit = monday_temp * 9/5 + 32
# print(monday_temp_farenheit)

# Create a data frame from scratch
data_dict = {
    "Students": ["Amy", "James", "Stephen"],
    "Marks": [23, 34, 45],
}

data = pandas.DataFrame(data_dict)
print(data)
