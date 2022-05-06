# Reading CSV Data in Python

# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)
# data_list = []
# for _ in data:
#     stripped_data = _.strip()
#     data_list.append(stripped_data)
# print(data_list)

import csv

temperature = []

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
print(temperature)


